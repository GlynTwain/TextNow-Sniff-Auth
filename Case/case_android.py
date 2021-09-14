import time

from loguru import logger

from cases.cases_msg import BaseMsg
from configuration.сapabilities import CapsDevice
from configuration.key import msg_key

from tools.appium_actions import exist_element_by_xpath


class Android(BaseMsg):
    def __init__(self, caps: CapsDevice = None, my_sms: classmethod = None):
        super().__init__(caps)
        self.key_button = msg_key['Телеграмм']
        self.my_sms = my_sms
        self.driver = None
        logger.add(f'log/session/{caps.get_uuid()}_{my_sms.num}log-all_tg.log', format="{time} {level} {message}",
                   rotation='10 MB', compression='zip')

    def _start_button(self) -> None:
        time.sleep(7)

        if exist_element_by_xpath(self.driver, self.key_button['Начать']):
            self._tap(element='Начать')
        time.sleep(2)
        if exist_element_by_xpath(self.driver, self.key_button['Start']):
            self._tap(element='Start')

    def _send_code(self, code) -> None:
        i = 1
        for c in code:
            self._send(
                f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                f"/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                f".widget.FrameLayout/android.widget.FrameLayout["
                f"2]/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android"
                f".widget.LinearLayout/android.widget.EditText[{i}]", c)
            i += 1

    def _checking_permissions(self) -> None:
        """Проверяе существование и даёт разрешение"""

        # 1-о окно от телеги, 2-а разрешения на звонки
        permissions_list = [self.key_button['Даны_не_все_разрешения_ОК'], msg_key['Системное']['Разрешить'],
                            msg_key['Системное']['Разрешить']]
        for this_permissions in permissions_list:
            time.sleep(1)
            if len(self.driver.find_elements_by_xpath(this_permissions)) > 0:
                self.driver.find_element_by_xpath(this_permissions).click()

    def action(self, fname: str, lname: str) -> bool:
        """Кейс регистрации одного аккаунта в телеграмм"""
        self.driver = super().init_driver()  # Создание сессии драйвера
        self.driver.implicitly_wait(2)  # Ожидание запуска приложения

        try:
            self._start_button()
            time.sleep(2)
            self._start_button()
        except Exception as e:
            logger.error(f"Ошибка на стартовой кнопке - {e}")
            return False

        self._checking_permissions()
        time.sleep(2)

        self.driver.find_element_by_xpath(self.key_button['Код_Страны']).clear()
        self._send(self.key_button['Код_Страны'], self.my_sms.country_code_num)

        self._checking_permissions()

        self.driver.find_element_by_xpath(self.key_button['Телефон']).clear()
        self._send(self.key_button['Телефон'], self.my_sms.num)  # my_sms.get_number()

        self._tap('Готово')
        self._checking_permissions()

        time.sleep(5)
        # 'TW'
        if exist_element_by_xpath(self.driver, self.key_button['Алерт_Говна']):
            logger.info('Номер заблокирован или превышено кол-во попыток')
            return False
        elif exist_element_by_xpath(self.driver, self.key_button['v_Звонок']):
            logger.info('Отправка кода через звонок, ожидание 3 минуты')
            time.sleep(190)
            logger.info('Прошло 3 минуты, ')
            code = self.my_sms.get_code()
            logger.info(code)
            if code is None or exist_element_by_xpath(self.driver, self.key_button['Код_не_пришел']):
                logger.debug(f"СМС с комдом не пришла")
                return False
            self._send_code(code)

        else:
            logger.info('Ввод кода доступен сразу')
            time.sleep(2)
            code = self.my_sms.get_code()
            logger.info(f"Код из СМС : {code}")
            if code is None or exist_element_by_xpath(self.driver, self.key_button['Код_не_пришел']): return False
            self._send_code(code)

        self._tap('Готово')

        time.sleep(5)

        # Обработка двухфакторной аутентификации путём перебора стандратных паролей
        # if exist_element_by_xpath(self.driver, self.key_button['TW']): test()

        self.driver.find_element_by_xpath(self.key_button['Имя']).clear()
        self._send(self.key_button['Имя'], fname)

        self.driver.find_element_by_xpath(self.key_button['Фамилия']).clear()
        self._send(self.key_button['Фамилия'], lname)

        self._tap('Готово')
        return True
