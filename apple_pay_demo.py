import os
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.options.common.base import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
import time
import base64

API_TOKEN = os.getenv("HS_API_TOKEN")

APPIUM = 'https://appium-dev.headspin.io:443/v0/'+API_TOKEN+'/wd/hub'

#Importing Images and encoding them as base64
with open(r"payButton.png", "rb") as image_file:
    pay_button_base64 = base64.b64encode(image_file.read()).decode("utf-8")

with open(r"assistTouch.png", "rb") as image_file:
    assist_touch_base64 = base64.b64encode(image_file.read()).decode("utf-8")

with open(r"applePay.png", "rb") as image_file:
    apple_pay_base64 = base64.b64encode(image_file.read()).decode("utf-8")

with open(r"confirmApplePay.png", "rb") as image_file:
    confirm_apple_pay_base64 = base64.b64encode(image_file.read()).decode("utf-8")

#When setting the Appium capabilities for find by image you need the image plugin added
#Also, please ensure you are using Appium 2+ since the plugin is not supported below Appium 2.0.0
options = AppiumOptions()
options.load_capabilities({
    "udid": "UDID",
    "automationName": "XCUITest",
    "platformName": "iOS",
    "headspin:assistiveTouch": "enable",
    "headspin:appiumOptions": {
        "version": "2.0.0",
        "plugins": ["images"],
    },
    "browserName": "safari",
})

driver = webdriver.Remote(
    command_executor=APPIUM,
    options=options
)
try:
    wait = WebDriverWait(driver, 10)

    #These settings are for adjusting the sensitivity of the find by image feature
    driver.update_settings({"imageMatchThreshold": "0.2", "fixImageTemplateScale": True})

    #Navigate to the apple pay demo website
    driver.get("https://applepaydemo.apple.com/")

    #Switches to NATIVE_APP context, it will not find the elements by image in a webview context
    driver.switch_to.context("NATIVE_APP")

    time.sleep(1)

    #Clicks the pay button on the apple pay demo page
    pay_button = driver.find_element(By.IMAGE, pay_button_base64)
    pay_button.click()

    #Clicks on the assistive touch button, and will find it anywhere on the page
    assist_touch = driver.find_element(By.IMAGE, assist_touch_base64)
    assist_touch.click()

    #Clicks on apple pay in the assistive touch menu
    apple_pay = driver.find_element(By.IMAGE, apple_pay_base64)
    apple_pay.click()

    #Clicks on confirm apple pay in the assistive touch menu
    confirm_apple_pay = driver.find_element(By.IMAGE, confirm_apple_pay_base64)
    confirm_apple_pay.click()

    #Enters the passcode, when prompted for it
    passcode = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Passcode field")))
    passcode.send_keys("123456")

    time.sleep(5)
finally:
    driver.quit()