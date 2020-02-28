from selenium import webdriver
from random import shuffle
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='./geckodriver.exe',
                           firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe')


sites = open("randomsite.txt", "r").readlines()

shuffle(sites)

open("tempsites.txt", 'w+').writelines(sites)

driver.get(sites[0])
for i in range(1, len(sites), 1):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i])
    driver.get(sites[i])

for i in range(len(sites) - 1, -1, -1):
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(1)
    driver.close()
