import yaml
import os
import time
import json
import datetime
from threading import Thread
import requests
import socket
from threading import BoundedSemaphore
import tkinter as tk
from tkinter import messagebox

# 锁
Max = 1
s = BoundedSemaphore(Max)

# 读取总 yaml 文件
Result = []
ThreadList = []

# 主机名
Hostname = socket.gethostname()
rootpassword = ""

def system_main(index):
    """
    系统漏洞检测的主要函数

    Args:
        index (int): 索引
    """
    print(IndexSystemPocs[index] +'  running!')
    with open('./data/SystemPocs/' + IndexSystemPocs[index] + '/' + IndexSystemPocs[index] + '.yaml', 'r', encoding='utf-8') as f:
        poc_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)

    # poc 相关参数处理
    system_pocs_inter = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] is not None:
        system_pocs_inter = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    system_pocs_inter_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] is not None:
        for j in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            system_pocs_inter_args += j +' '

    system_pocs_name = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] is not None:
        system_pocs_name = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    system_poc_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args'] is not None:
        for j in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
            system_poc_args += j +' '

    system_poc_max_time = ''
    if poc_yaml['SiteRequests']['Implement']['ExpireTime'] is not None:
        system_poc_max_time = poc_yaml['SiteRequests']['Implement']['ExpireTime']

    # 执行 exploit
    instructions = 'timeout'+ str(system_poc_max_time) +' '+ system_pocs_inter +' '+ system_pocs_inter_args +'./data/SystemPocs/' + IndexSystemPocs[index] +'/' + system_pocs_name +' '+ system_poc_args +' 1> '+ './data/SystemPocs/' + IndexSystemPocs[index] +'/result.txt'+ ' 2>&1'
    command_result_strs = ''
    test_poc = -1

    # 判断是否需要执行其他命令进行数据检查
    other_ins = 0

    # exploit 结果判断
    for j in range(0, len(poc_yaml['SiteRequests']['Implement']['Inter'])):
        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '<<':
            # 执行 <<
            other_ins = 1
            instructions += ';'+ (poc_yaml['SiteRequests']['Implement']['Inter'][j][3:] +' >> '+ './data/SystemPocs/' + IndexSystemPocs[index] + '/tmp.txt')
        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>.':
            # 执行 <.
            time.sleep(0)
        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>?':
            # 执行 <?
            if other_ins == 1:
                os.system(instructions)
                with open('./data/SystemPocs/' + IndexSystemPocs[index] + '/tmp.txt') as file:
                    command_result_strs = file.read()
                os.system('rm./data/SystemPocs/' + IndexSystemPocs[index] + '/tmp.txt')
                test_poc = command_result_strs.find(poc_yaml['SiteRequests']['Implement']['Inter'][j][3:])
            else:
                os.system(instructions)
                with open('./data/SystemPocs/' + IndexSystemPocs[index] + '/result.txt', errors='ignore') as file:
                    if poc_yaml['SiteRequests']['Implement']['Inter'][j][3:] in file.read():
                        test_poc = 1

    if test_poc == -1:
        res_dict = {IndexSystemPocs[index]: {'CheckResult': 0,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
    else:
        s.acquire()
        print('repairing '+IndexSystemPocs[index])
        res_dict = {IndexSystemPocs[index]: {'CheckResult': 0,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
        os.system('echo "'+rootpassword+'" | sudo -S python3./data/SystemPocs/'+IndexSystemPocs[index]+'/solution.py')
        print('finishing '+IndexSystemPocs[index])
        s.release()

    print(IndexSystemPocs[index] +'  finishing!')
    os.system('rm./data/SystemPocs/' + IndexSystemPocs[index] + '/result.txt')

Result.append({'CheckTime': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname': Hostname})

# 获得 root 密码
def show_entry_fields():
    """
    获取输入的 root 密码并关闭窗口
    """
    global rootpassword
    rootpassword = e1.get()
    messagebox.showinfo("提示", "root 密码已输入，请确认。")
    master.destroy()

# 创建主窗口
master = tk.Tk()
master.title("系统漏洞修复")

# 设置窗口大小和位置
width = 800
height = 200
screenwidth = master.winfo_screenwidth()
screenheight = master.winfo_screenheight()
position_right = int((screenwidth - width) / 2)
position_down = int((screenheight - height) / 2)
master.geometry(f'{width}x{height}+{position_right}+{position_down}')

# 设置字体大小
font_size = 28

# 创建标签和输入框
label = tk.Label(master, text="root 密码", font=('Helvetica', font_size))
label.grid(row=0, column=0, sticky='e', padx=5, pady=10)

e1 = tk.Entry(master, show='*', font=('Helvetica', font_size))  # 使用 show 参数隐藏输入的密码
e1.grid(row=0, column=1, padx=5, pady=10)

# 创建按钮
button = tk.Button(master, text='系统漏洞修复', command=show_entry_fields, font=('Helvetica', font_size))
button.grid(row=1, column=0, columnspan=2, pady=20)

# 启动主循环
master.mainloop()

with open('./data/SystemPocs/SystemPocs.yaml', 'r', encoding='utf-8') as f:
    IndexSystemPocs = yaml.load(f.read(), Loader=yaml.FullLoader)

for k in range(0, len(IndexSystemPocs)):
    t = Thread(target=system_main, args=(k,))
    ThreadList.append(t)
    t.start()

for j in ThreadList:
    j.join()

with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/系统漏洞检测修复报告.json', 'w', encoding='utf-8') as f:
    json.dump(Result, f, ensure_ascii=False, indent=4)