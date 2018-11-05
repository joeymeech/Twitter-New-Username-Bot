#TwitterBot by: Joey Meech

#Import all of these modules
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
#Put your path here
driver = webdriver.Chrome("/Users/meech/Desktop/chromedriver")




#Fill your information out here in the ''
email = 'example@gmail.com'
password = 'passwordhere'
usernameyouwant = 'username'
osuser = getpass.getuser()

if(1 == 1):
    print('Welcome ' + osuser) 
    print(r"""
#Twitter Bot
  ____                 _                    __  __                _     
 |  _ \       _       | |                  |  \/  |              | |    
 | |_) |_   _(_)      | | ___   ___ _   _  | \  / | ___  ___  ___| |__  
 |  _ <| | | |    _   | |/ _ \ / _ \ | | | | |\/| |/ _ \/ _ \/ __| '_ \ 
 | |_) | |_| |_  | |__| | (_) |  __/ |_| | | |  | |  __/  __/ (__| | | |
 |____/ \__, (_)  \____/ \___/ \___|\__, | |_|  |_|\___|\___|\___|_| |_|
         __/ |                       __/ |                              
        |___/                       |___/                               

                            
    """)                 




time.sleep(3)
#Goes to the twitter login page
driver.get("https://twitter.com/login")
#Selects the username input box and sends the email keys to it
username = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
username.send_keys(email)
#Finds the password input box and sends the password keys to it
passe = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
passe.send_keys(password)
#Finds the button and clicks it to login
clickme = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
clickme.click()
#Changes links, and it goes to the settings page
driver.get("https://twitter.com/settings/account")
#Clears your username
driver.find_element_by_xpath('//*[@id="user_screen_name"]').clear()
#Finds the username input box and sends the keys of the username that you want
newuser = driver.find_element_by_xpath('//*[@id="user_screen_name"]')
newuser.send_keys(usernameyouwant)
#Waits 2 seconds to allow twitter to responds and see if the username is available or taken
time.sleep(2)
#If there is a problem with the username it will start this loop and will only be broken if a error does not come up
while driver.find_elements_by_class_name('problem'):
    #refreshes the page to allow twitter to check again the status of the username
    driver.refresh()
    #Clears out your current username to try again for the new one
    driver.find_element_by_xpath('//*[@id="user_screen_name"]').clear()
    #Finds the username input box and sends the keys of the username that you want
    newuser = driver.find_element_by_xpath('//*[@id="user_screen_name"]')
    newuser.send_keys(usernameyouwant)
    #Waits 2 seconds to allow twitter to responds and see if the username is available or taken
    time.sleep(2)

#If there is no problem and the loop above is broken this will run
else:
    #Waits 2 seconds to allow twitter to responds and see if the username is available or taken
    time.sleep(2)
    #Presses the enter key to change the username
    enter = driver.find_element_by_xpath('//*[@id="user_screen_name"]')
    enter.send_keys(Keys.RETURN)
    #Types your password into the input box so that twitter will allow you to change your username
    sendpass = driver.find_element_by_xpath('//*[@id="auth_password"]')
    sendpass.send_keys(password)
    #Just adding extra time delay in every step when the username is available just to make sure nothing is messed up.
    time.sleep(1)
    #Finds the save password button and clicks it
    clickthis = driver.find_element_by_xpath('//*[@id="save_password"]')
    clickthis.click()
    #Waits 5 seconds before quitting the code to make sure the new username is saved
    time.sleep(5)
    quit()









