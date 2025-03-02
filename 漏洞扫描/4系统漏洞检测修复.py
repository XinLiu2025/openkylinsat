import yaml
import os
import time
import json
import datetime
from threading import Thread
import requests
import socket
from threading import BoundedSemaphore
from tkinter import *
from tkinter import messagebox
import tkinter as Tk
#锁
Max=1
s=BoundedSemaphore(Max)
#读取总yaml文件
Result=[]
ThreadList=[]
Hostname=socket.gethostname()
rootpassword=""
def SystemMain(i):
    # 打开poc yaml
    print(IndexSystemPocs[i]+'  running!')
    with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/'+IndexSystemPocs[i]+'/'+IndexSystemPocs[i]+'.yaml', 'r', encoding='utf-8') as f:
        PocsYaml = yaml.load(f.read(), Loader=yaml.FullLoader)
    #poc inter
    SystemPocsInter=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] != None:
        SystemPocsInter=PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    SystemPocsInterArgs=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] != None:
        for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            SystemPocsInterArgs=SystemPocsInterArgs+j+' '

    SystemPocsName=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] != None:
        SystemPocsName=PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    SystemPocArgs=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args'] != None:
            for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
                SystemPocArgs = SystemPocArgs + j +' '

    SystemPocMaxTime=''
    if PocsYaml['SiteRequests']['Implement']['ExpireTime'] != None:
        SystemPocMaxTime=PocsYaml['SiteRequests']['Implement']['ExpireTime']
    #执行exploit
    #print(
        #'timeout ' + str(SystemPocMaxTime) + ' ' + SystemPocsInter + ' ' + SystemPocsInterArgs + ' ./data/SystemPocs/' +
        #IndexSystemPocs[i] + '/' + SystemPocsName + ' ' + SystemPocArgs + ' 1> ' + './data/SystemPocs/' +
        #IndexSystemPocs[i] + '/result.txt' + ' 2>&1')
    instrucions='timeout ' + str(SystemPocMaxTime) + ' ' + SystemPocsInter + ' ' + SystemPocsInterArgs + ' /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' +IndexSystemPocs[i] + '/' + SystemPocsName + ' ' + SystemPocArgs + ' 1> ' + '/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' +IndexSystemPocs[i] + '/result.txt' + ' 2>&1'
    CommandReultStrs=''
    testPoc=-1
    #判断是否需要执行其他命令进行数据检查
    otherIns=0
    #exlpoit结果判断判断
    for j in range(0,len(PocsYaml['SiteRequests']['Implement']['Inter'])):
        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] =='<<' :
            #执行<<
            #<<:后的命令没有\n
            otherIns=1
            instrucions=instrucions+';'+(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:]+' >> '+'/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' + IndexSystemPocs[i] + '/tmp.txt')
        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>.':
            #执行<.
            time.sleep(0)
        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>?':
            #print(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:])
            #执行<?
            if otherIns==1:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' + IndexSystemPocs[i] + '/tmp.txt') as file:
                    CommandReultStrs = file.read()
                os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' + IndexSystemPocs[i] + '/tmp.txt')
                testPoc=CommandReultStrs.find(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:])
            else:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/'+IndexSystemPocs[i]+'/result.txt',errors='ignore') as file:
                    if PocsYaml['SiteRequests']['Implement']['Inter'][j][3:] in file.read():
                        testPoc=1
    if testPoc == -1 :
        res_dict = {IndexSystemPocs[i]: {'CheckResult': 0,'solution': PocsYaml['SiteInfo']['Solution'] }}
        Result.append(res_dict)
    else:
        s.acquire()
        print('repairing '+IndexSystemPocs[i])
        res_dict = {IndexSystemPocs[i]: {'CheckResult': 0,'solution': PocsYaml['SiteInfo']['Solution'] }}
        Result.append(res_dict)
        os.system('echo "'+rootpassword+'" | sudo -S python3 ./data/SystemPocs/'+IndexSystemPocs[i]+'/solution.py')
        print('finishing '+IndexSystemPocs[i])
        s.release()
    #print('')
    print(IndexSystemPocs[i]+'  finishing!')
    os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/'+IndexSystemPocs[i]+'/result.txt')

def printinfo():
    print("\n系统漏洞扫描修复成功，检查结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/漏洞扫描/result’目录下")


Result.append({'CheckTime':str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname':Hostname})

# 获得root密码
def show_entry_fields():
    global rootpassword
    rootpassword = e1.get()
    messagebox.showinfo("提示", "root密码已输入，请确认。")
    master.destroy()

# 创建主窗口
master = Tk.Tk()
master.title("系统漏洞修复")

# 设置窗口大小和位置
width = 650
height = 150
screenwidth = master.winfo_screenwidth()
screenheight = master.winfo_screenheight()
position_right = int((screenwidth - width) / 2)
position_down = int((screenheight - height) / 2)
master.geometry(f'{width}x{height}+{position_right}+{position_down}')

# 设置字体大小
font_size = 28

# 创建标签和输入框
Label = Tk.Label(master, text="root 密码", font=('Helvetica', font_size))
Label.grid(row=0, column=0, sticky='e', padx=5, pady=10)

e1 = Tk.Entry(master, show='*', font=('Helvetica', font_size))  # 使用 show 参数隐藏输入的密码
e1.grid(row=0, column=1, padx=5, pady=10)

# 创建按钮
Button = Tk.Button(master, text='系统漏洞修复', command=show_entry_fields, font=('Helvetica', font_size))
Button.grid(row=1, column=0, columnspan=2, pady=20)

# 启动主循环
master.mainloop()

with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/SystemPocs.yaml', 'r', encoding='utf-8') as f:
    IndexSystemPocs = yaml.load(f.read(), Loader=yaml.FullLoader)
for k in range(0, len(IndexSystemPocs)):
    t = Thread(target=SystemMain, args=(k,))
    ThreadList.append(t)
    t.start()
for j in ThreadList:
    j.join()
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/系统漏洞检测修复报告.json', 'w', encoding='utf-8') as f:
   json.dump(Result, f,ensure_ascii=False, indent=4)
printinfo()
