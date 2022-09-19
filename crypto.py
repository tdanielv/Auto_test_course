import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def first_name():
    firstname = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    return firstname.send_keys('Dan')



link = 'https://bitcoin24.su/'

try:
    # browser = webdriver.Chrome()
    # browser.get(link)
    #
    # def BTC():
    #     courses = browser.find_elements(By.CLASS_NAME, 'xtt_one_line_curs')
    #     names = browser.find_elements(By.CLASS_NAME, 'xtt_one_line_name_right')
    #     for i in range(len(courses)):
    #         print(names[i].text, '====', float((courses[i].text)[4:]))
    #
    # # BTC()
    # print('END')
    # time.sleep(5)


    def DAI_DAI():
        button = browser.find_element(By.XPATH, '//div[@class="xtt_one_line_name" and contains(., "DAI")]')
        button.click()
        courses = browser.find_elements(By.CLASS_NAME, 'xtt_one_line_curs')
        names = browser.find_elements(By.CLASS_NAME, 'xtt_one_line_name_right')
        for i in range(len(courses)):
            print(names[i].text, '====', float((courses[i].text)[4:]))


    # DAI_DAI()

    link = 'https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?redirect_uri=storagerelay%3A%2F%2Fhttps%2Faccounts.binance.com%3Fid%3Dauth419904&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=960821425630-aclsesu662patrhhq95iuuijekgg15p3.apps.googleusercontent.com&ss_domain=https%3A%2F%2Faccounts.binance.com&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, "identifierId").send_keys('daniil.tkalich@gmail.com')
    browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]').click()



finally:
    time.sleep(1000)
    browser.quit()

