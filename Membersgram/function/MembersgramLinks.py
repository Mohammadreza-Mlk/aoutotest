from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
sys.path.append("../Membersgram")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from function.result_Json import save_to_json



def privacy(driver):
    try :
            Membersgram = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@content-desc='Membersgram'])")
            Membersgram.click()
       
    except:
        print("")
    driver.implicitly_wait(5)
    Home_Tab = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"gram.members.android:id/navigation_bar_item_icon_view\"])[1]")
    Home_Tab.click()
    Profile_Tab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
    Profile_Tab.click()
    Setting_section = driver.find_element(by=AppiumBy.XPATH, value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"gram.members.android:id/rvProfile\"]/android.view.ViewGroup[7]")
    Setting_section.click()
    Privacy_Policy =  driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Privacy Policy\"]")
    Privacy_Policy.click()

    time.sleep(5)
    # driver.execute_script('mobile:longClickGesture', {'x':100, 'y':600, 'duration':1000})
      
    driver.execute_script("mobile: dragGesture", {
          "startX": 61,"startY": 300,
          "endX": 570,"endY": 1200,
          "duration": 15500  
      })
    time.sleep(1)
    driver.tap([(119, 200)])

    clipboard_text = driver.get_clipboard_text()
    print("Clipboard text:", clipboard_text)
    
    
    my_text = """Membersgram Privacy Policy
    1. Introduction
    This privacy policy is established to inform you that our product is an unofficial Telegram app. To log in to Membersgram, you must proceed through Telegram login (You can read the terms of use of Telegram in the https://telegram.org/tos )

    1.1. Terms of Service
    This Privacy Policy forms part of our Terms of Service, which describes the terms under which you use our Services and which are available at https://Membersgram.com/tos. This Privacy Policy should therefore be read in conjunction with those terms."""

    # حذف فاصله‌ها و newlineها برای مقایسه
    def normalize_text(text):
        return "".join(text.split())

    if normalize_text(clipboard_text) == normalize_text(my_text):
        save_to_json("PrivacyLink" ,  "pass ✅")
    else:
        save_to_json("PrivacyLink" ,  "failed❌")
    driver.press_keycode(187)  
    time.sleep(0.7)
    closeAllApp = driver.find_element(by=AppiumBy.ID, value="com.sec.android.app.launcher:id/clear_all_button")
    closeAllApp.click()
      
    
 

def TermOfService(driver):
    try :
            Membersgram = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@content-desc='Membersgram'])")
            Membersgram.click()
       
    except:
        print("")
    driver.implicitly_wait(5)
    Home_Tab = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"gram.members.android:id/navigation_bar_item_icon_view\"])[1]")
    Home_Tab.click()    
    Profile_Tab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
    Profile_Tab.click()
    Setting_section = driver.find_element(by=AppiumBy.XPATH, value="//androidx.recyclerview.widget.RecyclerView[@resource-id=\"gram.members.android:id/rvProfile\"]/android.view.ViewGroup[7]")
    Setting_section.click()
    Term_Of_Service = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Terms of Services\"]")
    Term_Of_Service.click()

    time.sleep(5)
      
    driver.execute_script("mobile: dragGesture", {
          "startX": 45,"startY": 400,
          "endX": 500,"endY": 460,
          "duration": 1500  
      })
    driver.tap([(124, 318)])

    clipboard_text = driver.get_clipboard_text()
    print("Clipboard text:", clipboard_text)
    if clipboard_text == "By signing up for Membersgram, you accept our Privacy Policy and agree not to:" : 
        # The `save_to_json("TermOfServiceLink" ,  "pass ✅")` function call is saving the result of
        # the test for the "Terms of Service" link verification to a JSON file.
        save_to_json("TermOfServiceLink" ,  "pass ✅")
            
    else:
        save_to_json("TermOfServiceLink" ,  "failed❌")
    driver.press_keycode(187)  # Keycode 187 = APP_SWITCH
    time.sleep(0.7)
    closeAllApp = driver.find_element(by=AppiumBy.ID, value="com.sec.android.app.launcher:id/clear_all_button")
    closeAllApp.click()













def Support(driver):
    try :
            Membersgram = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@content-desc='Membersgram'])")
            Membersgram.click()
       
    except:
        print()
 
    driver.implicitly_wait(5)
    Home_Tab = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"gram.members.android:id/navigation_bar_item_icon_view\"])[1]")
    Home_Tab.click()
    Profile_Tab = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Profile")
    Profile_Tab.click()
    Support = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Support\"]")
    Support.click()
    time.sleep(5)   
    driver.execute_script("mobile: dragGesture", {
          "startX": 857,"startY": 418,
          "endX": 500,"endY": 418,
          "duration": 1500  
      })
    time.sleep(0.7)
    driver.tap([(119, 300)])

    clipboard_text = driver.get_clipboard_text()
    print("Clipboard text:", clipboard_text)
    if clipboard_text == "?How can we help you" : 
        save_to_json("ُsupportLink" ,  "pass ✅") 
                
    else :
        save_to_json("SupportLink" ,  "failed❌")


    driver.press_keycode(187)  
    time.sleep(0.7)
    closeAllApp = driver.find_element(by=AppiumBy.ID, value="com.sec.android.app.launcher:id/clear_all_button")
    closeAllApp.click()
    try :
            time.sleep(1)
            Membersgram = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@content-desc='Membersgram'])")
            Membersgram.click()
       
    except:
        print()
    