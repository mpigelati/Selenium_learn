Hellow selinium
https://chercher.tech/python/table-selenium-python


def listgroups(driver):
    #time.sleep(30)
    driver.find_element_by_id("Group").click() # here we can use by ID or Xpath # Alternative (driver.find_element_by_xpath("//*[@id='Group']/div").click())

    mypath="//*[@id = 'tableOrgGroupsConversations']/tbody/tr"
    mypath1 = "//*[@id = 'tableOrgGroupsConversations']/tbody"

    Rows = len(driver.find_elements_by_xpath(mypath))
    print("number of rows", Rows)

    for count in range(1,Rows+1):

        print("===================>Starting index",count)
        temp = Rows
        #print("===================>Rows", Rows)
        string = mypath1 + '/tr[' + str(temp) + ']/td/span/a/span[1]'
        string1 = mypath1 + '/tr[' + str(temp) + ']/td[2]/span'

        data1 = driver.find_element_by_xpath(string1)
        #print("mystring", string1)
        if data1.text != "Member":
            print("Admin-Member-->", data1.text)

            print("mystring",string)
            data=driver.find_element_by_xpath(string)
            print("Group-->",data.text)

            select_element= driver.find_element_by_xpath(mypath1+'/tr[' + str(temp)+']/td[5]')
            select_element.click()
            driver.find_element_by_xpath(mypath1+'/tr[' + str(temp)+']/td[5]/div/ul/li[3]/a').click()
            driver.find_element_by_xpath("//*[@id='delete-group-modal']/div/div/div[2]/button[2]").click()
            time.sleep(50)
            #print("Deleted Group ",data.text)
            time.sleep(50)
            temp = temp - count
            print("Temp-->",temp)
            driver.refresh()
        print("----------------------------------------")


