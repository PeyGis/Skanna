import time
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from base_scrapper import ProductScraper
from product import Product



class JijiScraper(ProductScraper):
    def __init__(self, url):
        super().__init__(url)
        print(self.url)
        self.base_url = 'https://www.jiji.com.gh'
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome()

    def get_product_urls(self):
        self.driver.get(self.url)
        time.sleep(5)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        products = soup.find_all('div', {'class': 'b-list-advert__gallery__item js-advert-list-item'})
        urls = []
        for product in products:
            url = self.base_url + product.find("a")["href"]
            urls.append(url)
        return urls

    def scrape(self) -> List[Product]:
        urls = self.get_product_urls()
        print(urls)
        products = []
        for url in urls:
            self.driver.get(url)
            time.sleep(5)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            try:
                title = soup.find('div', {'class': 'b-advert-title-inner qa-advert-title b-advert-title-inner--h1'}).text.strip()
                price = float(soup.find("span", {"class": "qa-advert-price-view-title b-alt-advert-price__text"}).text.replace(",", "").replace("GH₵", ""))
                print(f"Title: {title}, Price: {price}")
                products.append(Product(url, title, price, "Jiji"))
            except:
                pass
        return products


    def __del__(self):
        self.driver.quit()
