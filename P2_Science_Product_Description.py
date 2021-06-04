import requests
from bs4 import BeautifulSoup
import time

page = requests.get(
    "http://books.toscrape.com/catalogue/category/books/science_22/index.html")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content,
                     'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
link = soup.find_all('h3')
links = []
for h3 in link:
    a = h3.find('a')
    web = a['href']
    links.append('http://books.toscrape.com/catalogue/science_22/index.html' + web)

with open('urls.txt', 'r') as inf:
    with open('P2_Science_Product_Description.text', 'w') as f:
        f.write('product_page_url \n')
        f.write('title \n')
        f.write('product_description_head \n')
        f.write('product_description \n')
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_page_url = url
                title = soup.find('h1').get_text()
                product_description_head = soup.find_all('h2')[0].get_text()
                product_description = soup.find_all('p')[3].get_text()
                print(product_page_url)
                print(title)
                print(product_description_head)
                try:
                    print(product_description)
                except:
                    print("********** Error, cannot display description **********")
                f.write(product_page_url)
                f.write(title)
                f.write(product_description_head)
                f.write(str(product_description.encode('utf8')))
            time.sleep(3)
