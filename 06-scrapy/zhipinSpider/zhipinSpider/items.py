# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 第 3 行代码表明所有的 Item 类都需要继承 scrapy.Item 类，
# 接下来就为所有需要爬取的信息定义对应的属性，每个属性都是一个 scrapy.Field 对象。

# 该 Item 类只是一个作为数据传输对象（DTO）的类，因此定义该类非常简单。
import scrapy


class ZhipinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    # 工作名称
    title = scrapy.Field()
    # 工资
    salary = scrapy.Field()
    # 招聘公司
    company = scrapy.Field()
    # 工作详细链接
    url = scrapy.Field()
    # 工作地点
    work_addr = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 公司规模
    company_size = scrapy.Field()
    # 招聘人
    recruiter = scrapy.Field()
    # 发布时间
    publish_date = scrapy.Field()
