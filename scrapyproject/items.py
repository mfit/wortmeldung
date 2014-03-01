from scrapy.item import Item, Field


class WordSection(Item):
    """ Represents a section of a protocol ( "Wortmeldung" / Speech )
    """

    TAG_TYPE_ABG = 'abg'
    TAG_TYPE_OTHER = 'unknown'

    section = Field()
    rawcontent = Field()
    content = Field()
    contentParts = Field()
    speaker = Field()
    title = Field()
    party = Field()
    timeBegin = Field()

    originalDocument = Field()
    sitzung = Field()
    index = Field()

    date = Field()
    timestamps = Field()
    reactions = Field()
    cssclasses = Field()
    links = Field()
    tags = Field()
    urltags = Field()

    scraping_date = Field()


class TranscriptItem(Item):
    """ Represents a protocol.
    """
    url = Field()
    contents = Field()
    headline = Field()
    date_str = Field()
    date = Field()
    year = Field()
    sitzung = Field()
    urltags = Field()
    scraping_date = Field()
    house = Field()
    visited = Field()
