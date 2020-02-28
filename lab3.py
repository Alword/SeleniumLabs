import unittest
from selenium import webdriver
from random import shuffle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


delay = 2
calcUrl = "https://yandex.ru/search/?text=калькулятор"


class YandexCalc(unittest.TestCase):
    def setUp(self):    self.driver = webdriver.Firefox(executable_path='./geckodriver.exe',
                                                        firefox_binary='C:/Users/aasle/AppData/Local/Mozilla Firefox/firefox.exe')

    def getInput(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[1]/span[2]/span/input")))

    def getOutput(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "calculator-display__result")))

    def getRadLabel(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[1]/span[1]/label[2]")))

    def test_1(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys("1"+Keys.SHIFT+"+"+"1")
        calcOutput = self.getOutput()
        assert "2" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_2(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys("2"+Keys.SHIFT+"*"+"7")
        calcOutput = self.getOutput()
        assert "14" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_3(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys("2"+Keys.SHIFT+"+2*2")
        calcOutput = self.getOutput()

        assert "6" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_4(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"(2+2)*2")

        calcOutput = self.getOutput()
        assert "8" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_5(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"sp/6)")
        radLabel = self.getRadLabel()
        radLabel.click()
        calcOutput = self.getOutput()
        assert "0,5" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_6(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"cp/3)")
        radLabel = self.getRadLabel()
        radLabel.click()
        calcOutput = self.getOutput()
        assert "0,5" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_7(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"tp/4)")
        radLabel = self.getRadLabel()
        radLabel.click()
        calcOutput = self.getOutput()
        assert "1" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_8(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"c-p/4)/")
        time.sleep(1)
        calcInput.send_keys("s-p/4)")
        radLabel = self.getRadLabel()
        radLabel.click()

        calcOutput = self.getOutput()
        while calcOutput.text == "Ошибка":
            calcOutput = self.getOutput()

        assert '−1' == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_9(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"2^6")
        calcOutput = self.getOutput()
        assert "64" == calcOutput.text

        time.sleep(delay)
        self.driver.close()

    def test_10(self):
        self.driver.get(calcUrl)
        calcInput = self.getInput()

        calcInput.send_keys(Keys.SHIFT+"lg1000000)")
        calcOutput = self.getOutput()
        while calcOutput.text == "Ошибка":
            calcOutput = self.getOutput()
        assert "6" == calcOutput.text

        time.sleep(delay)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
