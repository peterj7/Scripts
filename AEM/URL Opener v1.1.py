#URL Opener v1.1
#
#built on URL Opener v1.0
#modification: able to take in multiple urls
#and multiple countries at the same time.
#handles case of both aem and external links
#included in desired urls
#
#description: this is a python script that uses
#selenium to automate opening desired page(s)
#in aem or externally
#Input -> enter url(s) + enter country code(s)
#Output -> url(s) are opened in one web browser window
#-------------------------------------------

#imports selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("START PROGRAM")

#user login credentials
userid = ""
userpass = ""

#enter desired url and desired countries to open
urlList = [] #country code in url doesn't get counted, needs to be added to countries list
countryList = []

#checks for aem or external url
checkAem = False
for url in urlList:
    if "aem" in url:
        checkAem = True
        break

#builds array of urls with country codes inserted into url
countryUrl = []
for url in urlList:
    indexOfUnderscore = url.find("_")
    for country in countryList:
        countryUrl.append(url[:(indexOfUnderscore-2)]+country+url[(indexOfUnderscore+3):]) #pieces together url with different country code

#opens each url
firstInstance = True
skippedUrl = []
driver = webdriver.Chrome() #opens desired web browser
driver.maximize_window()
for url in countryUrl:
    driver.get(url) #opens current instance of url in array
    print("OPEN "+url)
    driver.implicitly_wait(1) #waits(seconds) for page to load
    if (firstInstance == True and checkAem == True): #on first instance of opening aem, login is necessary
        if "aem" in url:
            loginid = driver.find_element_by_id('username')
            loginid.clear()
            loginid.send_keys(userid)
            loginpass = driver.find_element_by_id('password')
            loginpass.clear()
            loginpass.send_keys(userpass)
            loginpass.send_keys(Keys.RETURN)
            firstInstance = False #login no longer necessary
    driver.execute_script("window.open('');") #opens a new tab
    driver.switch_to_window(driver.window_handles[-1]) #switches focus to new tab
driver.execute_script("window.close('');") #closes the last new tab

print("END PROGRAM")
