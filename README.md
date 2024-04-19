# Lazada Web Scraping Project

This is a web scraping project that scrapes data from Lazada. The data is scraped from a search result page with input 'monitor'. Each product of each page is considered a row with columns: title, price, units_sold, reviews, percent_off, location, average_rating, five_stars, four_stars, three_stars, two_stars, one_star.

**NOTE: Lazada has a security feature that detects unusual activity through a network. This feature is difficult to bypass which prevents web scraping of the site. This project only shows the concepts and methods used to possibly scrape the product data from the search. No CSV file or table was created.**

## Search Page

This is what a search page looks like.

(insert page)

There is a list of products in grid format, and there is a list of pages at the bottom.

Through inspection the page urls can be iterated through using a loop similar to this

for i in range(1, 103):
base_url = f'https://www.lazada.com.ph/tag/monitor/?catalog_redirect_tag=true&page={i}&q=monitor&spm=a2o4l.home-ph.search.d_go'

The 'monitor' search input gave a result of 102 pages.

### Product

(insert page)

Looking at a product from the search page we can extract the title, price, units_sold, reviews, percent_off, and location

The ratings of the products cannot be seen on the search page.

## Product Page

(insert page)

Instecting the title of the product, an anchor tag can be seen which leads to the product page.

(insert pic)

In this product page we can find the average_rating, five_stars, four_stars, three_stars, two_stars, and one_star. The five_stars, four_stars, three_stars, two_stars, and one_star columns refer to the number of each rating.
