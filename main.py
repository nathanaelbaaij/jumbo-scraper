import requests
import bs4

# scrapping url https://www.jumbo.com/producten?PageNumber=1&SortingAttribute=ALPHABETICAL_ASCENDING
# where PageNumber=1 is counting up
# 2018 is max page number
# 2018 * 9 = 18.162 producten


class Jumbo:
    def __init__(self):
        self.products = []

    def addProduct(self, title):
        self.products.append(title)


jumboUrl = "https://www.jumbo.com/producten?SortingAttribute=ALPHABETICAL_ASCENDING"
request = requests.get(jumboUrl)


soup = bs4.BeautifulSoup(request.text, 'lxml')


# get product title
products = soup.find_all("div", class_="jum-results-grid-wrapper")

for product in products:
    print(product.select('.jum-item-titlewrap > h3 > a'))

# get product price
# .jum-item-price > .jum-sale-price > input[jum-data-price]


# jumbo = Jumbo()

# for i in range(len(products)):
#     jumbo.addProduct(products[i].get_text())

# for product in jumbo.products:
#     print(product)
