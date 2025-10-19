from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
sys.path.append("../Membersgram")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # اضافه کردن پوشه Membersgram

# from function.JsonWrite import create_or_overwrite_result
from function.Register import Register
from function.Login import LoginEmail
from function.LogOut import LogOut
from function.OrderMemberByCoin import OrderMemberByCoin
from function.OrderViewBycoin import OrderViewByCoin
from function.TransferCoin import TransferCoin
from function.CloseAddAccountFullScreeen import CloseAddAccountFullScreeen
from function.Permision import Permission
from function.LoginWithTelegram import LoginWithTelegram
from function.MembersgramLinks import privacy, TermOfService, Support
from function.AddaccountFullScreen import AddAccountFullScreen
from function.OrderMemberByPurchase import OrderMemberByPurchase
from function.OrderViewByPurchase import OrderViewByPurchase
from function.AddTelegramAccount import AddAccount
 
# from function.result import res
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    'udid' :'RZ8NA1L8W1X',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'
 
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

file_path = "TestResult.json"
 
time.sleep(2)

Permission(driver)
time.sleep(2)
time.sleep(1.5)
Register(driver)
time.sleep(0.5)
CloseAddAccountFullScreeen(driver)
time.sleep(1.5)
LogOut(driver)
time.sleep(1.5)
LoginWithTelegram(driver)
time.sleep(1.5)
Support(driver)
time.sleep(2)
Support(driver)
time.sleep(2)
privacy(driver)
time.sleep(2)
TermOfService(driver)
LogOut(driver)
time.sleep(1.5)
LoginEmail(driver)
time.sleep(1.5)

OrderMemberByCoin(driver)
time.sleep(1.5)
OrderViewByCoin(driver)
time.sleep(2)
TransferCoin(driver)
time.sleep(1.5)
 














# time.sleep(1.5)
# OrderViewByPurchase(driver)
# time.sleep(1)
# OrderMemberByPurchase(driver)
# time.sleep(1.5)