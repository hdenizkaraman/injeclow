import requests
import lxml
from bs4 import BeautifulSoup, element
import time
import ctypes
import subprocess
import os
import threading

class Contra():
    def __init__(self):
        self.headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        self.activatedlog = []
        self.event = threading.Event()

    def pullcontent(self):
        while True:
            source = BeautifulSoup(requests.get("https://dqtech.pythonanywhere.com/datas/", headers=self.headersparam).content,"lxml")
            activatedones = source.find_all("span", attrs={"id":"1"})
            disabledones = source.find_all("span", attrs={"id":"0"})
            for i in activatedones:
                active = i.text.replace(" ", "")
                if active in self.activatedlog: pass
                else:
                    runcommand = getattr(Contra, active)
                    runcommand(contravolta)
                    self.activatedlog.append(active)
                    print(self.activatedlog)

            for k in disabledones:
                deactive = k.text.replace(" ", "")
                if deactive in self.activatedlog: 
                    runcommand = getattr(Contra, "reverse_"+deactive)
                    runcommand(contravolta)
                    self.activatedlog.remove(deactive)
                    print(self.activatedlog)
                else: pass

    def timer(self):
        timestart = time.time()
        while True:
            if self.event.is_set(): break
            timenow = time.time()
            if int(timenow)-int(timestart)==8: 
                subprocess.Popen("taskkill /f /IM notepad.exe /t", shell=True)
                time.sleep(0.2)
                subprocess.Popen("notepad.exe", shell=True)
                timestart = time.time()
            else: pass

    def ekrankilit(self):
        self.tiktak = threading.Thread(target=Contra().timer, args=[], name="tiktak")
        self.tiktak.start()
        subprocess.Popen("notepad.exe", shell=True)
        return 0

    def reverse_ekrankilit(self):        
        self.event.set()
        self.tiktak.join()
        #! KILL THIS FUCKING THREAD
        #! AND TEST THAT: CAN IT START ANOTHER ACT WHILE THREADING?
        subprocess.Popen("taskkill /f /IM notepad.exe /t",shell=True)
        # subprocess.Popen("taskkill /f /IM explorer.exe & start explorer",shell=True)
        return 0


    def dqopening(self):
        return subprocess.run(["start", "/wait", "cmd", "/K", "echo WELCOME BACK MR. DENQ"], shell=True)

    def reverse_dqopening(self): pass 

contravolta = Contra()
contravolta.pullcontent()