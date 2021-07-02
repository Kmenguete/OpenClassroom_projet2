import csv
import requests
from bs4 import BeautifulSoup
import time


from Book_detailed_scraper import book_extract_information


def store_category_book_data(url, book_link):
    incrementor = 0
    while url is not None:
        with open('category_{}.csv'.format(incrementor), 'w', newline='', encoding='utf-8') as file:
            book_data = requests.get(book_link)
            if book_data.ok:
                soup = BeautifulSoup(book_data.text, 'html.parser')
                product_page_url = book_link
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
                incrementor += 1


def get_books_for_category():
    time.sleep(3)
    page = requests.get("https://books.toscrape.com/")  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document

    for web in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
        href = web.a.get('href')
        url = "https://books.toscrape.com/{}".format(href)
        # time.sleep(3)
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'html.parser')
            link = soup.find_all('h3')
            for h3 in link:
                a = h3.find('a')
                href = a.get('href')
                links = 'https://books.toscrape.com/catalogue' + href
                book_link = str(links).replace("../../..", "")
                print(book_link)
                book_extract_information(book_link)
                store_category_book_data(url, book_link)


get_books_for_category()
