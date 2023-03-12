from abc import ABC, abstractmethod
from typing import List
import requests
from bs4 import BeautifulSoup
from product import Product

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class Scraper(ABC):
    @abstractmethod
    def extract_products(self, country: str) -> List[Product]:
        pass

class JumiaScraper(Scraper):
    base_url = "https://www.jumia.com.{}/mobile-phones/?page=1"
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def extract_products(self, country: str) -> List[Product]:
        url = self.base_url.format(country)

        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = []
        for product in soup.find_all('article', {'class': 'prd _fb col c-prd'}):
            try:
                url = product.find("a", {"class": "core"})["href"]
                title = product.find('h3', {'class': 'name'}).text.strip()
                price = float(product.find("div", {"class": "prc"}).text.replace(",", "").replace("GH₵", ""))
                products.append(Product(url, title, price, "Jumia"))
            except:
                pass

        return products

class JijiScraper(Scraper):
    base_url = "https://jiji.com.{}//mobile-phones"
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def extract_products(self, country: str) -> List[Product]:
        url = self.base_url.format(country)
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = []

        for product in soup.find_all("div", {"class": "b-list-advert__gallery__item js-advert-list-item"}):
            try:
                ##print(product)
                url = product.find("a")["href"]
                title = product.find("div", {"class": "qa-advert-title"}).text.strip()
                price = float(product.find("div", {"class": "qa-advert-price"}).text.replace(",", "").replace("GH₵", ""))
                products.append(Product(url, title, price, "Jiji"))
            except:
                pass

        return products
