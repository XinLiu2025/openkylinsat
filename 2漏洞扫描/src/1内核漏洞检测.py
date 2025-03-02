import yaml
import os
import time
import json
import requests
import datetime
import socket
from threading import Thread

# 全局变量
Result = []
ThreadList = []
Hostname = socket.gethostname()

def kernel_main(index):
    """
    内核漏洞检测的主要函数

    Args:
        index (int): 索引
    """
    print(IndexKernelPocs[index] +'  running!')
    with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/' + IndexKernelPocs[index] + '.yaml', 'r', encoding='utf-8') as f:
        poc_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)

    kernel_pocs_inter = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] is not None:
        kernel_pocs_inter = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    kernel_pocs_inter_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] is not None:
        for arg in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            kernel_pocs_inter_args += arg +' '

    kernel_pocs_name = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] is not None:
        kernel_pocs_name = poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    kernel_poc_args = ''
    if poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args'] is not None:
        for arg in poc_yaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
            kernel_poc_args += arg +' '

    kernel_poc_max_time = ''
    if poc_yaml['SiteRequests']['Implement']['ExpireTime'] is not None:
        kernel_poc_max_time = poc_yaml['SiteRequests']['Implement']['ExpireTime']

    # 执行 exploit
    instructions = (
            'timeout'+ str(kernel_poc_max_time) +' '+ kernel_pocs_inter +' '+ kernel_pocs_inter_args +'./data/KernelPocs/' +
            IndexKernelPocs[index] +'/' + kernel_pocs_name +' '+ kernel_poc_args +' 1> '+ './data/KernelPocs/' +
            IndexKernelPocs[index] +'/result.txt'+ ' 2>&1')

    command_result_strs = ''
    test_poc = -1
    other_ins = 0

    for inter_item in poc_yaml['SiteRequests']['Implement']['Inter']:
        if inter_item[0:2] == '<<':
            other_ins = 1
            instructions += ';'+ (inter_item[3:] +' >> '+ './data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt')

        if inter_item[0:2] == '>.':
            time.sleep(0)

        if inter_item[0:2] == '>?':
            if other_ins == 1:
                os.system(instructions)
                with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt') as file:
                    command_result_strs = file.read()
                os.system('rm./data/KernelPocs/' + IndexKernelPocs[index] + '/tmp.txt')
                test_poc = command_result_strs.find(inter_item[3:])
            else:
                os.system(instructions)
                with open('./data/KernelPocs/' + IndexKernelPocs[index] + '/result.txt', errors='ignore') as file:
                    if inter_item[3:] in file.read():
                        test_poc = 1

    if test_poc == -1:
        res_dict = {IndexKernelPocs[index]: {'CheckResult': 0,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)
    else:
        res_dict = {IndexKernelPocs[index]: {'CheckResult': 1,'solution': poc_yaml['SiteInfo']['Solution']}}
        Result.append(res_dict)

    print(IndexKernelPocs[index] +'  finishing!')
    os.system('rm./data/KernelPocs/' + IndexKernelPocs[index] + '/result.txt')

Result.append({'CheckTime': str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname': Hostname})

with open('./data/KernelPocs/KernelPocs.yaml', 'r', encoding='utf-8') as f:
    IndexKernelPocs = yaml.load(f.read(), Loader=yaml.FullLoader)

for k in range(len(IndexKernelPocs)):
    thread = Thread(target=kernel_main, args=(k,))
    ThreadList.append(thread)
    thread.start()

for thread in ThreadList:
    thread.join()

post_string = json.dumps(Result)
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测报告.json', 'w', encoding='utf-8') as f:
    json.dump(Result, f, indent=4, ensure_ascii=False)