class CapsDevice:
    def __init__(self, uuid: str, port: str):
        self.desired_capabilities = {
            "udid": str(uuid),  #
            "platformName": "Android",
            "app": 'builds/Telegram_7.9.0.apk',  # -- Смена взависимости от апк
            "noReset": "true",
            "unicodeKeyboard": "true",
            "useNewWDA": "false",
            "usePrebuiltWDA": "true",
            "automationName": "UiAutomator2",
            "uiautomator2ServerLaunchTimeout": 900000,
            "uiautomator2ServerInstallTimeout": 800000,
            'adbExecTimeout': 100000,
            'maxDuration': 10800,
            'newCommandTimeout': 1000,
            'appWaitPackage':'org.telegram.messenger.web',# -- Смена взависимости от апк
            'appActivity': 'org.telegram.ui.LaunchActivity',# -- Смена взависимости от апк
            'appPackage':'org.telegram.messenger.web',# -- Смена взависимости от апк
            'autoGrantPermissions': 'true',
            'resetKeyboard': 'true',
        }
        self.appium_port = port
        self.appium_id = '127.0.0.1'

    def get_caps(self) -> dict:
        """Капабили под данное устройство"""
        return self.desired_capabilities

    def get_address(self) -> str:
        """Адрес общения для данного устройства"""
        return f'http://{self.appium_id}:{self.appium_port}/wd/hub'

    def get_uuid(self) -> str:
        """Адрес общения для данного устройства"""
        return self.desired_capabilities['udid']
