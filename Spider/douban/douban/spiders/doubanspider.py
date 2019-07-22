# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.http import Request

class Douban(CrawlSpider):
    name = 'douban'
    start_urls = ['http://movie.douban.com/top250']
    firstPageUrl = 'http://movie.douban.com/top250'

    def parse(self, response):
        item = DoubanItem()
        selector = Selector(response)
        movieInfos = selector.xpath("//div[@class='info']")

        for mi in movieInfos:
            title = mi.xpath("div[@class='hd']/a/span/text()").extract()
            fullTitle = ''
            for t in title:
                fullTitle += t

            movieInfo = mi.xpath("div[@class='bd']/p/text()").extract()
            movieInfoStriped = ''
            for txt in movieInfo:
                movieInfoStriped += txt.strip()

            star = mi.xpath("div[@class='bd']/div[@class='star']/span[2]/text()").extract()
            evaluation = mi.xpath("div[@class='bd']/div[@class='star']/span[4]/text()").extract()
            quote = mi.xpath("div[@class='bd']/p[@class='quote']/span[1]/text()").extract()
            if quote:
                pass
            else:
                quote = ''

            item['title'] = fullTitle
            item['movieInfo'] = movieInfoStriped
            item['star'] = star
            item['evaluation'] = evaluation
            item['quote'] = quote
            yield item

            nextlink = selector.xpath("//div[@class='paginator']//span[@class='next']//link/@href").extract()[0]
            if nextlink:
                yield Request(self.firstPageUrl + nextlink, callback=self.parse)

            print('#'*10, self.firstPageUrl + nextlink, '#'*10)