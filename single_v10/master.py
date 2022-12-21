import os
import subprocess

class World:
    def __init__(self):
        self.posibilites = {
            "sb ks || on": 'enable_usbkey',
            "sb ks || off": 'disable_usbkey',
        }

    def enable_usbkey(self):
        return os.system("servisatk.exe")

    def disable_usbkey(self):
        return os.system("taskkill /f /IM servisatk.exe /t")