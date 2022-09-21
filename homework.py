import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

text = ''


@pytest.mark.parametrize('link', [links[i] for i in range(len(links))])
def test_stepik_links(browser, link):
    global text
    try:
        browser.get(link)
        input = WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea')))
        input.send_keys(math.log(int(time.time())))
        button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        button.click()
        t = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
        if t.text != 'Correct!':
            text += t.text
    finally:
        print(text)

