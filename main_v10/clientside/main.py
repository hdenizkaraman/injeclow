import win32com.client

class WebConnection():
    pass

class MainArchit():
    def __init__(self):
        pass

    def usbcontrol(self):
        usblist = []
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            pass

mainarchit = MainArchit()
mainarchit.usbcontrol()