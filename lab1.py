# Импортируем необходимые библиотеки
from selenium import webdriver
from random import shuffle

# Зададим драйвер нашего браузера

def close_tab(windows):
    driver = windows[:-1]
    driver.quit()
    windows.remove(driver)


def open_tab(link, windows):
    if 'http' in link:
        driver = webdriver.Firefox(executable_path='./geckodriver.exe',
                                   firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe')
        driver.get(link.replace('\n', ''))
        windows.append(driver)

# Метод driver.get(url) перенаправляет к странице с адресом url.
# WebDriver будет ждать пока страница не загрузится полностью,
# прежде чем передать контроль вашему тесту или скрипту.


openstream = open("randomsite.txt", encoding="UTF-8-sig")
sites = openstream.readlines()

shuffle(sites)

windows = []

for link in sites:
    open_tab(link, windows)

while len(windows) > 0:
    close_tab(windows)

open("tempsites.txt", 'w+', encoding="UTF-8-sig",).writelines(sites)
