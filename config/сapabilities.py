class CapsDevice:
    def __init__(self, uuid: str, port: str):
        self.desired_capabilities = {
            "browserstack.user": "gfhjbkn_Kioue8",
            "browserstack.key": "4zC9YYaxPfqAqH4qdPtv",
            'browserstack.networkLogs': True,

            # Set URL of the application under test
            "app": "bs://3fc42329993b6bfeb766d156fe41df4536bbf9f8",

            # Specify device and os_version for testing
            "device": "Samsung Galaxy S20",#
            "os_version": "10.0",#

            # Set other BrowserStack capabilities
            "project": "TextNow Auth",#
            "build": "Python Android", #
            "name": "first_test"
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
