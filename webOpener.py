import os
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C://geckodriver//geckodriver.exe")
driver.get("https://olympus.greatlearning.in/dashboard")


def GL_loggin():
    emailBox = driver.find_element_by_xpath('//*[@id="login"]')
    passWord = driver.find_element_by_xpath('//*[@id="password"]')
    enterButton = driver.find_element_by_xpath('//*[@id="loginSubmitButton"]')

    emailBox.send_keys('nishanth818@gmail.com')
    passWord.send_keys('Neya@8012')
    enterButton.click()


def switchBox():
    switchBox = driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div[3]/div/button[2]/span[1]')
    switchBox.click()


def secB():
    secB_Box = driver.find_element_by_xpath(
        "/html/body/div[3]/div[3]/ul/li[1]/p")
    secB_Box.click()

    switchBox = driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div[3]/div/button[2]/span[1]')
    switchBox.click()

    upcomingBox = driver.find_element_by_xpath(
        '/html/body/div[1]/main/div/div/div/div[3]/div/div[1]/div[2]/div/button[1]')
    upcomingBox.click()


def secA():
    secA_Box = driver.find_element_by_xpath(
        "/html/body/div[3]/div[3]/ul/li[2]/p")
    secA_Box.click()

    switchBox = driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div[3]/div/button[2]/span[1]')
    switchBox.click()

    upcomingBox = driver.find_element_by_xpath(
        '/html/body/div[1]/main/div/div/div/div[3]/div/div[1]/div[2]/div/button[1]')
    upcomingBox.click()


def secML():
    secML_Box = driver.find_element_by_xpath(
        "/html/body/div[3]/div[3]/ul/li[3]/p")
    secML_Box.click()

    switchBox = driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div[3]/div/button[2]/span[1]')
    switchBox.click()

    upcomingBox = driver.find_element_by_xpath(
        '/html/body/div[1]/main/div/div/div/div[3]/div/div[1]/div[2]/div/button[1]')
    upcomingBox.click()


def CheckDashboard():
    programBox = driver.find_element_by_xpath(
        "/html/body/div[1]/header/div/div/div[2]/div/div/div")
    programBox.click()
    secB()


GL_loggin()
CheckDashboard()
