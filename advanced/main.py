from product_factory import ProductScraperFactory

if __name__ == '__main__':
    jumia_url = 'https://www.jumia.com.gh/mobile-phones/?page=1'
    jumia_scraper = ProductScraperFactory.create_scraper('jumia', jumia_url)
    jumia_scraper.scrape()

    # jiji_url = 'https://jiji.com.gh/mobile-phones'
    # jiji_scraper = ProductScraperFactory.create_scraper('jiji', jiji_url)
    # jiji_scraper.scrape()