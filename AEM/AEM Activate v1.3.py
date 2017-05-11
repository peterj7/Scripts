#AEM Activate v1.3
#
#built on AEM Activate v1.2
#modification: able to pull login credentials,
#web page urls, and country codes
#
#description: this is a python script that uses
#selenium to automate activating desired page(s)
#in aem author for desired country(s)
#Input -> enter url(s) + enter country code(s)
#Output -> specified pages activated for each country listed
#-------------------------------------------

#imports selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

print("START PROGRAM")

#user login credentials, pulled from logininfo.txt file
login = open("logininfo.txt")
info = login.read().split('\n')
userid = info[1]
userpass = info[3]
login.close()

#url and country code list pulled from .txt files
#*note - country code in url doesn't get counted, needs to be added to countries list
with open('urls.txt') as urls:
    urlList = urls.read().splitlines()
with open('countries.txt') as countries:
    countryList = countries.read().splitlines()

#builds array of urls with country codes inserted into url
countryUrl = []
for url in urlList:
    indexOfUnderscore = url.find("_")
    for country in countryList:
        countryUrl.append(""+country+url[(indexOfUnderscore+3):]) #pieces together url with different country code

#opens each url and activates the page
firstInstance = True
skippedUrl = []
driver = webdriver.Chrome() #opens desired web browser
for url in countryUrl:
    driver.get(url) #opens current instance of url in array
    driver.implicitly_wait(1) #waits(seconds) for page to load
    if firstInstance == True: #on first instance of opening aem, login is necessary
        driver.maximize_window()
        loginid = driver.find_element_by_id('username')
        loginid.clear()
        loginid.send_keys(userid)
        loginpass = driver.find_element_by_id('password')
        loginpass.clear()
        loginpass.send_keys(userpass)
        loginpass.send_keys(Keys.RETURN)
        firstInstance = False #login no longer necessary
        driver.implicitly_wait(1) #waits(seconds) for page to load after login
    try:
        pagetab = driver.find_element_by_css_selector(".x-tab-strip-text.cq-sidekick-tab.cq-sidekick-tab-icon-page").click() #clicks 'Page' tab in sidekick
    except WebDriverException: #neccessary if page is not fully loaded
        skippedUrl.append(url) #url activation skipped and added to skippedUrl list
        print("SKIPPED "+url)
    else:
        activatepage = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='Activate Page']").click() #clicks 'Activate Page' button in sidekick
        print("SUCCESSFUL "+url)
        driver.implicitly_wait(1) #waits 1 second for page to load after activating

#activation for skippedUrl list where activation was skipped due to partially loaded pages
for url in skippedUrl:
    driver.get(url) #opens current instance of url in array
    driver.implicitly_wait(1) #waits(seconds) for page to load
    try:
        pagetab = driver.find_element_by_css_selector(".x-tab-strip-text.cq-sidekick-tab.cq-sidekick-tab-icon-page").click() #navigates to 'Page' tab in sidekick
    except WebDriverException:
        skippedUrl.append(url) #url is reappended to skippedUrl list due to page not fully loaded
        print("RETRY SKIPPED "+url)
    else:
        activatepage = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='Activate Page']").click() #clicks 'Activate Page' button in sidekick
        print("RETRY SUCCESSFUL "+url)
        driver.implicitly_wait(1) #waits(seconds) for page to load after activating

print("END PROGRAM")

driver.close() #closes web browser when script is done
