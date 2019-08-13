Hellow selinium
https://chercher.tech/python/table-selenium-python




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

import xlrd
import time
import pandas as pd
import csv

username

password=""
driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
#driver.implicitly_wait()
#kaizala_web1 = "https://manage.kaiza.la"
prod     = "https://manage.kaiza.la"


#driver = new WebDriverWait(driver, 10);
driver.get(alpha)
driver.maximize_window()

driver.find_element_by_id("i0116").send_keys(username)
driver.find_element_by_id("idSIButton9").click()
driver.implicitly_wait(20)

def listgroups(driver):
    #time.sleep(30)
    driver.find_element_by_id("Group").click() # here we can use by ID or Xpath # Alternative (driver.find_element_by_xpath("//*[@id='Group']/div").click())

    mypath="//*[@id = 'tableOrgGroupsConversations']/tbody/tr"

    driver.implicitly_wait(20)

    time.sleep(30)

    Rows = len(driver.find_elements_by_xpath(mypath))
    print("number of rows", Rows)
    print(type(Rows))
#    count =0
    ro = []
    for count in range(1,Rows+1):
        print("row_count",count)
        mystr=mypath+'/td['+str(count)+']/span[2]/a/span[1]'
        print(mystr)

        mystr1 = mypath +'/td['+ str(count)+']/span[2]/a/span[1][//@class="ng-binding"]'
        mystr1.__getattribute__()


#        //td[@colspan="10"]
#        print(mystr1)
 #       time.sleep(30)
  #      data= driver.find_element_by_xpath(mystr1)
        #print(data.text())

    #print(ro)

    #driver.get_screenshot_as_file("sample.png")

    #colun=len((driver.find_elements_by_xpath("//*[@id = 'tableOrgGroupsConversations']/tbody/tr[1]/td")))
    #print("colun",colun)




#"//*[@id = 'tableOrgGroupsConversations']/tbody/tr/td/span[2]/a/span"



listgroups(driver)
#Group_create(driver)
#CreateGroup_AddBulkUpload_AddUsersTOGroup(driver)
#Group_Search(driver,"Testing_1")
#user_Search(driver)





