from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

username = "admin"
password = "admin123"
url = 'https://itera-qa.azurewebsites.net/Login'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver',options=chrome_options)

#Open URL 
driver.get(url)

#Input username to field
uname = driver.find_element("id", "Username")
uname.send_keys(username)

#Input password to field
pwd = driver.find_element("id", "Password")
pwd.send_keys(password)

#Click login button
btn = driver.find_element(By.XPATH,"//input[@name='login']")
btn.click()

#check if login successful
try:
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH,"//h3[normalize-space()='Welcome admin']"))
    print("Login successful")
except:
    print("Login unsuccessful")

driver.close()