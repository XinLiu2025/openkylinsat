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

# 锁
Max = 1
s = BoundedSemaphore(Max)

# 读取总 yaml 文件
Result = []
ThreadList = []

# 主机名
Hostname = socket.gethostname()
rootpassword = ""

def kernel_main(index):
    """
    内核漏洞检测的主要函数

    Args:
        index (int): 索引
    """
    print(IndexKernelPocs[index] +'  running!')
    with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/' + IndexKernelPocs[index] + '.yaml', 'r', encoding='utf-8') as f:
        poc_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)

    # poc 相关参数处理
    kernel_pocs_inter = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] is not None:
        kernel_pocs_inter = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    kernel_pocs_inter_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] is not None:
        for j in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            kernel_pocs_inter_args += j +' '

    kernel_pocs_name = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] is not None:
        kernel_pocs_name = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    kernel_poc_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args'] is not None:
        for j in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
            kernel_poc_args += j +' '

    kernel_poc_max_time = ''
    if poc_yaml['SiteRequests']['Implement']['ExpireTime'] is not None:
        kernel_poc_max_time = poc_yaml['SiteRequests']['Implement']['ExpireTime']

    # 执行 exploit
    instructions = (
            'timeout'+ str(kernel_poc_max_time) +' '+ kernel_pocs_inter +' '+ kernel_pocs_inter_args +'./data/KernelPocs/' +
            IndexKernelPocs[index] +'/' + kernel_pocs_name +' '+ kernel_poc_args +' 1> '+ './data/KernelPocs/' +
            IndexKernelPocs[index] +'/result.txt'+ ' 2>&1'
    )
    command_result_strs = ''
    test_poc = -1

    # 判断是否需要执行其他命令进行数据检查
    other_ins = 0

    # exploit 结果判断
    for j in range(0, len(poc_yaml['SiteRequests']['Implement']['Inter'])):
        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '<<':
            # 执行 <<
            other_ins = 1
            instructions += ';'+ (poc_yaml['SiteRequests']['Implement']['Inter'][j][3:] +' >> '+ './data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt')

        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>.':
            # 执行 <.
            time.sleep(0)

        if poc_yaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>?':
            # 执行 <?
            if other_ins == 1:
                os.system(instructions)
                with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt') as file:
                    command_result_strs = file.read()
                os.system('rm./data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt')
                test_poc = command_result_strs.find(poc_yaml['SiteRequests']['Implement']['Inter'][j][3:])
            else:
                os.system(instructions)
                with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/result.txt', errors='ignore') as file:
                    if poc_yaml['SiteRequests']['Implement']['Inter'][j][3:] in file.read():
                        test_poc = 1

    if test_poc == -1:
        res_dict = {IndexKernelPocs[index]: {'CheckResult': 0,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
    else:
        s.acquire()
        res_dict = {IndexKernelPocs[index]: {'CheckResult': 1,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
        os.system(
            'echo "' + rootpassword + '" | sudo -S python3./data/SystemPocs/' + IndexKernelPocs[index] + '/solution.py')
        s.release()

    print(IndexKernelPocs[index] +'  finishing!')
    os.system('rm./data/KernelPocs/' + IndexKernelPocs[index] + '/result.txt')

Result.append({'CheckTime': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname': Hostname})

def center_window(width, height, root):
    """
    使窗口居中显示

    Args:
        width (int): 窗口宽度
        height (int): 窗口高度
        root (Tk 对象): Tkinter 窗口对象
    """
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/2))
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# 创建 Tkinter 窗口
root = tk.Tk()
root.title("内核漏洞修复")

# 设置窗口大小和位置
width = 700
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# 创建标签和输入框
label = tk.Label(root, text="root 密码", font=("Helvetica", 28))
label.grid(row=0, column=0, sticky="w")

e1 = tk.Entry(root, show="*", font=("Helvetica", 28))
e1.grid(row=0, column=1)

def show_entry_fields():
    """
    处理输入 root 密码并关闭窗口
    """
    global rootpassword
    rootpassword = e1.get()
    messagebox.showinfo("提示", "root 密码已输入，请确认。")
    root.destroy()

# 创建按钮
button = tk.Button(root, text="内核漏洞修复", command=show_entry_fields, font=("Helvetica", 18))
button.grid(row=3, column=0, sticky="w", pady=10)

# 启动 Tkinter 事件循环
root.mainloop()

with open('./data/KernelPocs/KernelPocs.yaml', 'r', encoding='utf-8') as f:
    IndexKernelPocs = yaml.load(f.read(), Loader=yaml.FullLoader)

for k in range(0, len(IndexKernelPocs)):
    t = Thread(target=kernel_main, args=(k,))
    ThreadList.append(t)
    t.start()

for j in ThreadList:
    j.join()

# 保存结果到本地文件
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测修复报告.json', 'w', encoding='utf-8') as f:
    json.dump(Result, f, indent=4, ensure_ascii=False)