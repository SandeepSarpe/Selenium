'''
Created on Sep 10, 2014

@author: sandeeps
'''
from selenium import webdriver
import time
import csv
import os
from com import properties
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utilities:

    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir","C:\Users\sandeeps\PycharmProjects\Tangoe\com\Reports\GenerateReports\Downloads")
    fp.set_preference("pdfjs.disabled",True)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk",('application/pdf'))

    driver = webdriver.Firefox(firefox_profile=fp)
    #driver = webdriver.Chrome()
    #driver = webdriver.Chrome(executable_path=r"E://Sandeep//UpToDate//New era//Selenium//pythonselenium//chromedriver.exe")
    '''chromedriver = "E:/Sandeep/UpToDate/New era/Selenium/pythonselenium/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("www.google.com")'''

    #output_file = ''
    testdata = []
    #driver.find_element_by_xpath()

    def getmydriver(self):
        return self.driver

    def launchapplication(self,driver,url):
        driver.get(url)
        driver.maximize_window()


    def login(self,driver):
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(properties.usernameadmin)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(properties.passwordadmin)
        driver.find_element_by_name("Login").click()
        #WebDriverWait(driver, 60).until(EC.presence_of_element_located(By.XPATH,".//*[@id='wizHomeTop']/strong"))

    def waitUntilElementToBeClickableById(self,driver,id):
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
        finally:
            print "finally"

    def waitUntilvisibility_of_element_locatedByName(self,driver,name):
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, name)))
        finally:
            print "finally"

    def readCSV(self,csvfile_path):
        output_path = properties.output_path

        with open(csvfile_path, 'rb') as f:
            reader = csv.reader(f)


        #Create output file
        '''Utilities.output_file = os.path.join(output_path, "TestResultReport_" + time.strftime("%Y-%m-%d-%H%M%S", time.localtime())) + ".csv"
        with open(Utilities.output_file,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writing.writerow(['Test_case', 'Parking Lot', 'IN_time', 'IN_date', 'OUT_time', 'OUT_date', 'Actual_cost', 'Expected_cost', 'Actual_time', 'Expected_time', 'Result', 'Comments'])'''

        return reader


    def writeCSV(self,testresult):
        with open(Utilities.output_file ,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            item = testresult
            writing.writerow(
                [item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]])
    