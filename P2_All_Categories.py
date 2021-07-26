import requests
from bs4 import BeautifulSoup
import time

page = requests.get("https://books.toscrape.com/")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content,
                     'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document

for web in soup.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
    href = web.a.get('href')
    url = "https://books.toscrape.com/{}".format(href)
    time.sleep(5)
    response = requests.get(url)
    if response.ok:
        time.sleep(5)
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find_all('h3')
        for h3 in link:
            links = []
            a = h3.find('a')
            Bouddha = a['href']
            links.append('https://books.toscrape.com/catalogue' + Bouddha)
            Herman = str(links).replace("../../..", "")
            print(Herman)
            print(Herman.strip())
            response = requests.get(Herman)
            if response.ok:
                time.sleep(5)
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
                time.sleep(5)
                next_li = soup.find('li', class_='next')
                incrementor = 2
            # time.sleep(5)
                while next_li is not None:
                    url = "https://books.toscrape.com/{}".format(href)
                    Delta = url.replace("index.html", "page-1.html")
                    time.sleep(5)
                    page = requests.get(Delta)
                    time.sleep(5)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    next_li = soup.find('li', class_='next')
                    incrementor += 1
                    time.sleep(5)
                    response = requests.get(Delta.format(incrementor))
                    if response.ok:
                        time.sleep(5)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        for h3 in link:
                            links = []
                            a = h3.find('a')
                            Bouddha = a['href']
                            links.append('https://books.toscrape.com/catalogue' + Bouddha)
                            Vladimir = str(links).replace("../../..", "")
                            for Vladimir in web:
                                url = "https://" + Vladimir.strip()
                                time.sleep(5)
                                response = requests.get(url)
                                if response.ok:
                                    time.sleep(5)
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
                                    time.sleep(5)
                else:
                    print("Sorry, there is no longer pages")
