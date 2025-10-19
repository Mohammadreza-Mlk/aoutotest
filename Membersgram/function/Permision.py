import time
from appium.webdriver.common.appiumby import AppiumBy
from watchlog import Watchlog
watchlog_instance = Watchlog()
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append("../Membersgram")
from function.result_Json import save_to_json

 
def Permission(driver):
     
    
    try:
        driver.implicitly_wait(5)

        AllowButton = driver.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_button"]')
        AllowButton.click()
        time.sleep(2)
        save_to_json("Permision for androind 13" ,  "pass ✅")
       
    except:
            print("")
            save_to_json("Permision for android 13" ,  "failed❌")
    
