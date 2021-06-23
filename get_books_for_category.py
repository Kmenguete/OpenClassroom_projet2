import requests
from bs4 import BeautifulSoup
import time

from Book_detailed_scraper import book_extract_information


def get_books_for_category(url):
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
