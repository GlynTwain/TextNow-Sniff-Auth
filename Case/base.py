from appium import webdriver as AppiumDriver
from config.сapabilities import CapsDeviceA


class BaseAction:
    def __init__(self, caps,key):
        self.caps = caps
        self.driver = None
        self.key_button=key

    def init_driver(self) -> object:
        """Создает драйвер апиума, запускает приложение """
        try:
            self.driver = AppiumDriver.Remote(
                command_executor="http://hub-cloud.browserstack.com/wd/hub",
                desired_capabilities=self.caps.desired_capabilities
            )
        except Exception as e:
            print(f"\nОшибка старта драйвера - {e}\n")
        return self.driver

    def tap_id(self, element: str) -> None:
        """Нажатие"""
        self.driver.find_element_by_id(self.key_button[element]).click()

    def tap_xpath(self, element: str) -> None:
        """Нажатие"""
        self.driver.find_element_by_xpath(self.key_button[element]).click()

    def send_android(self, element: str, text: str) -> None:
        """Ввод в поле ввода"""
        self.driver.find_element_by_xpath(self.key_button[element]).send_keys(text)

    def send_ios(self, element: str, text: str) -> None:
        """Ввод в поле ввода"""
        self.driver.find_element_by_id(self.key_button[element]).send_keys(text)
