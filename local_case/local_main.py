from config.сapabilities import CapsDevice
from appium import webdriver
import time

user = {
    'login': 'omerozcp1987:',
    'password': 'WW93dq93',
    'token': None,
}
blus = {
    'login': 'gfhjbkn_Kioue8:',
    'password': '4zC9YYaxPfqAqH4qdPtv',

}


def exist_element_by_id(driver, path):
    """Проверка на существование элемента"""
    if len(driver.find_elements_id(path)) > 0:
        print('Есть элемент на экране')
        return True
    else:
        print('Нет элемента на экране')
        return False


caps = CapsDevice(uuid='emulator-5554', port='5901')
while True:
    driver = webdriver.Remote(command_executor=caps.get_address(), desired_capabilities=caps.desired_capabilities)

    time.sleep(2)
    driver.find_element_by_id('com.enflick.android.TextNow:id/sign_up_button').click()
    time.sleep(1)
    if len(driver.find_elements_by_id('com.enflick.android.TextNow:id/title_sign_up')) > 0:
        driver.find_element_by_id('com.enflick.android.TextNow:id/login_prompt').click()
        time.sleep(1)

    driver.find_element_by_id('com.enflick.android.TextNow:id/login_email_button').click()
    time.sleep(1)
    # driver.find_element_by_id('com.enflick.android.TextNow:id/email_text_box').click()
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText').send_keys(
        user['login'])
    time.sleep(1)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.EditText').send_keys(
        user['password'])
    time.sleep(1)
    driver.find_element_by_id('com.enflick.android.TextNow:id/authorization_button').click()




