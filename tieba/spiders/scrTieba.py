# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem

class ScrtiebaSpider(scrapy.Spider):
    name = 'scrTieba'
    #allowed_domains = ['tieba.baidu.com/p/5818787302?pn=1']
    start_urls = ['http://tieba.baidu.com/p/5818787302?pn=1/']

    def parse(self, response):

        for items in response.css('div.l_post.l_post_bright.j_l_post.clearfix'):
            var=TiebaItem()
            var['author']=items.css('div.d_author>ul.p_author>li.d_name>a::text').extract()
            var['image_urls']=items.css('div.d_post_content_main>div.p_content>cc>div>img::attr(src)').extract()
            if not var['image_urls']:
                continue
            yield var
        next_url=response.css(' div.l_thread_info > ul > li.l_pager.pager_theme_5.pb_list_pager > a:nth-child(7)::attr(href)').extract_first()
        if next_url:
            next_url=response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
