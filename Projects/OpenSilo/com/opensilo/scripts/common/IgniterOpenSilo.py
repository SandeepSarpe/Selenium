'''
Created on Sep 10, 2014

@author: sandeeps
'''
import csv
from com.opensilo.scripts.createusers import SignUp


class IgniterOpenSilo():

    def readCSV(self):
        signup = SignUp.SignUp()
        signupInfo = []
        csvfile_path = 'C:\Users\sandeeps\PycharmProjects\OpenSilo\com\Testdata.csv'
        
        with open(csvfile_path, 'rb') as f:
            reader = csv.reader(f)

            for i in reader:
                signupInfo.append(i)

            for i in range(len(signupInfo)):
                if i > 0:

                    record = signupInfo[i]
                    print record
                    #Sign up from landing page - This functionality will deprecated soon
                    signup.signupToOpenSilo(record[0])
                    
                    #Activate account by fetching valid registration link from email account - This functionality will deprecated soon
                    signup.activateAccount()
                    #Join Opensilo - This functionality will deprecated soon 
                    signup.joinOpenSilo(record)

if __name__=="__main__":
    ignitor = IgniterOpenSilo()
    ignitor.readCSV()
        
        
    
    
    