from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from xvfbwrapper import Xvfb

with Xvfb() as xvfb:
    #firefox_binary = FirefoxBinary('/usr/local/firefox/firefox-bin')
    #driver = webdriver.Firefox(firefox_binary = firefox_binary) 
    driver = webdriver.Firefox()
    driver.get("http://192.168.99.1:44444/")
