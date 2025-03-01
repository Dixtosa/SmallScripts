#Desktop MOVER.py v_1.2
 
 
import os,time
print "Desktop M0VER By dixtosa"
#############
print "sad ginda ro iyos desktopi?\n"
print "ExamPle: D:\\suratebi\n"
des=raw_input("Enter Path:")
des=des.replace("/","\\")
 
F='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /V Desktop /T REG_SZ /D '+des+' /F'
S='reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /V Desktop /T REG_SZ /D '+des+' /F'
 
 
os.system(F)
time.sleep(0.8)
os.system(S)
time.sleep(0.8)
os.system("taskkill /f /im explorer.exe")
 
print "GMADLOBT ROM IYENEBT CHEM PROGRAMAS. \n gtxovt daicadot manam bolomde chaitvirteba:)"
 
os.system("explorer.exe")
print "vso, morcha., ara ar ginda me tviton gamovirtvebi:) uyure..."
time.sleep(1.2)
sys.Exit()
