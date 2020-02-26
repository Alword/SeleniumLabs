# Импортируем необходимые библиотеки
from selenium import webdriver
from random import shuffle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
# Зададим драйвер нашего браузера


def open_tab(link):
    driver.execute_script(
        'window.open("{0}","_blank");'.format(link.replace('\n', '')))


opts = Options()
opts.set_preference("browser.link.open_newwindow.restriction", 0)
opts.set_preference("browser.link.open_newwindow", 3)

driver = webdriver.Firefox(firefox_options=opts,
                           executable_path='./geckodriver.exe',
                           firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe')

# Метод driver.get(url) перенаправляет к странице с адресом url.
# WebDriver будет ждать пока страница не загрузится полностью,
# прежде чем передать контроль вашему тесту или скрипту.

openstream = open("randomsite.txt", encoding="UTF-8-sig")
sites = openstream.readlines()

shuffle(sites)

for link in sites:
    open_tab(link)

open("tempsites.txt", 'w+', encoding="UTF-8-sig",).writelines(sites)

driver.close()
