import requests
from bs4 import BeautifulSoup
import time

page = requests.get(
    "http://books.toscrape.com/catalogue/category/books/science_22/index.html")  # I am downloading a web page using requests
soup = BeautifulSoup(page.content, 'html.parser')  # I am creating an instance of the BeautifulSoup class to parse the document
link = soup.find_all('h3')
links = []
for h3 in link:
    a = h3.find('a')
    web = a['href']
    links.append('http://books.toscrape.com/catalogue/science_22/index.html' + web)

    # links correspond � l'ensemble des liens de ma cat�gorie Science dont je souhaite extraire les donn�es des livres.
    # Les deux paragraphes de codes ci-dessous correspondent � deux tentatives d'extractions des donn�es des livres de la cat�gorie science.
    # Le probl�me du premier paragraphe de code c'est qu'il me retourne que les donn�es d'un seul livre.
    # Avec le deuxi�me paragraphe de code je tente de rem�dier aux probl�mes du premier paragraphe mais sans succ�s.
    # Le deuxi�me paragraphe de code me retourne les 14 liens de mes livres mais avec les donn�es du livre du premier paragraphe qui se r�p�te 14 fois.
    # Quand j'essaie d'appliquer une incr�mentation et string format mon code reste en cours d'�x�cution pour une dur�e ind�termin� (La fen�tre de r�sultat reste vide)
    # Pour conclure, aujourd'hui je sais aller chercher les donn�es qui m'int�resse dans une page web mais je ne sais pas encore naviguer d'une page web � l'autre.
    # Voici le lien de la vid�o dont je m'inspire pour mon code:https://www.youtube.com/watch?v=KdLkwBNtGsY , cette vid�o m'a �t� d'une tr�s grande utilit�.

# 1er paragraphe de code:  
with open('urls.txt', 'r') as file:
    for row in file:
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
        print(product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax,
              number_available,
              product_description_head + '\n' + product_description, category, review_rating, image_url)
        time.sleep(3)

# 2�me paragraphe de code:
    with open('urls.txt', 'r') as file:
        for links in file:
            response = requests.get(links)
            if response.ok:
                soup = BeautifulSoup(links)
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
            print(links, universal_product_code, title, price_including_tax, price_excluding_tax, number_available,
                  product_description_head + '\n' + product_description, category, review_rating, image_url)
