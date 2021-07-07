import requests
from bs4 import BeautifulSoup


page = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
soup = BeautifulSoup(page.content, 'html.parser')
image = str(soup.find('img'))
image_link = image.replace('<img alt="A Light in the Attic" src="../..', '')
final_link = 'https://books.toscrape.com' + image_link
print(final_link)


def get_image_file_book():
    main_page = 'https://books.toscrape.com/index.html'
    response = requests.get(main_page)
    if response.ok:
        soup1 = BeautifulSoup(response.text, 'html.parser')
        for web in soup1.find('ul', class_='nav nav-list').find('li').find('ul').find_all('li'):
            href = web.a.get('href')
            url = "http://books.toscrape.com/{}".format(href)
            page1 = requests.get(url)
            if page1.ok:
                soup2 = BeautifulSoup(page1.text, 'html.parser')
                link = soup2.find_all('h3')
                for h3 in link:
                    a = h3.find('a')
                    href = a.get('href')
                    links = 'https://books.toscrape.com/catalogue' + href
                    book_link = str(links).replace("../../..", "")
                    book = requests.get(book_link)
                    if book.ok:
                        soup3 = BeautifulSoup(book.text, 'html.parser')
                        image1 = str(soup3.find('img'))
                        alt = soup3.find('img').get('alt')
                        image_link1 = image1.replace('<img alt="{}" src="../..'.format(alt), '')
                        final_link1 = 'https://books.toscrape.com' + image_link1
                        print(final_link1)


get_image_file_book()
