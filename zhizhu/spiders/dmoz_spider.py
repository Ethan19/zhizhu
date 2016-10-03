import scrapy

from zhizhu.items import DmozItem

class DmozSpider(scrapy.Spider):
	name="dmoz"
	allwoed_domains=['dmoz.org']
	start_urls=["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"]

	def parse(self,response):
		item = DmozItem()
		item['title'] = response.css("title::text").extract()
		yield item


