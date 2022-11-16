# interwetten scraper


from tennis_scrape import tennis_scrape


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
# insert link of daily tennis coupon
website = 'https://www.interwetten.gr/en/sportsbook/l/412890/wta-buenos-aires'

tennis_scrape(driver_path, website)
