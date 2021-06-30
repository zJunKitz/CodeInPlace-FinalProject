from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/p/pl?d=graphic+card&cm_sp=KeywordRelated-_-graphics%20card-_-graphic%20card-_-INFOCARD'

# opening up a connection, grabbing the page before closing the connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# grab each product
cells = page_soup.findAll("div", {"class": "item-cell"})

filename = "products.csv"

# loop through every product for their name, price and shipping fee before
# writing them into a csv file
with open(filename, "w") as f:
    headers = "product_name, brand, shipping_price\n"
    f.write(headers)

    for cell in cells:
        title_container = cell.findAll("a", {"class": "item-title"})

        try:
            product_name = title_container[0].text.strip()
        except IndexError:
            product_name = "N/A"

        try:
            brand = cell.div.div.a.img["title"]
        except TypeError:
            brand = "N/A"
        except AttributeError:
            brand = "N/A"

        shipping_container = cell.findAll("li", {"class": "price-ship"})
        try:
            shipping_price = shipping_container[0].text.strip()
        except IndexError:
            shipping_price = "N/A"

        f.write(product_name.replace(",", "|") + ", " + brand + ", " + shipping_price + ", " + "\n")
