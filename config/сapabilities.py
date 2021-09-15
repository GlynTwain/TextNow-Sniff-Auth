import random


class CapsDeviceA:
    def __init__(self):
        device,os_version = self.rand_device()
        print(device + ' '+os_version)

        self.desired_capabilities = {
            "browserstack.user": "gfhjbkn_Kioue8",  #
            "browserstack.key": "4zC9YYaxPfqAqH4qdPtv",  #
            'browserstack.networkLogs': True,

            # Set URL of the application under test
            "app": "bs://3fc42329993b6bfeb766d156fe41df4536bbf9f8",

            # Specify device and os_version for testing
            "device": device,  #
            "os_version": os_version,  #

            # Set other BrowserStack capabilities
            "project": "TextNow Auth",  #
            "build": "Python Android",  #
            "name": "auth"
        }

    def rand_device(self):
        devices = [["Samsung Galaxy S21", "11.0"], ["Samsung Galaxy S20", "10.0"], ["Motorola Moto G9 Play", "10.0"], ["OnePlus 9", "11.0"]]
        this_device = random.choice(devices)
        return this_device[0], this_device[1]
