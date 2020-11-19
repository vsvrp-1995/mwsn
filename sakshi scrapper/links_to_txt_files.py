from typing import List

import scrapy


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
    }
    start_urls = [l.strip() for l in open('2020_01_links.txt').readlines()]

    def parse(self, response):

        CSS_SELECTOR = '.rtejustify::text'
        content = response.css(CSS_SELECTOR).extract()

        if (content == None):
            if 'redirect_urls' in response.request.meta:
                yield {
                    'article_content': content,
                    'url': response.request.meta['redirect_urls'][0],
                    'status': 'success',
                }
            else:
                yield {
                    'article_content': content,
                    'url': response.url,
                    'status' : 'success',
                }

        else:
            if 'redirect_urls' in response.request.meta:
                yield {
                    'article_content': content,
                    'url': response.request.meta['redirect_urls'][0],
                    'status': 'success',
                }
            else:
                yield {
                    'article_content': content,
                    'url': response.url,
                    'status' : 'success',
                }