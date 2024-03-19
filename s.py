import time
from selenium.webdriver.common.by import By
import time
import re
import string
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from random import randint
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
from selenium import webdriver

# setup chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# set the target URL
url = "https://suhuwaktogel.land/"
id = "conggacor"
passw = "cong999"
# set up the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
actions = ActionChains(driver)
driver.get("https://suhuwaktogel.land/")
time.sleep(3)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbar_username"]'))).send_keys(id)
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbar_password"]'))).send_keys(passw)
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="submitlogin"]'))).click()
time.sleep(0.2)
pon = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="setuju"]')))
time.sleep(2)
actions.move_to_element(pon).click().perform()
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content2"]/div[2]/div/div[4]/div/div[1]/div/div/h2'))).click()
time.sleep(0.5)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content2"]/div[2]/div/div[4]/div/div[2]/a/i'))).click()
time.sleep(0.5)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content2"]/div[2]/div[1]/a[1]'))).click()
time.sleep(0.5)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="li-4dquick"]/a'))).click()
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content4d"]/div[2]/div[1]/section/div[1]/div[3]'))).click()
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tebak"]'))).send_keys("90")
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="beli-2dset"]'))).send_keys("0.1")
time.sleep(0.2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kirimkan"]'))).click()
time.sleep(1)
ass = driver.switch_to.alert
# accept the alert
ass.accept()
time.sleep(1)
driver.close()
