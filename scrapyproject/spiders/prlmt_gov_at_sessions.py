# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from items import TranscriptItem
import datetime
import re
from scrapy.utils.project import get_project_settings


class FetchTranscriptSpider(Spider):
    """ Fetch sessions ('sitzungen') data, 
        including title, date and link to actual transcript.
    """

    name = 'at_parlament_sessions'
    allowed_domains = ['parlament.gv.at']
    house_name = 'parlament.gv.at'
    monthparse = ["Jänner", "Februar", "März", 
                  "April", "Mai", "Juni", 
                  "Juli", "August", "September",
                  "Oktober", "November", "Dezember"] 

    start_urls = []

    def __init__(self, *args, **kwargs):
        super(FetchTranscriptSpider, self).__init__(*args, **kwargs)
        settings = get_project_settings()
        self.start_urls = settings['PARL_GOVAT_STARTURLS']

    def parse(self, response):
        """ This parser extracts links to a sitzungs overview file.
        """
        hxs = HtmlXPathSelector(response)
        links = hxs.select('//div[@id=\'filterListeFP_007\']/table/tr/td/a')

        for link in links:
            title = link.select('text()').extract().pop().strip()
            href = link.select('@href').extract().pop().strip()
            if "Sitzung" in title:
                href = "http://www.parlament.gv.at" + href
                yield Request(url=href, callback=self.parseSitzungOverview)

    def parseSitzungOverview(self, response):
        hxs = HtmlXPathSelector(response)
        liitems = hxs.select('//div[@class="contentBlock"]/div[@class="reiterBlock"]/div[@class="c_2"]/div[@class="c_2"]/ul/li')
        if len(liitems) > 0:
            links = liitems[0].select('a')
            if len(links) > 1:
                linktext = links[0].select('text()').extract().pop().strip()
                if "Stenographisches Protokoll" in linktext:
                    # take the *next* link, it' link to the the HTML version:
                    href = "http://www.parlament.gv.at" + links[1].\
                        select('@href').extract().pop().strip()
                    item = TranscriptItem(url=href)
                    urltags = href.split('/')
                    urltags.remove("http:")
                    urltags.remove("")
                    item['urltags'] = urltags
                    item['sitzung'] = ""
                    for part in urltags:
                        if "NRSITZ_" in part:
                            item['sitzung'] = part

                    headline = hxs.select('//h1[@id="inhalt"]/text()').\
                        extract()

                    # extract date from headline
                    if len(headline) > 0:
                        item['headline'] = headline[0]
                        dateparts = re.findall('([0-9]{1,2})\. *([A-z]+) *([0-9]{4})', headline[0], re.UNICODE)
                        if len(dateparts) > 0:
                            item['date_str'] = '.'.join(dateparts[0])
                            item['year'] = dateparts[0][2]
                            try:
                                item['date'] =  \
                                    datetime.datetime(int(dateparts[0][2]),
                                                  self.monthparse.index(dateparts[0][1]) + 1,
                                                  int(dateparts[0][0]))

                            except ValueError:
                                pass

                    item['scraping_date'] = datetime.datetime.utcnow()
                    item['house'] = self.house_name
                    item['visited'] = 0

                    yield item
