'''
Created on Sep 10, 2014

@author: sandeeps
'''
from selenium import webdriver
import time
import csv
import os
from com import properties

class Utilities:
    driver = webdriver.Firefox()
    output_file = ''
    testdata = []

    def getmydriver(self):
        #Launch application
        return self.driver

    def launchapplication(self,driver,url):
        driver.get(url)

    def readCSV(self):
        csvfile_path = properties.input_path
        output_path = properties.output_path

        with open(csvfile_path, 'rb') as f:
            reader = csv.reader(f)
            for i in reader:
                Utilities.testdata.append(i)

        #Create output file
        Utilities.output_file = os.path.join(output_path, "TestResultReport_" + time.strftime("%Y-%m-%d-%H%M%S", time.localtime())) + ".csv"
        with open(Utilities.output_file,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writing.writerow(['Test_case', 'Parking Lot', 'IN_time', 'IN_date', 'OUT_time', 'OUT_date', 'Actual_cost', 'Expected_cost', 'Actual_time', 'Expected_time', 'Result', 'Comments'])

        return Utilities.testdata


    def writeCSV(self,testresult):
        with open(Utilities.output_file ,'a') as f:
            writing = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            item = testresult
            writing.writerow(
                [item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11]])
    