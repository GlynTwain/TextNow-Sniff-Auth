from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_cap = {
    # Set your access credentials
    "browserstack.user": "gfhjbkn_Kioue8",
    "browserstack.key": "4zC9YYaxPfqAqH4qdPtv",

    # Set URL of the application under test
    "app": "bs://<app-id>",

    # Specify device and os_version for testing
    "device": "Samsung Galaxy S20",
    "os_version": "10.0",

    # Set other BrowserStack capabilities
    "project": "First Python project",
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

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()