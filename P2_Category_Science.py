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
    with open('P2_Category_Science.csv', 'w') as outf:
        outf.write('product_page_url \n')
        outf.write('universal_product_code \n')
        outf.write('title \n')
        outf.write('price_including_tax \n')
        outf.write('price_excluding_tax \n')
        outf.write('number_available \n')
        outf.write('category \n')
        outf.write('review_rating \n')
        outf.write('image_url \n')
        for row in inf:
            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
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
                print(product_page_url)
                print(universal_product_code)
                print(title)
                print(price_including_tax)
                print(price_excluding_tax)
                print(number_available)
                print(product_description_head)
                try:
                    print(product_description)
                except:
                    print("********** Error, cannot display description **********")
                print(category)
                print(review_rating)
                print(image_url)
                outf.write(str(product_page_url))
                outf.write(str(universal_product_code))
                outf.write(str(title))
                outf.write(str(price_including_tax))
                outf.write(str(price_excluding_tax))
                outf.write(str(number_available))
                outf.write(str(category))
                outf.write(str(review_rating))
                outf.write(str(image_url))
            time.sleep(3)
