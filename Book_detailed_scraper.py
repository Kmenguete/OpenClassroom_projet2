import requests
from bs4 import BeautifulSoup
import time

import requests
from bs4 import BeautifulSoup


def book_extract_information(url):
    time.sleep(3)
    page = requests.get(url)  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document

    print(url)
    print(soup.find('h1').get_text())
    print(soup.find_all('h2')[0].get_text())
    print(soup.find_all('p')[3].get_text())
    print(soup.find_all('tr')[0].get_text())
    print(soup.find_all('tr')[2].get_text())
    print(soup.find_all('tr')[3].get_text())
    print(soup.find_all('tr')[5].get_text())
    print(soup.find_all('a')[3].get_text())
    print(soup.find_all('tr')[6].get_text())
    print(soup.find_all('img')[0])
