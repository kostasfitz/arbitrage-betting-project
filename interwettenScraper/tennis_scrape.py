from datetime import datetime
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json


def tennis_scrape(driver_path, website):
    driver = webdriver.Chrome(driver_path)
    driver.get(website)

    # close popups
    t.sleep(2)
    cookies_button = driver.find_element(by=By.XPATH, value="//button[@class='tru_iw__btn']")
    cookies_button.click()

    # create dataframe
    dataframe = pd.DataFrame({'Date': [],
                              'Home': [],
                              'Away': [],
                              'HomeOdds': [],
                              'AwayOdds': []})

    # find available games
    t.sleep(1)
    # table = driver.find_element(by=By.XPATH, value="//table[@id='TBL_Content_TabbedKindOfSportList']")
    rows = driver.find_elements(by=By.XPATH, value="//td[@class='bets']")

    for row in rows:
        info = row.get_attribute('innerText')
        info.strip()
        home, home_odds, *_, away, away_odds = info.split('\n')
        date = 'N/A'  # will be fixed in later version
        home_lastname, *_ = home.split(' ')
        away_lastname, *_ = away.split(' ')
        data = [date, home_lastname, away_lastname, home_odds, away_odds]
        dataframe.loc[len(dataframe)] = data

    # export data as csv
    now = datetime.now()
    datetime_str = now.strftime("%d%m%Y%H%M%S")
    dataframe.to_csv(datetime_str + '.csv')

    driver.close()
