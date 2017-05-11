#AEM Rollout v1.0
#
#description: this is a python script that uses
#selenium to automate rolling out desired page(s)
#on the blueprint in aem author for the desired child country(s)
#Input -> enter blueprint url(s) + enter country code(s)
#Output -> specified pages rolled out for each child country listed
#-------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
import time

#function to convert all external urls to aem url
def aemUrl(url):
    indexOfUnderscore = url.find("_")
    blueprintUrl = url[(indexOfUnderscore-2):(indexOfUnderscore+3)]
    if url.find("aemauthor") == -1: #url is not in aem
        url = ""+blueprintUrl+url[(indexOfUnderscore+3):]
    return url

#rollout function, rollout on one blueprint page to multiple countries
def rollout(driver, url, countryList):
    pageLoaded = False
    rolloutWindowLoaded = False
    countrySelectLoaded = False
    rolloutButtonLoaded = False
    while pageLoaded != True:
        try:
            pagetab = driver.find_element_by_css_selector(".x-tab-strip-text.cq-sidekick-tab.cq-sidekick-tab-icon-page").click() #clicks 'Page' tab in sidekick
        except WebDriverException: #neccessary if page is not fully loaded
            print("PAGE NOT FULLY LOADED")
        else:
            pageLoaded = True
            rolloutpage = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='Rollout Page']").click() #clicks 'Rollout Page' button in sidekick
            driver.implicitly_wait(1)
            while rolloutWindowLoaded != True:
                try:
                    nextpage = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='Next']").click() #clicks 'Next' button in sidekick
                    time.sleep(2) #waits 2 seconds, avoids problem of checkboxes not being fully loaded
                except (ElementNotVisibleException, NoSuchElementException): #exception occurs when page is not fully loaded
                    print("NOT FULLY LOADED ROLLOUT WINDOW")
                else:
                    rolloutWindowLoaded = True
                    driver.implicitly_wait(1)
                    while countrySelectLoaded != True:
                        try:
                            onRollout = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='On Rollout']") #locates 'on rollout' checkbox
                        except (ElementNotVisibleException, NoSuchElementException): #exception occurs when page is not fully loaded
                            print("NOT FULLY LOADED UNSELECT ALL")
                        else:
                            a1 = webdriver.common.action_chains.ActionChains(driver) #use actions to click on specific coordinates on the screen
                            a1.move_to_element_with_offset(onRollout, -365, 15).click().perform() #uses 'on rollout' location to click 'unselect all' checkbox
                            driver.implicitly_wait(1)
                            print("SUCCESSFULLY UNSELECTED ALL")
                            countrySelectLoaded = True
                            for countryCode in countryList:
                                try:
                                    childPage = driver.find_element_by_xpath('//div[contains(text(), "' + countryCode + '")]') #locates country code in the rollout window
                                except (ElementNotVisibleException, NoSuchElementException): #exception occurs when page is not fully loaded
                                    print("NOT FULLY LOADED "+countryCode+" CHECKBOX")
                                    countryList.append(countryCode)
                                else:
                                    a2 = webdriver.common.action_chains.ActionChains(driver)
                                    a2.move_to_element_with_offset(childPage, -15, 5).click().perform() #uses country code location to click matching checkbox
                                    driver.implicitly_wait(1)
                                    print("SUCCESSFULLY CHECKED "+countryCode+" BOX")
                            while rolloutButtonLoaded != True:
                                try:
                                    rollout = driver.find_element_by_xpath("//button[@class=' x-btn-text'][text()='Rollout']") #locates 'rollout' button
                                except (ElementNotVisibleException, NoSuchElementException): #exception occurs when page is not fully loaded
                                    print("NOT FULLY LOADED ROLLOUT BUTTON")
                                else:
                                    a3 = webdriver.common.action_chains.ActionChains(driver)
                                    a3.move_to_element_with_offset(rollout, 1, 1).click().perform() #clicks 'rollout button'
                                    driver.implicitly_wait(1)
                                    print("SUCCESSFULLY CLICKED ROLLOUT BUTTON")
                                    rolloutButtonLoaded = True

print("START PROGRAM")

#user login credentials, pulled from logininfo.txt file
login = open("logininfo.txt")
info = login.read().split('\n')
userid = info[1]
userpass = info[3]
login.close()

#enter blueprint url and desired countries for activation
with open('urls.txt') as urls: #reads in urls from txt file
    urlList = urls.read().splitlines()
for u in urlList: #call aemUrl to convert urls
    u = aemUrl(u)
with open('countries.txt') as countries: #reads in country codes from txt file
    countryList = countries.read().splitlines()

driver = webdriver.Chrome() #opens desired web browser
driver.maximize_window() #maximize current browser window
driver.get("") #url for aem login page
loginid = driver.find_element_by_id('username')
loginid.clear()
loginid.send_keys(userid)
loginpass = driver.find_element_by_id('password')
loginpass.clear()
loginpass.send_keys(userpass)
loginpass.send_keys(Keys.RETURN)

#loops through each blueprint page for rollout
for url in urlList:
    driver.get(url)
    driver.implicitly_wait(1)
    rollout(driver, url, countryList) #calls rollout for current blueprint page url
    driver.execute_script("window.open('');") #opens new tab
    driver.switch_to_window(driver.window_handles[-1]) #changes focus onto newest tab
driver.execute_script("window.close('');") #closes last new tab

print("END PROGRAM")
