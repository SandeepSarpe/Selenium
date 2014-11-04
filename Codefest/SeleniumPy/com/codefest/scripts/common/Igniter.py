'''
Created on Sep 10, 2014

@author: sandeeps
'''
from com.codefest.scripts.common.Utilities import Utilities
from com.codefest.scripts.problems.problem1 import ParkingChrgCalc
from com import properties
from com.codefest.scripts.problems.problem1.TestSuite import TestSuite


class Igniter():
    '''def openApp(self):
        driver = serve.getmydriver()
        serve.launchapplication(driver, properties.application_url)'''

if __name__ == "__main__":
    serve = Utilities()
    testsuite = TestSuite()
    park_calc = ParkingChrgCalc.ParkingChrgCalc()
    testdata = []

    #Launch Application
    #igniter.openFF()
    serve.launchapplication(serve.getmydriver(),properties.application_url)

    #Read test data
    testdata = serve.readCSV()

    #Run Test Suite
    for i in range(len(testdata)):
            if i > 0:
                record = testdata[i]
                print record
                actual_time_display, actual_cost = park_calc.actualParkingchargeCalc(record)
                expected_time_display, expected_cost = park_calc.expectedParkingchargeCalc(record)

                print 'actual_cost: ' + str(actual_cost)
                print 'expected_cost: ' + str(expected_cost)
                print 'actual_time: ' + str(actual_time_display)
                print 'expected_time: ' + str(expected_time_display)

                testsuite.testParkingCost(record,actual_cost,expected_cost)
                testsuite.testParkingTime(record,actual_time_display,expected_time_display)




    