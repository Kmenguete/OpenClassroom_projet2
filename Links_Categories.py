import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://books.toscrape.com/")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content, 'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
for web in soup.find_all('a'):
    web.append('http://books.toscrape.com/' + web.get('href'))
    print(web)
