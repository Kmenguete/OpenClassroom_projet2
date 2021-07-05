import requests
from bs4 import BeautifulSoup


page = requests.get("http://books.toscrape.com/")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content, 'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
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
        incrementor += 1


def get_next_page():
    return url
