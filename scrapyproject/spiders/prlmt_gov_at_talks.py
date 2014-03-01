from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from items import WordSection
from pymongo import Connection
import re


class FetchTalksSpider(Spider):
    """ Fetch talks/parts of one session.
    """

    name = "at_parlament_talks"
    regexStripTags = re.compile('<.*?>')
    regexFindSpeaker = re.compile('([^:]*):')

    def start_requests(self):
        """ Retrieve unvisited url(s) from the database.
        """
        connection = Connection()
        db = connection.protokolle
        requests = []
        item = db.protokoll.find({'visited': 0}).next()
        requests.append(Request(item['url'], callback=self.parse))

        item['visited'] = 1  # mark as visited
        db.protokoll.save(item)

        return requests

    def parse(self, response):
        urltags = [t for t in response.url.split('/') \
                   if t not in ["http:", ""]]
        sitzungsnr = ""
        for part in urltags:
            if "NRSITZ_" in part:
                sitzungsnr = part

        # Select divs with class="section"
        hxs = HtmlXPathSelector(response)
        items = hxs.select('//div[contains(@class, \'Section\')]')
        for item_index, item in enumerate(items):
            # get section name
            classnames = item.select('@class').extract()
            wordsection = classnames.pop() if len(classnames) > 0 else ""

            # get text from various p-classes
            textparts = []
            timestamps = []
            pclasses = set()
            cleaned_parts = []
            links = []

            for txt in item.select('p'):
                pclass = txt.select('@class').extract().pop().strip()
                pclasses.add(pclass)
                if pclass in ["MsoNormal", "StandardRB", "MsoListBullet"]:
                    text = txt.extract()
                    textparts.append(text)
                    textclean = ''.join(self.regexStripTags.split(text))\
                        .strip()
                    cleaned_parts.append(textclean)

                if pclass in ["RE"]:
                    timestamps.append(''.join(self.regexStripTags.\
                                              split(txt.extract())).strip())

            textpart = ''.join(textparts)
            textpart = ' '.join(textpart.splitlines())

            links = re.findall('<a href="([^"]*)"[^>]*>(.*?)</a>', textpart)
            cleantext = ''.join(self.regexStripTags.split(textpart)).strip()

            # setup item
            ws = WordSection()
            ws['index'] = item_index
            ws['content'] = cleantext
            ws['section'] = wordsection
            ws['originalDocument'] = response.url
            ws['rawcontent'] = textpart
            ws['speaker'] = ''
            ws['party'] = ''
            ws['title'] = ''
            ws['reactions'] = re.findall('\((.*?)\)', cleantext)
            ws['timestamps'] = timestamps
            ws['cssclasses'] = list(pclasses)
            ws['urltags'] = urltags
            ws['sitzung'] = sitzungsnr
            ws['contentParts'] = cleaned_parts
            ws['links'] = links

            if len(timestamps) > 0:
                ws['timeBegin'] = timestamps[0]
            speaker_parts = self.regexFindSpeaker.match(cleantext)

            if not speaker_parts == None:
                speakertext = speaker_parts.group(1)
                party = re.search('\((.*?)\)', speakertext)
                if not party == None:
                    ws['party'] = party.group(1).strip()
                    speakertext = re.sub('\(.*?\)', '',  speakertext)

                title = re.match('([^\W].*?)\W', speakertext, re.UNICODE)
                if not title == None:
                    ws['title'] = title.group(1).strip()
                    speakertext = re.sub(ws['title'], '',
                                         speakertext, re.UNICODE)
                    ws['tags'] = WordSection.TAG_TYPE_ABG \
                        if ws['title'] in ['Abgeordneter', 'Abgeordnete'] \
                        else WordSection.TAG_TYPE_OTHER

                ws['speaker'] = speakertext.strip()

            yield ws
