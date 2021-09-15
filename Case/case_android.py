import time

from Case.base import BaseAction
from config.key import un_key
from config.сapabilities import CapsDeviceA


class Android(BaseAction):
    def __init__(self, caps: CapsDeviceA = None, user: dict = None):
        super().__init__(caps,un_key['Android'])
        # self.key_button = un_key['Android']
        self.user = user
        self.driver = None

    def action(self,login,passw) -> None:
        """Кейс регистрации одного аккаунта в телеграмм"""
        self.driver = super().init_driver()  # Создание сессии драйвера
        self.driver.implicitly_wait(2)  # Ожидание запуска приложения

        self.tap_id('Зарегестрироваться')

        time.sleep(1)
        if len(self.driver.find_elements_by_id('com.enflick.android.TextNow:id/title_sign_up')) > 0:
            self.tap_id('Залогиниться')
            time.sleep(1)

        self.tap_id('Войти_по_почте')
        time.sleep(1)
        self.send_android('Поле_ввода_логина', login)
        time.sleep(1)
        self.send_android('Поле_ввода_пароля', passw)
        time.sleep(1)

        self.tap_id('Войти')
        time.sleep(8)

        self.driver.quit()
