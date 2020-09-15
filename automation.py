from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')

time.sleep(1)
emailButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
emailButton.send_keys('whenwhatwhy1@gmail.com')

passwordButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
passwordButton.send_keys('Encrypted123')

loginButton = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
loginButton.click()

time.sleep(2)
notnowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notnowButton.click()

searchButton = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
searchButton.send_keys('cristiano')

time.sleep(1)
clickAccount = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span')
clickAccount.click()

time.sleep(1)
followersForAccount = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
followersForAccount.click()

time.sleep(2)
# Get all buttons that has the text Follow 
buttons = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
for btn in buttons:
    # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable unless you go to it's location
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(10)

