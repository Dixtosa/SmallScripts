#Name:            DesktopMover.py
#Author:          Dixtosa
#Date started:    08.01.2OO9
#website:         Dixtosa.wordpress.com

import os, time

print "Desired desktop path (example: D:\\desktop\n):"
des=raw_input("Enter Path:")
des=des.replace("/","\\")

F='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /V Desktop /T REG_SZ /D '+des+' /F'
S='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /V Desktop /T REG_SZ /D '+des+' /F'

os.system(F)
time.sleep(1)
os.system(S)
time.sleep(1)
os.system("taskkill /f /im explorer.exe")

print "Wait until explorer.exe loads. or just restart :D"

os.system("explorer.exe")
raw_input("Done...")