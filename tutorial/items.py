# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FilmItem(scrapy.Item):
	name = scrapy.Field()
	url = scrapy.Field()

class JdItem(scrapy.Item):
	title = scrapy.Field()
	
class ESFItem(scrapy.Item):
	id = scrapy.Field()
	publish_time = scrapy.Field()
	title = scrapy.Field()
	total_price = scrapy.Field()
	house_type = scrapy.Field()
	house_build_area = scrapy.Field()
	house_use_area = scrapy.Field()
	house_age = scrapy.Field()
	orientation = scrapy.Field()
	floor = scrapy.Field()
	structure = scrapy.Field()
	decoration = scrapy.Field()
	residential_category = scrapy.Field()
	building_class = scrapy.Field()
	property_right = scrapy.Field()
	property_name = scrapy.Field()
	school = scrapy.Field()
	
class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
