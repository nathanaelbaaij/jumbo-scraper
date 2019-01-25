from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from pyvirtualdisplay import Display


def correct_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url


def scrollDown(browser, numberOfScrollDowns):
    body = browser.find_element_by_tag_name("body")
    while numberOfScrollDowns >= 0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
        time.sleep(0.3)
    return browser


def crawl_url(url, run_headless=False):
    # if run_headless:
    #     display = Display(visible=0, size=(1024, 768))
    #     display.start()

    # url = correct_url(url)
    browser = webdriver.Chrome()
    browser.get(url)

    time.sleep(2)

    browser = scrollDown(browser, 30)

    products = browser.find_elements_by_class_name("jum-result")

    for product in products:
        # a_element = hover_element.find_element_by_tag_name("a")
        # product_title = a_element.get_attribute("title")
        # product_link = a_element.get_attribute("href")

        title = product.find_elements_by_class_name("jum-item-titlewrap")
        title = title[0].find_element_by_tag_name("a")
        title = title.text

        # price =

        print(title)

    browser.quit()


if __name__ == '__main__':
    url = "https://www.jumbo.com/producten?SortingAttribute=ALPHABETICAL_ASCENDING"
    crawl_url(url)
