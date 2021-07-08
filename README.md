## Table of contents 
1. General info 
2. Libraries 
3. Book_detailed_scraper 
4. get_books_for_category 
5. categories_scraper 
6. get_next_page 
7. get_image_file_book 
### 1. General info 
*** 
The goal of the application is to extract book information(sorted by category) 
and to store it to a csv file(one csv file per category). 
*** 
### 2. Libraries 
*** 
In order to write and run properly the application, I installed 2 libraries. 
I installed BeautifulSoup and requests. I also installed pandas but finally,
I didn't use this library. The initial purpose of pandas was to write csv 
files but finally, I used the package csv(automatically installed in python).
***
### 3. Book_detailed_scraper 
***
The purpose of this file is to extract book information data and store it 
into a csv file. 
*** 
### 4. get_books_for_category 
*** 
The purpose of this file is to apply the function of Book_detailed_scraper to 
a whole category. In other words, one csv file per category with their 
corresponding book data.
*** 
### 5. categories_scraper 
*** 
The purpose of this file is to apply the function of get_books_for_category 
to every category. 
*** 
### 6. get_next_page 
***
During the running of the application, I noticed an issue. Some categories 
have more than one page, and my application is scraping only the data of 
the first page of each category. To get the data of books from other 
pages(categories with more than one page), I built a function get_next_page 
that go to the next page. In order to get data from other pages, I called the 
get_books_for_category function inside the get_next_page function. 
*** 
### 7. get_image_file_book 
*** 
The purpose of the project was also to get image file of every book. 
So, I built a function that return the image file of all books from 
every category. 
***