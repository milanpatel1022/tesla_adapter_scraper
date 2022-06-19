# Scraper for Tesla Adapters

My sibling needs an adapter for their incoming Tesla, but the one they need is out of stock.

Tesla has a feature to email users when the adapter they want comes back in stock.
However, many people have found out and complained that the adapter they wanted was in stock on the website, but they never received any emails.

So, I decided to quickly develop this scraper that uses both Selenium and BeautifulSoup. It sends a desktop notification to me as soon as the adapter is in stock.

It is also important to note that my scraper does honor the crawling-delay requested by Tesla (via their robots.txt).

