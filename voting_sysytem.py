import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv


if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.exe'
else:
    PHANTOMJS_PATH = './phantomjs'
start=time.time()
with open("Data.csv") as csv_file: #file containing voters data
        
	csv_reader = csv.reader(csv_file)
	regcounter = 0
	newreg = 0
	
	#Constants used for a particular voting website. Change as needed
	browser = webdriver.PhantomJS("~PATH/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe") #download from https://phantomjs.org/download.html
	for data in csv_reader:
            
            try:
                browser.get('https://www.keepmovingindia.com/?utm_source=Money%20Control')
                submit_log = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li/a").click()
                print(data)
                name_inp = browser.find_element_by_xpath("//*[@id='u_name']").send_keys(data[0])
                email_inp = browser.find_element_by_xpath("//*[@id='u_email']").send_keys(data[1])
                mobile_inp = browser.find_element_by_xpath("//*[@id='u_mobile']").send_keys(data[2])
                pass_inp = browser.find_element_by_xpath("//*[@id='u_pass']").send_keys(data[3])
                passc_inp = browser.find_element_by_xpath("//*[@id='u_confpass']").send_keys(data[4])
                submit_btn = browser.find_element_by_css_selector('.btn.btn-default').click()
                submit_log = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/a").click()
                newreg +=1
            except Exception:
                print ("Already registered")
                regcounter += 1
                pass
            
end = time.time()
print ("New registrations:", newreg)
print ("Already registered counts:", regcounter)
print ("Time taken for", newreg, "registrations is ", end - start, "seconds")

            
            
            
            
            
            
            
            

