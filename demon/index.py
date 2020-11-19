from typing import List

import scrapy


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [l.strip() for l in open('test.txt').readlines()]

    def parse(self, response):
        list_of_words = open("words.txt").read().split()
        matrix: List[int] = []

        CSS_SELECTOR = '.Normal'
        content = response.css(CSS_SELECTOR).extract_first()
        if (content == None):
            CSS_SELECTOR = '._3WlLe'
            content = response.css(CSS_SELECTOR).extract_first()
        if (content == None):
            for word in range(len(list_of_words)):
                matrix.append(0)
            yield {
                'finalmatrix': matrix,
                'url': response.request.meta['redirect_urls'][0],
                'status': 'error',
            }
        content = content.lower()
        for word in range(len(list_of_words)):
            matrix.append(content.count(list_of_words[word]))
        yield {
            'finalmatrix': matrix,
            'url': response.request.meta['redirect_urls'][0],
            'status' : 'success',
        }
