import requests
from bs4 import BeautifulSoup


page = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
soup = BeautifulSoup(page.content, 'html.parser')
image = str(soup.find('img'))
expected_result = 'https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg'
image_link = image.replace('<img alt="A Light in the Attic" src="../..', '')
final_link = 'https://books.toscrape.com' + image_link
print(final_link)


def get_image_file_book():
    return final_link
