from jiji_scrapper import JijiScraper
from jumia_scrapper import JumiaScraper

class ProductScraperFactory:
    @staticmethod
    def create_scraper(scraper_type, url):
        if scraper_type == 'jumia':
            return JumiaScraper(url)
        elif scraper_type == 'jiji':
            return JijiScraper(url)
        else:
            raise ValueError(f"Invalid scraper type: {scraper_type}")
