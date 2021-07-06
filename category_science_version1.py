import requests
from bs4 import BeautifulSoup
import time

page = requests.get(
    "http://books.toscrape.com/catalogue/category/books/science_22/index.html")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content,
                     'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
link = soup.find_all('h3')
links = []
for h3 in link:
    a = h3.find('a')
    web = a['href']
    links.append('http://books.toscrape.com/catalogue/science_22/index.html' + web)

with open('urls.txt', 'r') as file:
    for row in file:
        url = row.strip()
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            product_page_url = url
            universal_product_code = soup.find_all('tr')[0].get_text()
            title = soup.find('h1').get_text()
            price_including_tax = soup.find_all('tr')[3].get_text()
            price_excluding_tax = soup.find_all('tr')[2].get_text()
            number_available = soup.find_all('tr')[5].get_text()
            product_description_head = soup.find_all('h2')[0].get_text()
            product_description = soup.find_all('p')[3].get_text()
            category = soup.find_all('a')[3].get_text()
            review_rating = soup.find_all('tr')[6].get_text()
            image_url = soup.find_all('img')[0]
            print(product_page_url)
            print(universal_product_code)
            print(title)
            print(price_including_tax)
            print(price_excluding_tax)
            print(number_available)
            print(product_description_head)
            try:
                print(product_description)
            except:
                print("********** Error, cannot display description **********")
            print(category)
            print(review_rating)
            print(image_url)
        time.sleep(3)