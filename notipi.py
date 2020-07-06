from win10toast import ToastNotifier
import platform
import subprocess
toaster = ToastNotifier()
from time import sleep
def ping(Host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    return subprocess.call(['ping', param, '1', Host], creationflags =0x00000008) == 0
f=open('res/ip.txt','r')
ip = str(f.read())
ver=True
while True:    
    while ver:
        if ping(ip):
            ver = False
            toaster.show_toast("RaspberryPi","The Pi is enabled. ",duration = 5, icon_path = 'res/rpi.ico') 
        sleep(5)
    while ver==False:        
        if ping(ip)==False:
            ver = True
        sleep(5)
