
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
import platform
import sys
import subprocess
f=open('res/ip.txt','r')
ip = str(f.read())
app = QApplication(sys.argv)
from time import sleep
def ping(Host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    return subprocess.call(['ping', param, '1', Host], creationflags =0x00000008) == 0
trayIcon=QSystemTrayIcon(QIcon('res/rpi2.ico'), parent = app)
trayIcon.show()
ver = True
while True:    
    while ver:
        if ping(ip):
            ver = False
            trayIcon.setIcon(QIcon("res/rpi.ico"))
        sleep(1)
    while ver==False:        
        if ping(ip)==False:
            ver = True
            trayIcon.setIcon(QIcon("res/rpi2.ico"))
        sleep(1)

