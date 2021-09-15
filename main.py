from Case.case_android import Android
from config.сapabilities import CapsDeviceA
from log_handler import get_token

config = {"Платформа": "Android", "Логин": "omerozcp1987", "Пароль": "WW93dq93" }

while True:
    try:
        print('Начинаю процесс авторизации...')
        my_caps = CapsDeviceA()
        case = Android(caps=my_caps)
        case.action(login=config['Логин'], passw=config['Пароль'])

        # Запрос Network логов, обработка и сохранение
        get_token()
    except:
        print('Что то пошло не так ... (')