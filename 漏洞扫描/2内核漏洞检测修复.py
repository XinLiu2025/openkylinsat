import yaml
import os
import time
import json
import datetime
import socket
from threading import Thread
from tkinter import *
from threading import BoundedSemaphore
import tkinter as tk
from tkinter import messagebox
# from 漏洞扫描.内核漏洞检测 import Hostname
Hostname= socket.gethostname()
# 锁
Max = 1
s = BoundedSemaphore(Max)

# 读取总yaml文件
Result = []
ThreadList = []

rootpassword = ""


def KernelMain(i):
    # 打开poc yaml
    print(IndexKernelPocs[i] + '  running!')
    with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/' + IndexKernelPocs[i] + '.yaml', 'r', encoding='utf-8') as f:
        PocsYaml = yaml.load(f.read(), Loader=yaml.FullLoader)

    # poc inter
    KernelPocsInter = ''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] is not None:
        KernelPocsInter = PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    KernelPocsInterArgs = ''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] is not None:
        for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            KernelPocsInterArgs = KernelPocsInterArgs + j + ' '

    KernelPocsName = ''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] is not None:
        KernelPocsName = PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    KernelPocArgs = ''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args'] is not None:
        for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
            KernelPocArgs = KernelPocArgs + j + ' '

    KernelPocMaxTime = ''
    if PocsYaml['SiteRequests']['Implement']['ExpireTime'] is not None:
        KernelPocMaxTime = PocsYaml['SiteRequests']['Implement']['ExpireTime']

    # 执行exploit
    instrucions = (
            'timeout ' + str(KernelPocMaxTime) + ' ' + KernelPocsInter + ' ' + KernelPocsInterArgs + ' /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' +
            IndexKernelPocs[i] + '/' + KernelPocsName + ' ' + KernelPocArgs + ' 1> ' + './data/KernelPocs/' +
            IndexKernelPocs[i] + '/result.txt' + ' 2>&1'
    )
    CommandReultStrs = ''
    testPoc = -1

    # 判断是否需要执行其他命令进行数据检查
    otherIns = 0

    # exploit结果判断
    for j in range(0, len(PocsYaml['SiteRequests']['Implement']['Inter'])):
        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '<<':
            # 执行<<
            otherIns = 1
            instrucions = instrucions + ';' + (PocsYaml['SiteRequests']['Implement']['Inter'][j][3:] + ' >> ' + '/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt')

        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>.':
            # 执行<.
            time.sleep(0)

        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>?':
            # 执行<?
            if otherIns == 1:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt') as file:
                    CommandReultStrs = file.read()
                os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt')
                testPoc = CommandReultStrs.find(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:])
            else:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/result.txt', errors='ignore') as file:
                    if PocsYaml['SiteRequests']['Implement']['Inter'][j][3:] in file.read():
                        testPoc = 1

    if testPoc == -1:
        res_dict = {IndexKernelPocs[i]: {'CheckResult': 0, 'solution': PocsYaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
    else:
        s.acquire()
        res_dict = {IndexKernelPocs[i]: {'CheckResult': 1, 'solution': PocsYaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
        os.system(
            'echo "' + rootpassword + '" | sudo -S python3 ./data/SystemPocs/' + IndexKernelPocs[i] + '/solution.py')
        s.release()

    print(IndexKernelPocs[i] + '  finishing!')
    os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/result.txt')
def printinfo():
    print("\n内核漏洞扫描修复成功，结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/漏洞扫描/result’目录下")

Result.append({'CheckTime': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname': Hostname})


# 定义center_window函数
def center_window(width, height, root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

import tkinter as tk
from tkinter import messagebox

# 创建Tkinter窗口
root = tk.Tk()
root.title("内核漏洞修复")

# 设置窗口大小和位置
width = 650
height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)
root.geometry(f'{width}x{height}+{x}+{y}')


# 创建标签和输入框
label = tk.Label(root, text="root 密码", font=("Helvetica", 28))
label.grid(row=0, column=0, sticky='e', padx=5, pady=10)

e1 = tk.Entry(root, show="*", font=("Helvetica", 28))
e1.grid(row=0, column=1, padx=5, pady=10)
# 显示根密码输入框和按钮
def show_entry_fields():
    global rootpassword
    rootpassword = e1.get()
    messagebox.showinfo("提示", "root密码已输入，请确认。")
    root.destroy()

# 创建按钮
button = tk.Button(root, text="内核漏洞修复", command=show_entry_fields, font=("Helvetica", 28))
button.grid(row=1, column=0, columnspan=2, pady=20)

# 启动Tkinter事件循环
root.mainloop()
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/KernelPocs.yaml', 'r', encoding='utf-8') as f:
    IndexKernelPocs = yaml.load(f.read(), Loader=yaml.FullLoader)

for k in range(0, len(IndexKernelPocs)):
    t = Thread(target=KernelMain, args=(k,))
    ThreadList.append(t)
    t.start()

for j in ThreadList:
    j.join()

# 保存结果到本地文件
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测修复报告.json', 'w', encoding='utf-8') as f:
    json.dump(Result, f, indent=4, ensure_ascii=False)
printinfo()

