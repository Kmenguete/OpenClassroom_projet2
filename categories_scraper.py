import requests
from bs4 import BeautifulSoup

from get_books_for_category import get_books_for_category


def get_all_categories():
    page = requests.get(
        "http://books.toscrape.com/")  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
    for web in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
        href = web.a.get('href')
        url = "http://books.toscrape.com/{}".format(href)
        print(url)
        get_books_for_category(url)


get_all_categories()
