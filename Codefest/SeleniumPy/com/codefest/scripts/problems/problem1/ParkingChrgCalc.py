__author__ = 'sandeeps'

from selenium.webdriver.support.ui import Select
import time
from com.codefest.scripts.common import Utilities

class ParkingChrgCalc:

    def actualParkingchargeCalc(self,record):
        serve = Utilities.Utilities()
        driver = serve.getmydriver()
        Select(driver.find_element_by_id("Lot")).select_by_visible_text(record[0])
        driver.find_element_by_id("EntryTime").clear()
        driver.find_element_by_id("EntryTime").send_keys(record[1])
        driver.find_element_by_id("EntryDate").clear()
        driver.find_element_by_id("EntryDate").send_keys(record[2])
        driver.find_element_by_id("ExitTime").clear()
        driver.find_element_by_id("ExitTime").send_keys(record[3])
        driver.find_element_by_id("ExitDate").clear()
        driver.find_element_by_id("ExitDate").send_keys(record[4])
        driver.find_element_by_name("Submit").click()
        actual_cost = (driver.find_element_by_xpath("html/body/form/table/tbody/tr[4]/td[2]/span[1]/font/b").text).strip()
        actual_ptime = (driver.find_element_by_xpath("html/body/form/table/tbody/tr[4]/td[2]/span[2]/font/b").text).strip()
        return actual_ptime,actual_cost

    def expectedParkingchargeCalc(self,record):
        a = time.strptime(record[2]+'T'+record[1]+'Z', '%m/%d/%YT%H:%MZ')
        b = time.strptime(record[4]+'T'+record[3]+'Z', '%m/%d/%YT%H:%MZ')
        a = time.mktime(a)
        b = time.mktime(b)
        diff = b - a
        days = int(diff) / 86400
        hours = int(diff) / 3600 % 24
        minutes = int(diff) / 60 % 60
        diffdisplay =  '(' +str(days)+' Days, '+str(hours)+' Hours, '+str(minutes)+' Minutes)'
        thours =  (days * 24 + hours + abs(minutes/60))

        if record[0] == 'Short-Term Parking':
            pcharge = thours * 2
        elif record[0] == 'Economy Parking':
            pcharge = thours * 4
        elif record[0] == 'Long-Term Surface Parking':
            pcharge = thours * 2
        elif record[0] == 'Long-Term Garage Parking':
            pcharge = thours * 2
        elif record[0] == 'Valet Parking':
            pcharge = thours * 12

        return diffdisplay,'$ ' + str("%.2f" % pcharge)







