from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import xlrd
import pandas as pd
import csv

def excel_import():
    #print("hellow world")
    GroupIdList=[]
    with open("C:\\Users\\v-mosaip\\Downloads\\GroupInfo.csv", "rt",) as fd:
        data= csv.reader(fd)
        for num,line, in enumerate(data):
            if num > 0:
                #print(line)
                print(line[1])
                GroupIdList.append(line[1])
    return GroupIdList




username="v-mosaip@microsoft.com"
username_inno="mpigelati@innominds.com"

password=""
driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
kaizala_web1 = "https://manage.kaiza.la"
driver.get(kaizala_web1)
driver.maximize_window()
driver.find_element_by_id("i0116").send_keys(username)
driver.find_element_by_id("idSIButton9").click()
driver.implicitly_wait(20)

def Group_create():
    print("Group Ceate")
    driver.find_element_by_id("Group").click() # here we can use by ID or Xpath # Alternative (driver.find_element_by_xpath("//*[@id='Group']/div").click())
    #driver.find_element_by_id("group - bulkupload - dropdown").click()
    driver.implicitly_wait(20)
    print("Before Creating Group_Bulk_Upload",driver.current_url)
    driver.find_element_by_id("group-bulkupload-dropdown-elmt").click()
    driver.find_element_by_id("upload").click()
    driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("C:\\Users\\v-mosaip\\Desktop\\Groups\\G1.csv")
    driver.find_element_by_xpath('//*[@id="upload-groups"]/div/div/div[3]/div/button[1]').click()
    driver.implicitly_wait(20)
    driver.find_elements_by_xpath('// *[ @ id = "uploaded-groups-tasks"] / div / div / div[1] / button')
    driver.implicitly_wait(30)
    print("After Creating Group_Bulk_Upload",driver.current_url)
    driver.refresh()
    #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    #driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
    # Till gere it is working\
    #driver.find_element_by_css_selector('div[id="uploaded-groups-tasks"] button[title="Close"]').click()
    #driver.fin


    #driver.implicitly_wait(100)
    #driver.find_element_by_tag_name("body").send_keys("ESCAPE")
    #driver.implicitly_wait(30)
    # check the group name and
#    driver.find_element_by_xpath('//*[@id="uploaded-groups-tasks"]/div/div/div[1]/button').click()

    #driver.find_element_by_id("groupUploadFileName").send_keys('C:\\Users\\v-mosaip\\Desktop\\Groups\\G3.csv')
    #driver.find_element_by_xpath("//*[@id='upload-groups']/div/div/div[3]/div/button[1]").click()
    #driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("C:\\Users\\v-mosaip\\Desktop\\Groups\\G3.csv")


    #driver.find_element_by_css_selector('input[type="file"]').clear()
    #driver.find_element_by_css_selector('input[type="file"]').send_keys('C:\\Users\\v-mosaip\\Desktop\\Groups\\G3.csv')
    #driver.find_element_by_xpath("// *[ @ id = 'group-bulkupload-dropdown'] / span")
    #driver.find_element_by_xpath("//*['@id='group-bulkupload-dropdown']/span").click()
    #driver.find_element_by_id("upload").click()
    #upload
    #driver.find_element_by_id("export-existing-groups").click()

Group_create()
#driver.find_element_by_xpath("//*[@id='sidebar']/div[3]").click()

#driver.find_element_by_id("Group").click() # here we can use by ID or Xpath # Alternative (driver.find_element_by_xpath("//*[@id='Group']/div").click())
#driver.find_element_by_id("export-existing-groups").click()
# Function to get list for GroupId's
#GroupId=[]
#GroupId = excel_import()
'''
driver.implicitly_wait(20)
for count,line in enumerate(GroupId):
    print(count)
    myid=line+"MoreOptionsGroups"
    print(type(myid))
    print("{}{}".format(myid, count))
    driver.find_element_by_id(myid).click()
    driver.implicitly_wait(20)

    #driver.find_element_by_css_selector(role="menuitem").click()
    #driver.find_element(By.CSS_SELECTOR,'ng-click')
    #driver.find_element_by_css_selector(ng-click="::setGrouptoDelete(orgGroupInfo)").click
    #driver.find_element_by_name()
    #driver.find_element_by_name("ng-click").click()
    #driver.find_element_by_xpath("//*[@id='tableOrgGroupsConversations']/tbody/tr[1]/td[5]/div/ul/li[3]/a").click()
    # Pending
    #driver.find_element_by_xpath("//*[@id='delete-group-modal']/div/div/div[2]/button[2]").click()
'''
