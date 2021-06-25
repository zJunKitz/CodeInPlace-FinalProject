# importing the required libraries
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession

session = HTMLSession()
my_url = 'https://upjourney.com/best-self-help-books'

# Fetching the page and parsing it
response = session.get(my_url)
page_html = soup(response.html.html, "html.parser")

# Fetching all the div(s) which contains the information about the book
book_containers = page_html.findAll('div', {'class': 'wp-block-group'})

# Looping through each div, recording the name, price and audiobook availability into a csv file
with open("BestSelfHelpBooks.csv", "w") as f:
    headers = "Book Name, Price, Audio Book Availability\n"
    f.write(headers)

    for container in book_containers:
        book_name = container.div.h2.a.text

        price = (container.find("div", {'class': 'lasso-price-value'})).text

        if container.find('a', {'class': 'lasso-button-2 d-none'}):
            audio_book = "None"
        else:
            audio_book = "Available"
        f.write(book_name.replace(",", "|") + ", " + price + ", " + audio_book + "\n")

