# coding: utf-8
import win32com.client
import win32gui
import win32process
import subprocess

WMI = win32com.client.GetObject("winmgmts:") #WMIの取得_windows-managements
processes = WMI.InstancesOf("Win32_Process")
#print(len(processes))

#name_list = []
#for process in processes:
#    if process.Properties_('Name').Value == "gvim.exe":
#        print(process.Properties_('Name').Value)
#        name_list.append(process.Properties_('Name').Value)

id_list = []
for process in processes:
    if process.Properties_('Name').Value == "chrome.exe":
        id_list.append(process.Properties_('ProcessId').Value)
#print(id_list)

shell = win32com.client.Dispatch("Wscript.Shell")
if id_list != []:
    print(id_list[0])
    a = shell.AppActivate(id_list[0])
    print(a)
    #うまく開けなかった場合は、新しく開く
        #うまく切り替わってもfalseを返す場合がある
    if a == False:
        #shell.run("C:\\Program\ Files\ (x86)\\Google\\Chrome\\Application\\chrome.exe")
        subprocess.call("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
else:
    subprocess.call("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
