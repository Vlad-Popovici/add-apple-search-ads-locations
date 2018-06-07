from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#set browser size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome("ADD_PATH_TO_CHROME",chrome_options=chrome_options)
driver.set_window_size(1920, 1080)



#Syntax
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)

#loginto account
search_ads_url  = "https://app.searchads.apple.com/cm/app"
driver.get(search_ads_url)

#account info

account1_user = "YOUR_USERNAME"
account1_pass = "YOUR_PASSWORD"

account2_user = 'YOUR_USERNAME2'
account2_pass = 'YOUR_PASSWORD2'

time.sleep(4)



#locations
test_list = ["Alabama","Alaska","California"]
location_list_1 = ["Alabama","Alaska","California","Colorado","Georgia","Hawaii","Idaho","Kansas","Kentucky","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
location_list_2 = ["Alabama","Alaska","California","Colorado","Georgia","Hawaii","Idaho","Indiana","Kansas","Kentucky","Maine","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]



def Add_Locations(account_name,ad_group_url,list_type):


    #check the account name
    if account_name == 'account1':
        user = account1_user
        passw = account1_pass
    elif account_name == 'account2':
        user = account2_user
        passw = account2_pass
    else:
        print('There is no such account name, sorry.')


    #check the locations lists
    if list_type == 'v1':
        main_list = location_list1
        print(main_list)
    elif list_type == 'v2':
        main_list = location_list2
        print(main_list)
    else:
        print("There is no such list_type")

    #Find element by class and hit sign in, then hit advanced
    frame = driver.find_element_by_id("aid-auth-widget-iFrame")
    driver.switch_to.frame(frame)
    username_field = driver.find_element_by_id("account_name_text_field")
    username_field.click()
    username_field.send_keys(user)
    username_field.send_keys(Keys.RETURN)
    time.sleep(4)

    pass_field = driver.find_element_by_id("password_text_field")
    pass_field.click()
    pass_field.send_keys(passw)
    pass_field.send_keys(Keys.RETURN)
    time.sleep(8)
    
    #Go to ad_group settings
    driver.get(ad_group_url)
    time.sleep(20)
    locations_button = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[3]/div[2]/div[3]/div[1]/button').click()
    
    #main executable
    for i in main_list:
        locations_field = driver.find_element_by_xpath('//*[@id="spc-userlocation"]/div[2]/div/input')
        locations_field.click()
        locations_field.send_keys(i)
        time.sleep(3)
        locations_field.send_keys(Keys.TAB)
    #optional:
    #hit SAVE after all is done
    #save_button = driver.find_element_by_xpath('//*[@id="scm-line-save-button"]').click()

Add_Locations('YOUR_ACCOUNT_NAME','ADGROUP_URL','LOCATION_LIST1')


