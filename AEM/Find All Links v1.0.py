#Find All Links v1.0
#
#description: this is a python script that uses
#selenium to automate showing every web address
#that the input web page links to
#Input -> 1 url
#Output -> every link on that web page
#-------------------------------------------

#imports selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("START PROGRAM")

#opens the input webpage and stores each url in a href in source code
driver = webdriver.Chrome() #opens desired web browser
driver.get("") #opens url
driver.implicitly_wait(1) #waits(seconds) for page to load
linkList = driver.find_elements_by_xpath("//a[@href]") #stores every link in <a href = ...> tag in linkList
for link in linkList:
    print(link.get_attribute("href"))

print("END PROGRAM")

driver.close() #closes web browser when script is done
