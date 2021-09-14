from appium import webdriver as AppiumDriver
from loguru import logger
from config.сapabilities import CapsDevice
# from tools.appium_actions import tap_element_xpath, send_element_xpath, exist_element_by_xpath
from config.key import un_key


class BaseAction:
    def __init__(self, caps: CapsDevice):
        self.caps = caps
        self.driver = None

    def init_driver(self) -> object:
        """Создает драйвер апиума, запускает приложение """
        try:
            self.driver = AppiumDriver.Remote(
                command_executor="http://hub-cloud.browserstack.com/wd/hub",
                desired_capabilities=self.caps.get_caps()
            )
        except Exception as e:
            logger.error(f"\nОшибка старта драйвера - {e}\n")
        return self.driver

    def _tap_id(self, element: str) -> None:
        """Нажатие"""
        self.driver.find_element_by_id(self.key_button[element]).click()
        logger.info(f'Нажали {element}')

    def _tap_xpath(self, element: str) -> None:
        """Нажатие"""
        self.driver.find_element_by_xpath(self.key_button[element]).click()
        logger.info(f'Нажали {element}')

    def _send_android(self, element: str, text: str) -> None:
        """Ввод в поле ввода"""
        self.driver.find_element_by_xpath(self.key_button[element]).send_keys(text)
        logger.info(f'Ввели {text} в поле ввода')

    def _send_ios(self, element: str, text: str) -> None:
        """Ввод в поле ввода"""
        self.driver.find_element_by_id(self.key_button[element]).send_keys(text)
        logger.info(f'Ввели {text} в поле ввода')
