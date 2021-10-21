from selenium import webdriver
import pandas as pd
import time

# scrape data from NBA website to csv file


# function to save dataframe, will be used later
def save_df():
    # find the table element
    elem = driver.find_element_by_css_selector(".nba-stat-table__overflow")
    # convert element to html
    elem_html = elem.get_attribute('innerHTML')
    # read the html with pandas which returns array of all tables (only 1 table in our case)
    df = pd.read_html(elem_html)
    # save the first element of array which is our table
    df[0].to_csv(f"data{i}.csv")


# initializes chrome
driver = webdriver.Chrome('chromedriver')
# opens the webpage
driver.get("https://www.nba.com/stats/players/bio/?Season=2019-20&SeasonType=Regular%20Season&fbclid=IwAR1HOmAMuXkkiOiB4B1wDi9y5eVsWFmfyTMugrF1yXL7NmaB_oRYBWks8Q0")
# wait for page to load
time.sleep(1)
# finds the cookie accept button
consent = driver.find_element_by_css_selector("#onetrust-accept-btn-handler")
# clicks on cookie accept button
consent.click()
# sleeps to wait for page reload
time.sleep(3)
# clicks represent amount of clicks to go over all table pages
clicks = 11
for i in range(clicks):
    if (i == 0):
        save_df()
        # continue to i=1
        continue

    # find a button to go to next page
    nextClick = driver.find_element_by_class_name(
        "stats-table-pagination__next")
    # click to next page
    nextClick.click()
    # wait for page to load
    time.sleep(1)
    # save table
    save_df()
