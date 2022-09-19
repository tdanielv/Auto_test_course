import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return math.log(abs(12*math.sin(x)))

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button2 = browser.find_element(By.ID, 'book').click()

    browser.find_element(By.ID, 'answer').send_keys(str(calc(int(browser.find_element(By.ID, 'input_value').text))))
    button3 = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button3)
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()



# После выполнения кода элемент button должен оказаться в верхней части страницы
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# Эта команда проскроллит страницу на 100 пикселей вниз:
    # browser.execute_script("window.scrollBy(0, 100);")
import os

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)