from typing import List

import scrapy


class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [l.strip() for l in open('section_links_may.txt').readlines()]

    def parse(self, response):

        XPATH_SELECTOR = '//ul[@class="article-box-list no-space-t no-space-b"]/li/a/text()'
        content = response.xpath(XPATH_SELECTOR).extract()
        XPATH_SELECTOR2 = '//ul[@class="article-box-list no-space-t no-space-b"]/li/a/@href'
        content2 = response.xpath(XPATH_SELECTOR2).extract()
        print(len(content))
        print(len(content2))

        if (content == None):
            if 'redirect_urls' in response.request.meta:
                yield {
                    'base_url': response.request.meta['redirect_urls'][0],
                    'status': 'error',
                }
            else:
                yield {
                    'base_url': response.url,
                    'status': 'error',
                }
        else:
            for i in range(len(content)):
                data = content[i]
                link = content2[i]
                if 'redirect_urls' in response.request.meta:
                    yield {
                        'headline' : data,
                        'url' : link,
                        'base_url': response.request.meta['redirect_urls'][0],
                        'status': 'success',
                    }
                else:
                    yield {
                        'headline' : data,
                        'url' : link,
                        'base_url': response.url,
                        'status': 'success',
                    }


def remove_html_tags(text):
    """Remove html tags from a string"""
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
