from datetime import datetime
import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


def tennis_scrape(driver_path, website):
    driver = webdriver.Chrome(driver_path)
    driver.get(website)

    # close popups
    t.sleep(2)
    cookies_button = driver.find_element(by=By.ID, value='onetrust-accept-btn-handler')
    cookies_button.click()
    popup_button = driver.find_element(by=By.XPATH,
                                       value="//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
    popup_button.click()

    # find available matches
    t.sleep(1)
    table = driver.find_element(by=By.XPATH, value="//table[@class='events-list__grid']")
    rows = table.find_elements(by=By.XPATH, value="//tr[@class='events-list__grid__event']")

    dataframe = pd.DataFrame({'Date': [],
                              'Home': [],
                              'Away': [],
                              'HomeOdds': [],
                              'AwayOdds': []})

    for row in rows[:]:
        event = row.get_attribute('innerText')
        date, time, home, away, dummy1, home_odds, away_odds, *_ = event.split('\n')
        _, home_last, *_ = home.split(' ')
        *_, away_last = away.split(' ')
        data = [date + ' ' + time, home_last, away_last, home_odds, away_odds]
        dataframe.loc[len(dataframe)] = data

    # export data as csv
    now = datetime.now()
    datetime_str = now.strftime("%d%m%Y%H%M%S")

    dataframe.to_csv(datetime_str + '.csv')

    driver.close()