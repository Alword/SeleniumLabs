# Импортируем необходимые библиотеки
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Зададим драйвер нашего браузера
driver = webdriver.Firefox(
    executable_path='./geckodriver.exe', 
    firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe'
)
# Метод driver.get(url) перенаправляет к странице с адресом url.
# WebDriver будет ждать пока страница не загрузится полностью,
# прежде чем передать контроль вашему тесту или скрипту.
driver.get("https://www.mirea.ru")
# Проверяем есть ли в html-теге <title> подстрока "технологический"
assert "технологический" in driver.title
# Ищем на странице html-тег с параметром name="q" - строка поиска
elem = driver.find_element_by_name("q")
# Вводим в найденное поле  "Стипендия"
elem.send_keys("Стипендия")
# Эмулируем нажатие Enter
elem.send_keys(Keys.RETURN)
# Проверим наличие фразы на странице
assert "Стипендии Президента и Правительства РФ" in driver.page_source
# Закроем страницу
driver.close()
