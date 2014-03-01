from pymongo import Connection
from items import WordSection
from items import TranscriptItem
from scrapy.utils.project import get_project_settings


class StoreToMongoDbPipeline():

    def open_spider(self, spider):
        """ Set up mongo-db connection
        """

        settings = get_project_settings()
        dbname = settings.get("PIPELINE_MONGO_DB", "transcripts")
        col_talks = settings.get("PIPELINE_MONGO_TALK_COL", "talks")
        col_session = settings.get("PIPELINE_MONGO_SESS_COL", \
                                          "sessions")
        connection = Connection()
        db = connection[dbname]
        self.talkCollection = db[col_talks]
        self.protokollCollection = db[col_session]

    def process_item(self, item, spider):
        """ Store item in the according collection
        """

        if isinstance(item, TranscriptItem):
            self.protokollCollection.insert(dict(item))

        if isinstance(item, WordSection):
            self.talkCollection.insert(dict(item))

        return item
