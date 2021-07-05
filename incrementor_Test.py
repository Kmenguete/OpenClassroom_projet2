import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
page = requests.get(url)  # I am downloading a web page using requests
soup = BeautifulSoup(page.content, 'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document


#incrementor = 0

next_li = soup.find('li', class_='next')

print(url)

# if next_li is not None:
#     print(next_li)
# else:
#     print("next_li is not found")
#

incrementor = 2

while next_li is not None:
    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/page-{}.html".format(incrementor)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    next_li = soup.find('li', class_='next')
    print(url)
    incrementor += 1
