import requests
import requests_cache
from bs4 import BeautifulSoup
import re

""" Step 1 - fetch urls to the actual meeting-transcripts.
"""

""" Gesetzgebungsperioden. (timespans / categorziation of transcripts).
    These contain links pages for single meetings where the actual transcripts
    can be obtained from.
"""
SCRAPE_BASE = "http://www.parlament.gv.at"
period_urls = [
    #"http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=EF21125DCF&LISTE=&STEP=&listeId=1070&GP=XXIV&SUCH=&FBEZ=FP_007&pageNumber=&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
    "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=EF21125DCF&LISTE=&STEP=&listeId=1070&GP=XXIV&SUCH=&FBEZ=FP_007&pageNumber=&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
    "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=25796D8B02&LISTE=&STEP=&listeId=1070&GP=XXIII&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
    "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=4F817EE45F&anwenden=Anwenden&LISTE=&STEP=&listeId=1070&GP=XXII&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
    "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=76006EB96E&anwenden=Anwenden&LISTE=&STEP=&listeId=1070&GP=XXI&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
]


""" Set up a simple cache that will be used when fetching documents with 
    the requests module. 
"""
requests_cache.install_cache('cache')

meeting_meta_url = []

for url in period_urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    """ Loop over tr's of a certain table, the first link in every tr is
        the link to an overview-like page for the meeting.
    """ 
    for tr in soup.select('#filterListeFP_007 table tr'):
        links_in_tr = tr.select('a')
        if len(links_in_tr) > 0:
            meeting_meta_url.append(SCRAPE_BASE + links_in_tr[0]['href'])
    
transcripts = []
for url in meeting_meta_url:
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for a in soup.select('div#content div.c_2 a'):
        try:
            doc = a['href']
            if re.match('.*\.pdf$', doc):
                transcripts.append(doc)
                print doc
        except KeyError:
            pass
    
