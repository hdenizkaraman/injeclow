import os
import subprocess
import time


class World:
    def __init__(self, usbkey_act):
        self.posibilites = {
            "sb ks || on": 'enable_usbkey',
            "sb ks || off": 'disable_usbkey',
        }
        self.usbkey_activation = True

    # def usbkey_timer(self):
    #     while True:
    #         if self.usbkey_activation == False:
    #             starttime = int(time.perf_counter())
    #             while True:
    #                 nowtime = int(time.perf_counter())
    #                 if nowtime-starttime==140: break
    #                 else: pass
    #             self.disable_usbkey()
    #             self.enable_usbkey()
    #         else: break
        

    def enable_usbkey(self):
        self.usbkey_activation = True
        subprocess.Popen("servisatk.exe", shell=True)
        # self.usbkey_timer()

    def disable_usbkey(self):
        self.usbkey_activation = False
        subprocess.Popen("taskkill /f /IM servisatk.exe /t", shell=True)
        subprocess.Popen("taskkill /f /IM explorer.exe & start explorer", shell=True)