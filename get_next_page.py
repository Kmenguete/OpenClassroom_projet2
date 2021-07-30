import requests
from bs4 import BeautifulSoup
from get_books_for_category import get_books_for_category


# The get_next_page function has the purpose to get book information and their corresponding image file for categories
# with more than one page. However, the get_next_page file return only categories with more than one page. In the
# get_next_page function, we called get_books_for_category function that let us to get all book information data and
# their corresponding image file.


def get_next_page():
    page = requests.get("http://books.toscrape.com/")  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
    for web in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
        href = web.a.get('href')
        url = "http://books.toscrape.com/{}".format(href.replace("index", "page-1"))
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        next_li = soup.find('li', class_='next')
        incrementor = 1
        while next_li is not None:
            url = "http://books.toscrape.com/{}".format(href.replace("index", "page-{}".format(incrementor)))
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            next_li = soup.find('li', class_='next')
            print(url)
            get_books_for_category(url)
            incrementor += 1


get_next_page()
# return url
