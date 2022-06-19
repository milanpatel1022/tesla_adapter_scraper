from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from plyer import notification

#options for our scraper to bypass warnings, to render elements correctly, etc.
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1200')
options.add_argument('--no-sandbox')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--log-level=3')
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')


'''
Why use Selenium AND BeautifulSoup?
    - BeautifulSoup is not useful for fetching dynamic content, while Selenium is
    - Use Selenium to get rendered HTML from browser & then parse that using BeautifulSoup via the page_source property webdriver provides
'''

#set up our browser instance
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#URL that we need to scrape
URL = "https://shop.tesla.com/product/gen-2-nema-adapters"



while True:
    
    #go to page
    driver.get(URL)

    #honor Tesla's crawl-delay request (found in their robots.txt)
    sleep(10)

    soup = BeautifulSoup(driver.page_source, "lxml")

    #string containing adapters and if they are in stock
    adapter_info = soup.find('section', class_='product__container')['data-productpurchasablemapjson']

    #converted string into comma separated list of adapters & stock info
    adapters = adapter_info.split(',')

    #the adapter we are interested in
    our_adapter = adapters[1]

    #desktop notify when adapter is in stock
    if our_adapter.split(':')[1] == "true":
        notification.notify(
            title = our_adapter,
            message = "adapter in stock",
            app_icon = None,
            timeout = 50,
        )

        break

driver.close()