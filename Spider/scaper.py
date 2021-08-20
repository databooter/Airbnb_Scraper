import scrapy

class ListsSpider(scrapy.Spider):
    # name of spider
    name = "listings"

    # change this variable to desired city (must be formatted "City-State_or_Country")
    city = 'Deauville-Fr'

    # change these variables to desired timeframe (must be formatted "YYYY-MM-DD")
    check_in = ''
    check_out = ''

    # change these variables to desired price range (must use price range bins to obtain more than 300 listings)
    price_max = ""
    price_min = ""

    # The starting url formatted as an f-string with above variables
    start_urls = [
        f'https://www.airbnb.ie/s/{city}/homes?&checkin={check_in}&checkout={check_out}&price_min={price_min}&price_max{price_max}&display_currency=EUR'
    ]

    # parse
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
                'rating': tile.css('span._10fy1f8 ::text').get()
            }
        # crawl
        next_page = response.css('a._za9j7e ::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)