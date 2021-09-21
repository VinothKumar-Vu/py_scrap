from selenium import webdriver
chrome_driver_path = "C:\python\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.careerguide.com/career-options")

a = driver.find_element_by_xpath('//*[@id="aspnetForm"]/div[6]/div[2]/div/div[2]/div/div[1]/div[1]/ul')
Lists = a.find_elements_by_tag_name("li")
for li in Lists:
    text = li.text
    print (text)

driver.close()
v = "fda"