from scrapper import *

class ScraperFactory:
    @staticmethod
    def create_scraper(platform: str) -> Scraper:
        if platform == "Jumia":
            return JumiaScraper()
        elif platform == "Jiji":
            return JijiScraper()