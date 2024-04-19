# Lazada Web Scraping Project

This is a web scraping project that scrapes data from Lazada. The data is scraped from a search result page with input 'monitor'. Each product on each page is considered a row with columns: title, price, units_sold, reviews, percent_off, location, average_rating, five_stars, four_stars, three_stars, two_stars, and one_star.

**NOTE: Lazada has a security feature that detects unusual activity through a network. This feature is difficult to bypass which prevents web scraping of the site. This project only shows the concepts and methods used to scrape the product data from the search. No CSV file or table was created.**

## Search Page

<img width="1428" alt="Screenshot 2024-04-19 at 11 22 34 AM" src="https://github.com/lemonjerome/Lazada_Web_Scraping_Project/assets/106641504/b042e55b-cf69-4036-83d5-81bef61da05b">

This is what a search page looks like.

<img width="1428" alt="Screenshot 2024-04-19 at 11 22 46 AM" src="https://github.com/lemonjerome/Lazada_Web_Scraping_Project/assets/106641504/3bd02301-6b41-47db-8820-e6aeba0e1962">

There is a list of products in grid format and a list of pages at the bottom.

Through inspection, the page URLs can be iterated using a loop similar to this

for i in range(1, 103):
base_url = f'https://www.lazada.com.ph/tag/monitor/?catalog_redirect_tag=true&page={i}&q=monitor&spm=a2o4l.home-ph.search.d_go'

The 'monitor' search input gave a result of 102 pages.

### Product

<img width="268" alt="Screenshot 2024-04-19 at 11 23 02 AM" src="https://github.com/lemonjerome/Lazada_Web_Scraping_Project/assets/106641504/4b4527ca-b9ff-4ef2-90f3-ecf182c8c624">

Looking at a product from the search page we can extract the title, price, units_sold, reviews, percent_off, and location

The ratings of the products cannot be seen on the search page.

## Product Page

<img width="1440" alt="Screenshot 2024-04-19 at 11 23 44 AM" src="https://github.com/lemonjerome/Lazada_Web_Scraping_Project/assets/106641504/1ebeb1b1-09b3-498e-94ae-a59dfa055449">

Inspecting the title of the product, an anchor tag can be seen which leads to the product page.

<img width="1440" alt="Screenshot 2024-04-19 at 11 24 11 AM" src="https://github.com/lemonjerome/Lazada_Web_Scraping_Project/assets/106641504/bb3506ce-f2d7-4e6e-a46f-b015971a1650">

On this product page, we can find the average_rating, five_stars, four_stars, three_stars, two_stars, and one_star. The five_stars, four_stars, three_stars, two_stars, and one_star columns refer to the number of each rating.
