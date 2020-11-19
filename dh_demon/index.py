from typing import List

import scrapy


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [l.strip() for l in open('links.txt').readlines()]

    def parse(self, response):
        list_of_words = open("words.txt").read().split()
        matrix: List[int] = []

        CSS_SELECTOR = '.content'
        content = response.css(CSS_SELECTOR).extract_first()
        # if (content == None):
        #     CSS_SELECTOR = '._3WlLe'
        #     content = response.css(CSS_SELECTOR).extract_first()
        if (content == None):
            for word in range(len(list_of_words)):
                matrix.append(0)
            if 'redirect_urls' in response.request.meta:
                yield {
                    'finalmatrix': matrix,
                    'url': response.request.meta['redirect_urls'][0],
                    'status': 'error',
                }
            else:
                yield {
                    'finalmatrix': matrix,
                    'url': response.url,
                    'status' : 'error',
                }
        else:
            content = remove_html_tags(content)
            content = content.lower()
            for word in range(len(list_of_words)):
                matrix.append(content.count(list_of_words[word]))
            if 'redirect_urls' in response.request.meta:
                yield {
                    'finalmatrix': matrix,
                    'url': response.request.meta['redirect_urls'][0],
                    'status': 'success',
                }
            else:
                yield {
                    'finalmatrix': matrix,
                    'url': response.url,
                    'status' : 'success',
                }


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)