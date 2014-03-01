BOT_NAME = 'Scrapy Open Data Import'
SPIDER_MODULES = ['spiders']

ITEM_PIPELINES = [
     'pipelines.StoreToMongoDbPipeline',
]

CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS = 1

PIPELINE_MONGO_DB = "transcripts"
PIPELINE_MONGO_SESS_COL = "sessions"
PIPELINE_MONGO_TALK_COL = "talks"

# Gesetzgebungsperioden
PARL_GOVAT_STARTURLS = [
]
