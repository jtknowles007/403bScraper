from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import credentials


myurl = 'https://secure05.principal.com/member/accounts'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument ('user-data-dir=C:\\Users\\John\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_instance = webdriver.Chrome('C:\\Program Files (x86)\\Python3\\chromedriver.exe', chrome_options = chrome_options)
chrome_instance.get (myurl)

myurl_userid = chrome_instance.find_element_by_id('userid')
myurl_userid.send_keys(credentials.uname)

myurl_pass = chrome_instance.find_element_by_id('pass')
myurl_pass.send_keys(credentials.pwd)

myurl_submit = chrome_instance.find_element_by_css_selector('.loginButton')
myurl_submit.submit()


html = chrome_instance.page_source
print (html)
#- It's giving me the html from the "please wait" screen.  Need to pause or something in order to get html
# from the next screen with the actual data I want.





# myurl_balance = chrome_instance.find_element_by_id('total-balance')

