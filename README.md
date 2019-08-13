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

username=

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

    #driver.find_element_by_id("group - bulkupload - dropdown").click()
    driver.implicitly_wait(20)
    my_tr = []
    cell=[]
    #data= driver.find_element_by_xpath("//*[@id = 'tableOrgGroupsConversations']/tbody/tr[1]/td[1]/span[2]/a/span[contains(text(),'8-18 ')]")
    #print("mydata",data.text)
'''
    my_tr =driver.find_element_by_xpath("//*[@id = 'tableOrgGroupsConversations']/tbody/tr")-1
    cell=my_tr[1].find_element_by_tag_name("td")

    print("my_tr",my_tr)
    print("cell",cell)
    '''

my_len =len(driver.find_element_by_xpath("//*[@id = 'tableOrgGroupsConversations']/tbody/tr"))
print(my_len)



listgroups(driver)
#Group_create(driver)
#CreateGroup_AddBulkUpload_AddUsersTOGroup(driver)
#Group_Search(driver,"Testing_1")
#user_Search(driver)


