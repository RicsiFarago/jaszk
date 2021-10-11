import scrapy
from tutorial.items import TutorialItem

class FlucSpider(scrapy.Spider):
    name = "fluc"
    start_urls = ["https://www.fluc.at/programm/2021_Flucwoche25.html"]

    def parse(self, response):

        item = TutorialItem()
        item['title'] = response.xpath('//text()').getall()

        yield item

