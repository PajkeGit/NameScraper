from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib
import urllib.request
import os, sy

driver_path = 'C:/Program Files/chromedriver/bin/chromedriver.exe'
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

options = webdriver.ChromeOptions()
options.binary_location = brave_path                                    # Remove this if you're using Chrome
options.add_extension("ASDA")                                           # REPLACE THIS WITH THE PATH OF THE .crx FILE!

browser = webdriver.Chrome(executable_path=driver_path, chrome_options = options )
f = open("names.txt", "w")
 
for x in range(4000,6000):                                             # Replace the Numbers with starting number and end number
    browser.get("https://www.thehashmasks.com/detail/"+str(x))
    time.sleep(2)
    element = browser.find_element_by_tag_name('h1')
    print(element.text)
    f.write(element.text+"\n")


f.close()

