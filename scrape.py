from bs4 import BeautifulSoup
import requests
import csv

words_to_test = ['stand', 'riser', 'mount', 'bracket', 'rack']

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4.1 Safari/605.1.15"}

csv_header = ["title", "price", "units_sold", "reviews", "percent_off", "location", "average_rating", "five_stars", "four_stars", "three_stars", "two_stars", "one_star"]

with open('Lazada_scrape.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)

for i in range(1, 103):
    word_found = False
    base_url = f'https://www.lazada.com.ph/tag/monitor/?catalog_redirect_tag=true&page={i}&q=monitor&spm=a2o4l.home-ph.search.d_go'
    base_page = requests.get(base_url, headers=headers)
    base_soup = BeautifulSoup(BeautifulSoup(base_page.content, "html.parser").prettify(), "html.parser")
    products = base_soup.find_all('div', class_='Bm3ON')

    try: 
        for product in products:
            try:
                title = product.find('div', class_='RfADt').find('a').get_text().strip()
            except AttributeError:
                continue

            for word in words_to_test:
                if word in title:
                    word_found = True
                    break
            
            if word_found:
                continue
            try:
                price = product.find("span", class_= "ooOxS").get_text()[1:].strip()
            except AttributeError:
                price = None

            try:
                units_sold = product.find("span", class_= "_1cEkb").find("span").get_text().split(" ")[0].strip()
            except AttributeError:
                units_sold = None  

            try:
                reviews = product.find("span", class_= "qzqFw").get_text().translate(str.maketrans('', '', "() "))
            except AttributeError:
                reviews = None  
            
            try:
                percent_off = product.find("span", class_="IcOsH").get_text().split(" ")[0][:-1].strip()
            except AttributeError:
                percent_off = None   
            
            try:
                location = product.find("span", class_="oa6ri ").get_text().strip()
            except AttributeError:
                location = None
            
            try:
                product_url = product.find('div', class_='RfADt').find('a')['href']
            except AttributeError:
                product_url = None
            
            try:
                product_page = requests.get(product_url, headers=headers)
            except AttributeError:
                product_page = None
            
            try:
                product_soup = BeautifulSoup(BeautifulSoup(product_page.content, "html.parser").prettify(), "html.parser")
            except AttributeError:
                product_soup = None

            try:
                ratings = product_soup.find("div", class_="mod-rating")
            except AttributeError:
                ratings = None

            try:
                average_rating = ratings.find("span", class_="score-average").get_text().strip()
            except AttributeError:
                average_rating = None

            try:
                ratings_list = ratings.find("div", class_="detail").find_all("li")
            except AttributeError:
                ratings_list = None

            try:
                five_stars = ratings_list[0].find("span", class_="percent").get_text().strip()
            except AttributeError:
                five_stars = None

            try:
                four_stars = ratings_list[1].find("span", class_="percent").get_text().strip()
            except AttributeError:
                four_stars = None

            try:
                three_stars = ratings_list[2].find("span", class_="percent").get_text().strip()
            except AttributeError:
                three_stars = None
            
            try: 
                two_stars = ratings_list[3].find("span", class_="percent").get_text().strip()
            except AttributeError:
                two_stars = None
            
            try:
                one_star = ratings_list[4].find("span", class_="percent").get_text().strip()
            except AttributeError:
                one_star = None

            row = [title, price, units_sold, reviews, percent_off, location, average_rating, five_stars, four_stars, three_stars, two_stars, one_star]

            with open('Lazada_scrape.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
    except AttributeError:
        pass

