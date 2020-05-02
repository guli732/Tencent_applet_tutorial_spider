# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Tencent_applet_tutorial_spider.items import TencentAppletTutorialSpiderItem


class TencentAppSpiderSpider(CrawlSpider):
    name = 'tencent_app_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//p[@class='authors']/span/text()").get()
        article_introduce = response.xpath("//div[@class='blockquote']/p/text()").get()
        url = response.url
        item = TencentAppletTutorialSpiderItem(title=title, author=author, pub_time=pub_time, article_introduce=article_introduce, url=url)
        yield item