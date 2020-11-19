from typing import List

import scrapy


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
    }
    start_urls = [l.strip() for l in open('links.txt').readlines()]

    def parse(self, response):
        list_of_words = open("words.txt", encoding="utf-8").read().split()
        print(len(list_of_words))
        matrix: List[int] = []

        XPATH_SELECTOR = "//div[@class='db-contentScn']/div[not(@*)]"
        content = response.xpath(XPATH_SELECTOR).extract()

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
            s = ' '
            final_content = s.join(content)
            content = remove_html_tags(final_content)
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