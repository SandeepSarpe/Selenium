'''
Created on Sep 10, 2014

@author: sandeeps
'''
from com.opensilo.scripts.common import Utilities
from com.opensilo.scripts.common import MailVerification
from com.opensilo import opensilo
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUp:
    serve = Utilities.Utilities()
    def signupToOpenSilo(self,emailid):
        driver = self.serve.getMyDriver()
        #launch application
        self.serve.launchApplication(driver, opensilo.opensiloURL)
        #enter new email id
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtSignupEmail")))
        driver.find_element_by_id("txtSignupEmail").clear()
        driver.find_element_by_id("txtSignupEmail").send_keys(emailid)
        driver.find_element_by_id("btnSignup").click()

    def activateAccount(self):
        print 'inside Activate account'
        self.serve.launchApplication(self.serve.getMyDriver(),MailVerification.get_activationURL())

    def joinOpenSilo(self,record):
        print 'inside Join Opensilo'
        driver = self.serve.getMyDriver()

        #join opensilo using linked in profile
        driver.find_element_by_css_selector("span.cta").click()
        driver.find_element_by_id("session_key-oauth2SAuthorizeForm").clear()
        driver.find_element_by_id("session_key-oauth2SAuthorizeForm").send_keys("sarpe.sandeep@gmail.com")
        driver.find_element_by_id("session_password-oauth2SAuthorizeForm").clear()
        driver.find_element_by_id("session_password-oauth2SAuthorizeForm").send_keys("pappy010")
        driver.find_element_by_name("authorize").click()

        #Fill up sign up form and join opensilo
        #self.assertEqual("OpenSilo", driver.title)
        driver.find_element_by_id("txtfirstName").clear()
        driver.find_element_by_id("txtfirstName").send_keys(record[2])
        driver.find_element_by_id("txtlastName").clear()
        driver.find_element_by_id("txtlastName").send_keys(record[3])
        driver.find_element_by_id("txtdisplayName").clear()
        driver.find_element_by_id("txtdisplayName").send_keys(record[4])
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(record[5])
        driver.find_element_by_css_selector("div.agreeTo > input[type=\"checkbox\"]").click()
        driver.find_element_by_xpath("//input[@value='Join OpenSilo']").click()
        #self.assertEqual("OpenSilo", driver.title)

        #Wait for user to join opensilo
        ispageload = False
        while ispageload == False:
            #try:
                user_names = driver.find_elements_by_class_name("profileName")

                for username in user_names:
                    print username.text
                '''itr = iter(user_names)
                try:
                    while itr.next:
                        currentusername = record[2]+ " "+ record[3]
                        print currentusername
                        print itr.next().text
                        print itr.next().location
                        print.itr.next().id
                        if itr.next().text == currentusername:
                            break
                except StopIteration:
                    pass'''
            #except Error:

        '''boolean ispageload = false;
		Iterator<WebElement> itr;
		while(!ispageload){

			try{
				List<WebElement> elements = driver.findElements(By.className("profileName"));
				itr = elements.iterator();

				while(itr.hasNext()){
					WebElement element = (WebElement) itr.next();
					//System.out.println("***********************************"+element.getText()+"****");
					String currentusername = signupInfo.get(2)+" "+signupInfo.get(3);
					//System.out.println("***********************************"+currentusername+"****");
					if(element.getText().equals(currentusername)){
						ispageload = true;
						break;
					}
				}
			}catch(Exception e){
				System.err.println("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");
				System.err.println(e);
				System.err.println("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%");

			}

		}
		driver.findElement(By.id("settingsIcon")).click();
		driver.findElement(By.xpath(".//*[@id='settings']/div[3]/ul/li[2]/a")).click();'''
        
