import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://olympus.greatlearning.in/dashboard")

emailBox = driver.find_element_by_xpath('//*[@id="login"]')
passWord = driver.find_element_by_xpath('//*[@id="password"]')
enterButton = driver.find_element_by_xpath('//*[@id="loginSubmitButton"]')

emailBox.send_keys('nishanth818@gmail.com')
passWord.send_keys('Neya@8012')
enterButton.click()


try:
    tripleButton = driver.find_element_by_xpath(
        '//*[@id="root"]/header/div/div/button')
    tripleButton.click()
    programBox = driver.find_element_by_xpath(
        '/html/body/div[2]/div[3]/div/div[2]/div/div/div')
    programBox.click()
    sec_B = driver.find_element_by_xpath('//*[@id="menu-"]/div[3]/ul/li[1]')
    sec_B.click()

    switchButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.name, 'Switch Program')))

except:
    print('Not opening')
