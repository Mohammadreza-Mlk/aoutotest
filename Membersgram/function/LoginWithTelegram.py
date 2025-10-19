from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from appium import webdriver
from typing import Any, Dict
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
# from datetime import datetime 
from function.result_Json import save_to_json

import sys, time,re
sys.path.append("../TelegramAuto")

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.pointer_input import PointerInput
from function.LogOut  import  LogOut

def LoginWithTelegram(driver):
     
    PhoneNumberInput = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.EditText[@resource-id="gram.members.android:id/etNumberHint"]')
    PhoneNumberInput.click()
    sleep(0.5)
    PhoneNumberCountryCode = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.EditText[@resource-id="gram.members.android:id/et_country_code"]')
    PhoneNumberCountryCode.send_keys("1")
    sleep(0.5)
    PhoneNumberBox = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.EditText[@resource-id="gram.members.android:id/et_phone_number"]')
    PhoneNumberBox.send_keys("6603455472")
    sleep(0.5)
    ContinueButton = driver.find_element(by=AppiumBy.XPATH,
                                         value= '//android.widget.Button[@resource-id="gram.members.android:id/btn_continue"]')
    ContinueButton.click()
    sleep(0.5)
    try:
        driver.implicitly_wait(30)
        CodeInput = driver.find_element(by=AppiumBy.XPATH,
                                         value= '//android.widget.TextView[@text="Enter code"]')
        if CodeInput: 
            driver.press_keycode(3)
            driver.implicitly_wait(30)
            Vidogram = driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@content-desc="Vidogram"]')
            Vidogram.click()
            sleep(5)
            searchIcon = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
            searchIcon.click()
            searchInput = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.EditText[@text="Search"]')
            searchInput.send_keys("Telegram")
            sleep(5) 
            x, y = 300, 500
            driver.tap([(x, y)])
            sleep(5)
            x, y = 500, 1850
            driver.tap([(x, y)])
            time.sleep(1.5)
            Copytext = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.TextView[@text="Copy"]')
            Copytext.click()
          
            sleep(1)
            
            clipboard_text = driver.get_clipboard_text()
            print(f"Clipboard text: {clipboard_text}")
             
            sleep(1)
            
            driver.press_keycode(3)
             
            
            def extract_code(message):
                # استفاده از regex برای پیدا کردن کد عددی 5 رقمی
                match = re.search(r'\b\d{5}\b', message)
                if match:
                    return match.group()
                return None

            # استخراج کدها;

            code = extract_code(clipboard_text)
            driver.set_clipboard_text(code)

            print("کد :", code)
            
            driver.implicitly_wait(30)
            MembersgramApp = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.TextView[@content-desc="Membersgram"]')
            MembersgramApp.click()
            x, y = 490, 1470
            driver.tap([(x, y)])
            driver.implicitly_wait(30)
            NextButton = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button')
            NextButton.click()
            sleep(4)
            driver.implicitly_wait(30)
            StartBot = driver.find_element(by=AppiumBy.XPATH,
                            value='//android.widget.Button[@text="Start"]')
            StartBot.click()
            
            
            
            save_to_json("Login With telegram" ,  "pass ✅")
            time.sleep(1.5)
            
        
    except:
        
       save_to_json("Login With telegram" ,  "failed❌")

         