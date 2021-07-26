
import requests
from bs4 import BeautifulSoup
from Book_detailed_scraper import book_extract_information, store_book_information


def get_books_for_category(url):
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
            book_info = book_extract_information(book_link)
            store_book_information(book_info)


get_books_for_category("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
