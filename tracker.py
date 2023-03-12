from typing import List
from product import Product
from factory import *

class Tracker:
    def __init__(self):
        self.products = []

    def add_products(self, new_products: List[Product]):
        self.products.extend(new_products)

    def print_products(self):
        for product in self.products:
            print(f"Title: {product.title}")
            print(f"Price: {product.price}")
            print(f"URL: {product.url}")
            print(f"Platform: {product.platform}")

            print()

if __name__ == "__main__":
    countries = ["gh"]
    platforms = ["Jumia","Jiji"]

    tracker = Tracker()

    for platform in platforms:
        scraper = ScraperFactory.create_scraper(platform)
        for country in countries:
            products = scraper.extract_products(country)
            tracker.add_products(products)

    tracker.print_products()

