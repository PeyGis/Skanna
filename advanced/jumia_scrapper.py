import time
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from base_scrapper import ProductScraper
from product import Product
from utils import *




class JumiaScraper(ProductScraper):
    def __init__(self, url):
        super().__init__(url)
        print(self.url)
        self.base_url = 'https://www.jumia.com.gh'
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome()

    def get_product_urls(self):
        self.driver.get(self.url)
        time.sleep(5)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        products = soup.find_all('article', {'class': 'prd _fb col c-prd'})
        urls = []
        for product in products:
            url = self.base_url + product.find("a", {"class": "core"})["href"]
            urls.append(url)
        return urls

    def get_ratings(self, soup: BeautifulSoup) -> str:
        """A function to return the ratings for products"""
        rating_selector = soup.find('div', {'class': 'stars _s _al'})
        rating = 0
        if rating_selector != None:
            rating = get_numerical_value_from_string(rating_selector.text.strip())
        return rating

    def get_number_of_verified_ratings(self, soup: BeautifulSoup) -> float:
        """Returns the number of verified ratings for a product"""
        num_verified_rating = 0
        num_verified_ratings_selector = soup.find('p', {'class': '-fs16 -pts'})

        if num_verified_ratings_selector != None:
            num_verified_rating = get_numerical_value_from_string(num_verified_ratings_selector.text.strip())
        return num_verified_rating

    def get_product_description(self, soup: BeautifulSoup) -> str:
        """A function to return the product description"""
        description_selector = soup.find('div', {'class': 'markup -mhm -pvl -oxa -sc'})
        product_description = ""
        if description_selector != None:
            product_description = description_selector.text.strip()[0:150]
        return product_description
    
    def get_items_in_stock(self, soup: BeautifulSoup) -> str:
        """Returns the number of items in stock. Jumia has 2 ways of displaying this information. A regular stock in <p> and a flash sale stock in <span>
        """
        items_in_stock = ""
        ## First check if the product is standard
        standard_listing = soup.find('p', {'class': '-df -i-ctr -fs12 -pbs -rd5'})
        in_stock = soup.find('p', {'class': '-df -i-ctr -fs12 -pbs -gy5'})
        few_units_left = soup.find('p', {'class': '-df -i-ctr -fs12 -pbs -yl7'})

        if standard_listing != None:
            items_in_stock = standard_listing.text.strip()
        elif in_stock != None:
            items_in_stock = in_stock.text.strip()
        elif few_units_left != None:
            items_in_stock = few_units_left.text.strip()
        else:
            items_in_stock = soup.find('span', {'class': '-fsh0 -prs -fs12'}).text.strip()
        return items_in_stock

    def get_product_brand(self, soup: BeautifulSoup) -> str:
        """A function to return the brand of a product"""
        brand_selector = soup.find_all('div', {'class': '-pvxs'})[1]
        brand_name = None
        if brand_selector != None:
            brand_name = brand_selector.find("a", {'class': "_more"}).text.strip()
        return brand_name

    def scrape(self) -> List[Product]:
        urls = self.get_product_urls()
        print(urls)
        products = []
        for url in urls:
            self.driver.get(url)
            time.sleep(5)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            try:
                title = soup.find('h1', {'class': '-fs20 -pts -pbxs'}).text.strip()
                price = float(soup.find("span", {"class": "-b -ltr -tal -fs24"}).text.replace(",", "").replace("GH₵", ""))
                image_url = soup.find('div', {'id': 'imgs'}).find('a')["href"]
                stock_quantity = self.get_items_in_stock(soup=soup)
                description = self.get_product_description(soup=soup)
                rating = self.get_ratings(soup=soup)
                num_verified_rating = self.get_number_of_verified_ratings(soup=soup)
                brand = self.get_product_brand(soup=soup)
                print(f"Title: {title}, Price: {price}, Stock: {stock_quantity}, Image URL: {image_url} Ratings: {rating} Num_Verified: {num_verified_rating} Brand: {brand}")
                products.append(Product(url, title, price, "Jumia"))
            except:
                pass
        return products


    def __del__(self):
        self.driver.quit()
