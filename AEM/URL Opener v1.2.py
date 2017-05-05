#URL Opener v1.2
#
#built on URL Opener v1.1
#modification: preview mode available by user input
#and login, url list, country list pulled in from .txt files
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

#user login credentials, pulled from logininfo.txt file
login = open("logininfo.txt")
info = login.read().split('\n')
userid = info[1]
userpass = info[3]
login.close()

#url and country code list pulled from .txt files
#full sites: en_us en_gb en_be en_dk en_nl de_de de_at de_ch fr_fr it_it zh_cn ja_jp ko_kr
#micro sites: en_au en_hk en_in en_my en_ph en_sg pt_br es_es es_mx ch_tw
with open('urls.txt') as urls:
    urlList = urls.read().splitlines()
with open('countries.txt') as countries:
    countryList = countries.read().splitlines()

#asks user if preview mode is desired
validInput = False
while validInput == False:
    previewDesired = input('Preview Mode? 1 = Yes, 0 = No ')
    if previewDesired == "1":
        previewMode = True
        validInput = True
    elif previewDesired == "0":
        previewMode = False
        validInput = True

#checks for aem or external url
checkAem = False
for i, url in enumerate(urlList):
    if "aem" in url:
        checkAem = True
        if previewMode == True:
            urlList[i] = url+"?wcmmode=disabled&previewpath=true"
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
