from selenium import webdriver
import time
import csv
from time import strftime

driver = webdriver.Firefox() # initiate a driver (by default firefox)
driver.get("https://wwws.mint.com/login.event") # go to the login page

# log in
username_field = driver.find_element_by_name("Email")# get the username field
password_field = driver.find_element_by_name("Password")# get the password field
username_field.send_keys("your username here") # enter in your username
password_field.send_keys("your password here") # enter in your password
password_field.submit() # submit it

#wait for login to happen
time.sleep(10)

#refresh page and wait 25 seconds
refreshButton = driver.find_element_by_xpath("//*[@id=\"module-accounts-update\"]")
refreshButton.click()

#wait for refresh to happen
time.sleep(30)

#Get net worth text
balanceElement = driver.find_element_by_xpath("//*[@id=\"moduleAccounts-bank\"]/div/h3/span[2]")
balance = balanceElement.text
print balance

#close browser
driver.quit()

#get current time
currentTime = strftime("%Y-%m-%d %H:%M:%S")
print(currentTime)

#write info to csv
balanceCSV = open('balance.csv','a')
csvwriter = csv.writer(balanceCSV)
csvwriter.writerow([balance, currentTime])
balanceCSV.close()
