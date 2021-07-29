## Table of contents 
1. General info 
2. Libraries 
3. Book_detailed_scraper 
4. get_books_for_category 
5. categories_scraper 
6. get_next_page
### 1. General info 
*** 
The goal of the application is to extract book information(sorted by category) 
and to store it to a csv file(one csv file per category). The goal is also to
download the image file of each book. The application run very well on linux
and macOS. On Windows, the application can face some encoding issues. 
Consequently, the application can miss some data.
*** 
### 2. Libraries 
*** 
In order to write and run properly the application, I installed 2 libraries. 
I installed BeautifulSoup 4.9.3 and requests 2.25.1. 
***
### 3. Book_detailed_scraper 
***
The purpose of this file is to extract book information data and store it 
into a csv file. The purpose is also to create a directory that store 
image files into a folder.
*** 
### 4. get_books_for_category 
*** 
The purpose of this file is to apply the function of Book_detailed_scraper to 
a whole category. In other words, one csv file per category with their 
corresponding book data, and an image file for each book.
*** 
### 5. categories_scraper 
*** 
The purpose of this file is to apply the function of get_books_for_category 
to every category. However, this python file return only the data of the first 
page of every category.
*** 
### 6. get_next_page 
***
To get the data of books from other pages(categories with more than one page), 
I built a function get_next_page that go to the next page. In order to get 
data from other pages, I called the get_books_for_category function inside 
the get_next_page function. However, this python file return only the data of 
categories with more than one page(except for Travel category and poetry).
***
