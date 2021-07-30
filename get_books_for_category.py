
import requests
from bs4 import BeautifulSoup
from Book_detailed_scraper import book_extract_information, store_book_information


# the goal of the get_books_for_category function is to get every book information for one category. Here, we took
# the category travel as an example. Inside this function, we called book_extract_information function and
# store_book_information function from the Book_detailed_scraper file. This is the Book_detailed_scraper file that let
# us to get book information, directory, folders and file for one category.


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
