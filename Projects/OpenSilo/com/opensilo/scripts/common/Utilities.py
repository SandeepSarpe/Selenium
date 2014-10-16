'''
Created on Sep 10, 2014

@author: sandeeps
'''
from selenium import webdriver

class Utilities:
    driver = webdriver.Firefox() 
    def getMyDriver(self):
        #Launch application
        return self.driver
    def launchApplication(self,driver,url):
        driver.get(url)
    