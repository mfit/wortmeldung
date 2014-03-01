BOT_NAME = 'Scrapy Open Data Import'
SPIDER_MODULES = ['spiders']

# ITEM_PIPELINES = [
#     'pipelines.StoreToMongoDbPipeline',
# ]

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS = 1

PIPELINE_MONGO_DB = "transcripts"
PIPELINE_MONGO_SESS_COL = "sessions"
PIPELINE_MONGO_TALK_COL = "talks"

# Gesetzgebungsperioden
PARL_GOVAT_STARTURLS = [
        #"http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=EF21125DCF&LISTE=&STEP=&listeId=1070&GP=XXIV&SUCH=&FBEZ=FP_007&pageNumber=&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
        "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=EF21125DCF&LISTE=&STEP=&listeId=1070&GP=XXIV&SUCH=&FBEZ=FP_007&pageNumber=&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
        "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=25796D8B02&LISTE=&STEP=&listeId=1070&GP=XXIII&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
        "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=4F817EE45F&anwenden=Anwenden&LISTE=&STEP=&listeId=1070&GP=XXII&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
        "http://www.parlament.gv.at/PAKT/PLENAR/index.shtml?NRBRBV=NR&R_SISTEI=SI&requestId=76006EB96E&anwenden=Anwenden&LISTE=&STEP=&listeId=1070&GP=XXI&SUCH=&pageNumber=&FBEZ=FP_007&EING=ALLE&xdocumentUri=%2FPAKT%2FPLENAR%2Findex.shtml&STATT=ALLE&jsMode=",
    ]
