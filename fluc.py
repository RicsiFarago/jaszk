import scrapy
from tutorial.items import TutorialItem

class FlucSpider(scrapy.Spider):
    name = "fluc"

    x = 42
    y = 43

    start_urls = ["https://www.fluc.at/programm/2021_Flucwoche%s.html" % y]


def parse(self, response):

        item = TutorialItem()
        item['title'] = response.xpath('//text()').getall()

        yield item
