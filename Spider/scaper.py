import scrapy

class ListsSpider(scrapy.Spider):
    name = "listings"

    city = 'Nashville-TN'
    check_in = '2022-08-25'
    check_out = '2022-08-28'

    start_urls = [
        f'https://www.airbnb.ie/s/{city}/homes?&checkin={check_in}&checkout={check_out}&adults=16&price_max=1100&display_currency=EUR'
    ]


    def parse(self, response):
        for tile in response.css('div._1e541ba5'):
            yield {
                'name': tile.css('span._1whrsux9 ::text').get(),
                'header': tile.css('div._1olmjjs6 ::text').get(),
                'link': tile.css('a ::attr(href)').get(),
                'guests': (tile.css('span._3hmsj ::text').extract())[0],
                'bedrooms': (tile.css('span._3hmsj ::text').extract())[1],
                'beds': (tile.css('span._3hmsj ::text').extract())[2],
                'bathrooms': (tile.css('span._3hmsj ::text').extract())[3],
                'price': (tile.css('span._1p7iugi ::text')).get(),
                'rating': tile.css('span._10fy1f8 ::text').get(),
                # 'num_reviews': (tile.css('span._a7a5sx ::text').extract())[2]
                # 'superhost': tile.css('div._1u0inz4').get()
            }
        next_page = response.css('a._za9j7e ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
