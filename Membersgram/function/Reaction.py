

from appium.webdriver.common.appiumby import AppiumBy
  
  
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
from appium import webdriver
from typing import Any, Dict
import json

from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
 


cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'
# desired_caps: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
 


 
 
 
 
 
def react(driver):
    ReactionTab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="React")
    ReactionTab.click()
    time.sleep(1)
    pakageOfReact = driver.find_element(by=AppiumBy.XPATH, value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"gram.members.android:id/rvOrderMemberBundles\"]/android.view.ViewGroup[3]")
    pakageOfReact.click()
    time.sleep(1)
    selectEmoji = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.GridView[@resource-id=\"gram.members.android:id/rvSelectEmoji\"]/android.view.ViewGroup[1]/android.widget.Button")
    selectEmoji.click()
    time.sleep(1)
    NextButton = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Next\"]")
    NextButton.click()
    time.sleep(1)
    LinkInputbox = driver.find_element(by=AppiumBy.ID, value="gram.members.android:id/textInputEditTextUserName")
    LinkInputbox.send_keys("wrongId")
    NextButton = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
    NextButton.click()
    time.sleep(1)
    ErrorLink = driver.find_element(by=AppiumBy.ID, value="gram.members.android:id/textinput_error")
    if ErrorLink :
        
     
        LinkInputbox = driver.find_element(by=AppiumBy.ID, value="gram.members.android:id/textInputEditTextUserName")
        LinkInputbox.send_keys("https://t.me/testpnx1/32")
        NextButton = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        NextButton.click()
        time.sleep(1)
        PayButton = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        PayButton.click()
        time.sleep(1)
        Successful = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Successful payment\"]")
        if Successful :
            GotitButton = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
            GotitButton.click()
            time.sleep(1)

    
    
react(driver)