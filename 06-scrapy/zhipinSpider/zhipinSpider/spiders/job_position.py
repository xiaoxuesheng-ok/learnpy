# -*- coding: utf-8 -*-
import scrapy
from zhipinSpider.items import ZhipinspiderItem


class JobPositionSpider(scrapy.Spider):
    # 定义该Spider的名字
    name = 'job_position'
    # 定义该Spider允许爬取的域名
    allowed_domains = ['zhipin.com']
    # 定义该Spider爬取的首页列表
    start_urls = ['https://www.zhipin.com/c101280100/h_101280100/']

# 开发者只要在 start_urls 列表中列出所有需要 Spider 爬取的页面 URL，
# 这些页面的数据就会“自动”传给 parse(self, response) 方法的 response 参数。

#因此，开发者主要就是做两件事情：
#将要爬取的各页面 URL 定义在 start_urls 列表中。
#在 parse(self, response) 方法中通过 XPath 或 CSS 选择器提取项目感兴趣的信息。

    # 该方法负责提取response所包含的信息
    # response代表下载器从start_urls中每个URL下载得到的响应
    def parse(self, response):
        # 遍历页面上所有//div[@class="job-primary"]节点
        for job_primary in response.xpath('//div[@class="job-primary"]'):
            item = ZhipinspiderItem()
            # 匹配//div[@class="job-primary"]节点下/div[@class="info-primary"]节点
            # 也就是匹配到包含工作信息的<div.../>元素
            info_primary = job_primary.xpath('./div[@class="info-primary"]')
            item['title'] = info_primary.xpath('./h3/a/div[@class="job-title"]/text()').extract_first()
            item['salary'] = info_primary.xpath('./h3/a/span[@class="red"]/text()').extract_first()
            item['work_addr'] = info_primary.xpath('./p/text()').extract_first()
            item['url'] = info_primary.xpath('./h3/a/@href').extract_first()
            # 匹配//div[@class="job-primary"]节点下./div[@class="info-company"]节点下
            # 的/div[@class="company-text"]的节点
            # 也就是匹配到包含公司信息的<div.../>元素
            company_text = job_primary.xpath('./div[@class="info-company"]' +
                '/div[@class="company-text"]')
            item['company'] = company_text.xpath('./h3/a/text()').extract_first()
            company_info = company_text.xpath('./p/text()').extract()
            if company_info and len(company_info) > 0:
                item['industry'] = company_info[0]
            if company_info and len(company_info) > 2:
                item['company_size'] = company_info[2]
            # 匹配//div[@class="job-primary"]节点下./div[@class="info-publis"]节点下
            # 也就是匹配到包含发布人信息的<div.../>元素
            info_publis = job_primary.xpath('./div[@class="info-publis"]')
            item['recruiter'] = info_publis.xpath('./h3/text()').extract_first()
            item['publish_date'] = info_publis.xpath('./p/text()').extract_first()
            yield item
        # 解析下一页的链接
        new_links = response.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()
        if new_links and len(new_links) > 0:
            # 获取下一页的链接
            new_link = new_links[0]
            # 再次发送请求获取下一页数据
            yield scrapy.Request("https://www.zhipin.com" + new_link, callback=self.parse)

# 第 57 行代码显式使用 scrapy.Request 来发送请求，
# 并指定使用 self.parse 方法来解析服务器响应数据。需要说明的是，这是一个递归操作，
# 即每当 Spider 解析完页面中项目感兴趣的工作信息之后，它总会再次请求“下一页”数据，
# 通过这种方式即可爬取广州地区所有的热门职位信息。
