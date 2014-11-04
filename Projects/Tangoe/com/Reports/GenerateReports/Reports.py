__author__ = 'sandeeps'

from com.Reports.GenerateReports.common.Utilities import Utilities
from selenium.webdriver.support.ui import Select
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Report:
    serve = Utilities()
    def navigate_To_reports(self,driver):
        time.sleep(2)
        driver.find_element_by_id("menuMainReporting").click()
        driver.find_element_by_id("menuMainReporting_Generate_Reports").click()

    def getinto_report_category(self,driver,report_category):
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame("CONTENT")
        driver.find_element_by_link_text(report_category).click()
        time.sleep(5)
        #driver.find_element_by_link_text("Charges Per Service Type By Department").click()


    def getintoReport(self,driver,dep_report):
        driver.find_element_by_link_text(dep_report).click()
        while (re.search(r'To view the report, first choose values for the parameters below', driver.page_source) == False):
            driver.find_element_by_link_text(dep_report).click()

    def selectParam(self,driver,param_format,param):
        #Select parameters
        if param_format == 'ParameterFormat1':
            Utilities().waitUntilvisibility_of_element_locatedByName(driver,"promptex-Billing Cycle Type")
            Select(driver.find_element_by_css_selector("select[name=\"promptex-Billing Cycle Type\"]")).select_by_visible_text(param[0])
            Select(driver.find_element_by_css_selector("select[name=\"promptex-Billing Cycle Period\"]")).select_by_visible_text(param[1])
            Select(driver.find_element_by_name("promptex-Hierarchy")).select_by_visible_text(param[2])
            #driver.find_element_by_css_selector("option[value=\"Secondary Hierarchy\"]").click()
            driver.find_element_by_class_name("tngoBtn").click()
        elif param_format == 'ParameterFormat2':
            print "Work in Progress!"
        else:
            print "No Parameter format found!"


    #Download Report
    def downloadReport(self,driver):
        driver.switch_to_frame("crystalReport")

        #Wait for report to generate
        Utilities().waitUntilElementToBeClickableById(driver,"exportdlgImage")

        driver.find_element_by_id("exportdlgImage").click()

        driver.implicitly_wait(5)

        parent_handle = driver.current_window_handle

        handles = driver.window_handles # before the pop-up window closes
        #handles.remove(parent_handle)
        driver.switch_to_window(handles.pop())
        Select(driver.find_element_by_id("exportformatlist")).select_by_visible_text("Adobe Acrobat (PDF)")#("Microsoft Excel 97-2000(XLS)")
        driver.find_element_by_css_selector("input.crexportbutton").click()
        driver.switch_to_window(parent_handle)
        driver.switch_to_frame("CONTENT")








        


