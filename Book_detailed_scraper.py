import os
import time
import requests
from bs4 import BeautifulSoup


def store_book_information(book_information_as_list):
    converted_list = [str(element) for element in book_information_as_list]
    category_name = book_information_as_list[8]  # Category is index 8 in book_information_as_list
    book_information_as_string = "|".join(converted_list).replace("\n", "")
    print(book_information_as_string)
    directory = 'books/{}'.format(category_name)

    if not os.path.exists(directory):
        os.makedirs(directory)
    with open('{}/{}.csv'.format(directory, category_name), 'a', encoding='utf-8') as file:
        file.write("\n")
        file.write(f'{book_information_as_string}\n')


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
    product_description_head = soup.find_all('h2')[0].get_text()
    product_description = soup.find_all('p')[3].get_text()
    category = soup.find_all('a')[3].get_text()
    review_rating = soup.find_all('tr')[6].get_text()
    image_url = soup.find_all('img')[0]
    image_link1 = str(image_url).replace('<img alt="{}" src="../..'.format(title.replace('&', '&amp;').replace('"', '&quot;')), '')
    image_link2 = str(image_link1).replace('"/>', '')
    image_url = "https://books.toscrape.com" + image_link2
    directory = 'books/{}/images'.format(category)

    if not os.path.exists(directory):
        os.makedirs(directory)
    response = requests.get(image_url)
    file = open("{}/{}.jpg".format(directory, title.replace('/', '_')), "wb")
    file.write(response.content)
    file.close()
    book_information_as_list = [product_page_url, universal_product_code, title, price_including_tax,
                                price_excluding_tax, number_available, product_description_head, product_description,
                                category, review_rating, image_url]
    return book_information_as_list


url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'


book_extract_information(url)
