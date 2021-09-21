from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from main import *
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_driver_path = "C:\python\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/uas/login")
file = open('config.txt')
lines = file.readlines()
userName = lines[0]
userPassword = lines[1]
elementID = driver.find_element_by_id('username')
elementID.send_keys(userName)
elementID = driver.find_element_by_id('password')
elementID.send_keys(userPassword)
elementID.submit()

search = driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
# getting from main.py
search.send_keys(listOfJobs[0])
search.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Jobs']")))
element.click()

jobsQueued = []


def getJobsAvailable(soup):
    jobsAvailable = []
    job = soup.find('ul', {'class': 'jobs-search-results__list list-style-none'})
    # cName = job.findall('li')
    for i in job:
        jobsQueued.append(i.text)
    print(jobsQueued)


getJobsAvailable(BeautifulSoup(driver.page_source))
