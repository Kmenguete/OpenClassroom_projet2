import time
import csv

import requests
from bs4 import BeautifulSoup


def store_book_information(product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                           number_available, product_description_head, product_description, category,
                           review_rating,  image_url):

    with open('book_information_storage.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["product_page_url", product_page_url])
        writer.writerow(["universal_product_code(upc)", universal_product_code])
        writer.writerow(["title", title])
        writer.writerow(["price_including_tax", price_including_tax])
        writer.writerow(["price_excluding_tax ", price_excluding_tax])
        writer.writerow(["number_available", number_available])
        writer.writerow(["product_description_head", product_description_head])
        writer.writerow(["product_description", product_description])
        writer.writerow(["category", category])
        writer.writerow(["review_rating ", review_rating])
        writer.writerow(["image_url", image_url])


def book_extract_information(url):
    time.sleep(3)

    page = requests.get(url)  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document

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
    store_book_information(product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
                           number_available, product_description_head, product_description, category,
                           review_rating, image_url)


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


book_extract_information(url)
