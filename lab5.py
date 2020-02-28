from selenium import webdriver
from random import shuffle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox(executable_path='./geckodriver.exe',
                           firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe')

driver.get("https://vk.com/")

email = driver.find_element_by_xpath("//*[@id=\"index_email\"]")
password = driver.find_element_by_xpath("//*[@id=\"index_pass\"]")

loginButton = driver.find_element_by_xpath("//*[@id=\"index_login_button\"]")

resource = open("./loginpass.secret").readlines()

email.send_keys(resource[0])
password.send_keys(resource[1])
loginButton.click()

element = WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div[2]/div[1]/div/nav/ol/li[3]/a/span/span[3]"))
    )

element.click()

element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "nim-dialog--preview")))

messageElements = list(filter(lambda x: x.text != '', driver.find_elements_by_class_name("_dialog_body")))[:10]

messages = [msgElem.text+"\n" for msgElem in messageElements]

open("./messages.txt","w+",encoding="UTF-8-sig").writelines(messages)

driver.close()
driver.quit()
