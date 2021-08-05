import requests
from bs4 import BeautifulSoup

from get_books_for_category import get_books_for_category


# The get_all_categories function return book information and their corresponding image file for every category.
# However, this function return only the first page of every category. In the get_all_categories function, we called
# get_books_for_category function that let us to get all book information data and their corresponding image file.


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
