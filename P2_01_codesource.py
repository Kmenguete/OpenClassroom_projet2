import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://books.toscrape.com/catalogue/soumission_998/index.html")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content,
                     'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
url = "http://books.toscrape.com/catalogue/soumission_998/index.html"
print(url)
print(soup.find('h1').get_text())
print(soup.find_all('h2')[0].get_text())
print(soup.find_all('p')[3].get_text())
print(soup.find_all('tr')[0].get_text())
print(soup.find_all('tr')[2].get_text())
print(soup.find_all('tr')[3].get_text())
print(soup.find_all('tr')[5].get_text())
print(soup.find_all('a')[3].get_text())
print(soup.find_all('tr')[6].get_text())
print(soup.find_all('img')[0])
import csv
with open('P2_01_codesource.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["product_page_url", "http://books.toscrape.com/catalogue/soumission_998/index.html"])
    writer.writerow(["universal_product_code(upc)", "UPC6957f44c3847a760"])
    writer.writerow(["title", "Soumission"])
    writer.writerow(["price_including_tax", "Price (incl. tax)£50.10"])
    writer.writerow(["price_excluding_tax ", "Price (excl. tax)£50.10"])
    writer.writerow(["number_available", "Availability In stock (20 available)"])
    writer.writerow(["category", "Fiction"])
    writer.writerow(["review_rating ", "Number of reviews 0"])
    writer.writerow(["image_url", "img alt=Soumission src=../../media/cache/ee/cf/eecfe998905e455df12064dba399c075.jpg"])

f = open("product_description.txt", "w")
f.write("Dans une France assez proche de la nôtre, un homme s’engage dans la carrière universitaire. Peu motivé par l’enseignement, il s’attend à une vie ennuyeuse mais calme, protégée des grands drames historiques. Cependant les forces en jeu dans le pays ont fissuré le système politique jusqu’à provoquer son effondrement. Cette implosion sans soubresauts, sans vraie révolution, s Dans une France assez proche de la nôtre, un homme s’engage dans la carrière universitaire. Peu motivé par l’enseignement, il s’attend à une vie ennuyeuse mais calme, protégée des grands drames historiques. Cependant les forces en jeu dans le pays ont fissuré le système politique jusqu’à provoquer son effondrement. Cette implosion sans soubresauts, sans vraie révolution, se développe comme un mauvais rêve.Le talent de l’auteur, sa force visionnaire nous entraînent sur un terrain ambigu et glissant ; son regard sur notre civilisation vieillissante fait coexister dans ce roman les intuitions poétiques, les effets comiques, une mélancolie fataliste.Ce livre est une saisissante fable politique et morale. ...more")
f.close()
