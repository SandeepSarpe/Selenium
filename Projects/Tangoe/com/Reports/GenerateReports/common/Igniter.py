'''
Created on Oct 16, 2014

@author: sandeeps
'''
from com.Reports.GenerateReports.common.Utilities import Utilities
from com import properties
from com.Reports.GenerateReports.Reports import Report
import csv
import time


class Igniter():
    '''def openApp(self):
        driver = serve.getmydriver()
        serve.launchapplication(driver, properties.application_url)'''

if __name__ == "__main__":
    serve = Utilities()
    report = Report()

    #Launch Application
    serve.launchapplication(serve.getmydriver(),properties.application_url)

    #Login to Tangoe
    serve.login(serve.getmydriver())

    #Navigate to Generate Reports
    report.navigate_To_reports(serve.getmydriver())

    # Select report - Read the report from ______Reports.csv file
    with open(properties.report_category_csv, 'rb') as f:
        reader = csv.reader(f)

        #loop through reports in ______Reports.csv
        for i in reader:
            dep_report = i[0]
            param_format = i[1]
            #path = 'properties.'+param_format

            #Select Report Category - Read it from properties file
            report.getinto_report_category(serve.getmydriver(),properties.report_category)

            report.getintoReport(serve.getmydriver(),dep_report)
            with open(properties.ParameterFormat1_csv, 'rb') as g:
                param_reader = csv.reader(g)
                for j in param_reader:
                    report.selectParam(serve.getmydriver(), param_format, j)
                    report.downloadReport(serve.getmydriver())
                    time.sleep(10) #Need to find out exact time to doenlaod the file and wait until that time
                    serve.getmydriver().find_element_by_link_text("Back to Report Parameters Page").click()
                    time.sleep(3)
            serve.getmydriver().find_element_by_link_text("Back to Report List").click()



#Choose parameter format for the current report among ParamaterFormat_.csv and loop through parameter combinations




    #Select Parameters

    #Wait Until Report fetch

    #downoad Reports

    #Read test data
    #testdata = serve.readCSV()






    