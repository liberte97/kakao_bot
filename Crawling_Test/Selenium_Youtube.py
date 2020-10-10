from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(1)

search = driver.find_element_by_name('search_query')

search.send_keys('공부 잘되는 음악')
time.sleep(1)

search.send_keys(Keys.ENTER)

# //*[@id="search"]