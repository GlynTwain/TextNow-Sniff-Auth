import requests
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from log_handler import get_token

user = {
    'login': 'omerozcp1987',
    'password': 'WW93dq93',
    'token': None,
}

desired_cap = {
    # Set your access credentials
    "browserstack.user": "gfhjbkn_Kioue8",
    "browserstack.key": "4zC9YYaxPfqAqH4qdPtv",
    'browserstack.networkLogs': True,

    # Set URL of the application under test
    "app": "bs://3fc42329993b6bfeb766d156fe41df4536bbf9f8",

    # Specify device and os_version for testing
    "device": "Samsung Galaxy S20",
    "os_version": "10.0",

    # Set other BrowserStack capabilities
    "project": "TextNow Auth",
    "build": "Python Android",
    "name": "first_test"
}

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

# Write your custom code here

time.sleep(2)
driver.find_element_by_id('com.enflick.android.TextNow:id/sign_up_button').click()
time.sleep(1)
if len(driver.find_elements_by_id('com.enflick.android.TextNow:id/title_sign_up')) > 0:
    driver.find_element_by_id('com.enflick.android.TextNow:id/login_prompt').click()
    time.sleep(1)

driver.find_element_by_id('com.enflick.android.TextNow:id/login_email_button').click()
time.sleep(1)
# driver.find_element_by_id('com.enflick.android.TextNow:id/email_text_box').click()
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').send_keys(user['login'])
time.sleep(1)
driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText').send_keys(user['password'])
time.sleep(1)
driver.find_element_by_id('com.enflick.android.TextNow:id/authorization_button').click()
time.sleep(10)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()

# Запрос Network логов, обработка и сохранение
get_token()


