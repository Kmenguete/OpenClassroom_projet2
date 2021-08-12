import os
import time
import csv
import requests
from bs4 import BeautifulSoup
"""
The goal of the Book_detailed_scraper file is to get book information and image file of one book. On this file,
 we took the book 'A light in the attic' as an example. The file consist of two functions: the
def store_book_information function and the def book_extract_information function. def store_book_information is a
 function that store book information into a csv file. The goal is to get one csv file per category with their
 corresponding book information.
"""
fieldnames = [
    'product_page_url',
    'universal_product_code',
    'title',
    'price_including_tax',
    'price_excluding_tax',
    'number_available',
    'product_description',
    'category',
    'review_rating',
    'full_image_url',
]


def store_book_information(book_information_as_list):
    converted_list = [str(element) for element in book_information_as_list]
    category_name = book_information_as_list[7]  # Category is index 8 in book_information_as_list
    book_information_as_string = "|".join(converted_list).replace("\n", "")
    print(book_information_as_string)
    directory = 'books/{}'.format(category_name)

    rows = {
        'product_page_url': book_information_as_list[0],
        'universal_product_code': book_information_as_list[1],
        'title': book_information_as_list[2],
        'price_including_tax': book_information_as_list[3],
        'price_excluding_tax': book_information_as_list[4],
        'number_available': book_information_as_list[5],
        'product_description': book_information_as_list[6],
        'category': book_information_as_list[7],
        'review_rating': book_information_as_list[8],
        'full_image_url': book_information_as_list[9],
    }

    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('{}/{}.csv'.format(directory, category_name), 'a', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(rows)


"""
the purpose of the def book_extract_information function is to extract book information from the html content of
web pages. This function also create a directory that organize the structure of our folders and files. In this
structure, we want to have a folder named books that will store one folder per category
(with their corresponding categories as name). Inside the category folder we have a csv file which contain all
book information of the corresponding category. Inside the category folder, we have also an other folder named
images that contain the image file of every book of the corresponding category.
"""


def book_extract_information(url):
    time.sleep(3)

    page = requests.get(url)  # I am downloading a web page using requests
    soup = BeautifulSoup(page.content,
                         'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document

    product_page_url = url
    universal_product_code = soup.find_all('tr')[0].get_text()
    title = soup.find('h1').get_text()
    price_including_tax = soup.find_all('tr')[3].get_text()
    price_excluding_tax = soup.find_all('tr')[2].get_text()
    number_available = soup.find_all('tr')[5].get_text()
    product_description = soup.find_all('p')[3].get_text()
    category = soup.find_all('a')[3].get_text()
    review_rating = soup.find_all('tr')[6].get_text()
    img = soup.find_all('img')[0]
    part_image_url = img['src'].replace("../..", "")
    print("URL ========> {}".format(part_image_url))
    full_image_url = "https://books.toscrape.com" + part_image_url
    directory = 'books/{}/images'.format(category)

    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(full_image_url)
    file = open("{}/{}.jpg".format(directory, title.replace('/', '_')), "wb")
    file.write(response.content)
    file.close()
    book_information_as_list = [product_page_url, universal_product_code, title, price_including_tax,
                                price_excluding_tax, number_available, product_description,
                                category, review_rating, full_image_url]
    return book_information_as_list


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


book_extract_information(url)
