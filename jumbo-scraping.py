import requests
import bs4
import csv
import os.path

filename = 'jumbo-products.csv'
pageNumber = 0
emptyPage = 0
productCount = 0

# prints out status


def printStatus(pageNumber, emptyPage):
    print("=========================================")
    print("Current pagenumber: {}".format(pageNumber))
    print("Empty pages found: {}".format(emptyPage))
    print("Product count: {}".format(productCount))
    print("=========================================")
    return

# gets product info and saves it to an csv file


def saveProductToCSV(sku, title, link, price, image):

    productArray = {}

    productArray['sku'] = str(sku)
    productArray['title'] = str(title)
    productArray['link'] = str(link)
    productArray['price'] = price
    productArray['image'] = str(image)

    file_exists = os.path.isfile(filename)

    with open(filename, 'a') as csv_file:

        fieldnames = ['sku', 'title', 'link', 'price', 'image']

        csv_writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, delimiter=',')

        if not file_exists:
            csv_writer.writeheader()  # file doesn't exist yet, write a header

        csv_writer.writerow(productArray)

    return


# while True
while pageNumber < 2:

    jumboUrl = "https://www.jumbo.com/producten?PageNumber={}&SortingAttribute=ALPHABETICAL_ASCENDING".format(
        pageNumber)

    request = requests.get(jumboUrl)

    if(request.status_code == 200):

        # init soup
        soup = bs4.BeautifulSoup(request.text, 'lxml')

        # get ul with all the products inside with it
        pageProducts = soup.find_all("li", class_="jum-result")

        if not pageProducts:
            pageNumber += 1
            emptyPage += 1
            if(emptyPage > 5):
                print("Done!")
                break
        else:
            # scrape products with soup
            for product in pageProducts:

                productSKU = product.select_one(
                    '.jum-item-product').get('data-jum-product-sku')

                productTitle = product.select_one(
                    '.jum-item-titlewrap > h3 > a').get_text()

                productLink = product.select_one(
                    '.jum-item-titlewrap > h3 > a').get('href')

                productPrice = product.select_one(
                    ".jum-item-price input[jum-data-price]").get('jum-data-price')

                productImage = product.select_one(
                    '.jum-item-figure img').get('data-jum-hr-src')

                # save productdetails to csv
                saveProductToCSV(
                    productSKU,
                    productTitle,
                    productLink,
                    productPrice,
                    productImage
                )

                productCount += 1

            # go to next page
            pageNumber += 1

    else:
        print("Error: page with pageNumber {} not found!".format(pageNumber))

    # print status
    printStatus(pageNumber, emptyPage)
