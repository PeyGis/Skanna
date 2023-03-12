from abc import ABC, abstractmethod

from product import Product
from typing import List


class ProductScraper:
    def __init__(self, url):
        self.url = url
    
    # @abstractmethod
    # def extract_title(self, product):
    #     pass
    
    # @abstractmethod
    # def extract_brand(self, product):
    #     pass
    
    # @abstractmethod
    # def extract_price(self, product):
    #     pass
    
    # @abstractmethod
    # def extract_rating(self, product):
    #     pass

    
    def scrape(self) -> List[Product]:
        raise NotImplementedError