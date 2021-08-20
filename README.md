# Airbnb_Scraper
 
![Mean_nightly_rate_Deauville](https://user-images.githubusercontent.com/71391244/129249901-372cc8f4-f082-40d7-bf25-37c0b2b79ca1.jpg)

A scraper that acquires data from the Airbnb results page.

Using this script, you are able to search a city, dates, and price range to obtain all of the available listings' name, header, url, price, bedrooms, bathrooms, or any other result on the Airbnb results page. 
# Overview

This scraper is written in Python and utilizes the Scrapy open-source framework (https://scrapy.org/). A request is submitted to the selected URL, which returns a response of the html of the page. CSS selectors or XPaths can be utilized to obtain the desired information from the response, such as listing name or price. Additionally, the link to the following pages in the search result can be obtained from the response with CSS selectors or XPaths. The CSS selector or XPath for the next page is incorporated in the scraper.py file to crawl additional pages to obtain the results of all pages in the search parameters. 

![css](https://user-images.githubusercontent.com/71391244/129333057-758b3b14-e5cc-4b37-a6dd-32e6cc3a1a03.png)

# Folders
* The spider folder contains the scraper.py file with the Scrapy spider. 
* The Scraped Data folder contains all of the individually scraped price ranges in a .json file. 
* The EDA folder contains the Jupyter notebook that combines each .json into a dataframe, cleans the data, and performs an exploratory data analysis to find the mean price per number of bedrooms. 

# Items to Note
*  Airbnb limits search results to 300. In order to find all of the listings in a particular area, you will have to search Airbnb manually to find the breaking point of 300 results. This said, it's relatively easy to find the breaking point of 300 listings when you break the queries into bins based on price range i.e. 0-75, 75-90, 90-110, etc. I would be interested in hearing of ways to automate this. 
*  Your query results will be in the currency of the region of the top-level-domain (TLD) you use. In this script I utilized .ie (Ireland) in order keep the result language in english and currency result in euros. If you are located in the US, you can use .com and it will return USD. There likely is a way to use a VPN, Selenium, or alter the scraper.py file to return search results of different countries in your desired language/currency.
*  It is recomended to alter the settings.py file to limit the amount of requests over a specifed timeframe (https://docs.scrapy.org/en/latest/topics/settings.html#download-delay) and identify yourself (https://docs.scrapy.org/en/latest/topics/settings.html?highlight=user#std-setting-USER_AGENT) in an effort to practice responsible scraping. 
*  Airbnb changes their tags often. The tags used in this script are current as of 08/13/21. You may need to update them if you are trying to run this in the future. 
*  The check-in/check-out dates utilized in these queries was 12/23/21 - 01/-02/22. 

# Timeline
 
7.11.21 - Initial project was written using BeautifulSoup. 
 
7.18.21 - Writing the project to utilize Scrapy in an effort to build a more robust alternative to BS4. 

7.29.21 - I have traveled from the US to France and will be here until 8.19.21. From my understanding this may change the site layout and/or affect my ability to access the Airbnb site as I would in the US.

7.31.21 - Spider parses the first page but does not crawl to additional pages. Researching additional Spider writing methodologies.

8.03.21 - Spider crawls every page for all listings.
  Total listing results equate to:
  20 listings per page x 15 pages ≈ 300 listings. 
  Depending on the area, it seems reasonable to assume that most popular destinations will have > 300 listings.

8.05.21 - Split json results into bins of =< 300 based on min_price and max_price. Added the feauture to the start url via f-string, similar to input dates.

8.09.21 - Conducting exploratory data analysis to find the mean price per bedroom in Deauville, France. 

## To Do ##

* Determine the occupancy rate of each unit size for a given area, i.e. (1 br-70%, 2br-80%) and run automatically every week to determine how many days different unit types usually book prior to arrival and the seasonal occupancy rate - time series (Not Started)
* Determine the amenities that have the largest influence on occupancy rate (maybe binned into price buckets) (maybe find if there is a seasonality of bookings based on amenities). (Not Started)
* Develop a time series to reflect seasonality and model dynamic pricing strategies. Then create a dashboard to assist in the manipulation of the time series. (Not Started)
