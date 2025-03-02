import yaml
import os
import time
import json
import requests
import datetime
import socket
from threading import Thread
#读取总yaml文件
Result=[]
ThreadList=[]
Hostname= socket.gethostname()
def KernelMain(i):
    # 打开poc yaml
    print(IndexKernelPocs[i]+'  running!')
    with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/'+IndexKernelPocs[i]+'/'+IndexKernelPocs[i]+'.yaml', 'r', encoding='utf-8') as f:
        PocsYaml = yaml.load(f.read(), Loader=yaml.FullLoader)
    #poc inter
    KernelPocsInter=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter'] != None:
        KernelPocsInter=PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Inter']

    KernelPocsInterArgs=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs'] != None:
        for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['InterArgs']:
            KernelPocsInterArgs=KernelPocsInterArgs+j+' '

    KernelPocsName=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec'] != None:
        KernelPocsName=PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Exec']

    KernelPocArgs=''
    if PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args'] != None:
            for j in PocsYaml['SiteRequests']['Implement']['ImArray'][0]['Args']:
                KernelPocArgs = KernelPocArgs + j +' '

    KernelPocMaxTime=''
    if PocsYaml['SiteRequests']['Implement']['ExpireTime'] != None:
        KernelPocMaxTime=PocsYaml['SiteRequests']['Implement']['ExpireTime']
    #执行exploit
    #print(
        #'timeout ' + str(KernelPocMaxTime) + ' ' + KernelPocsInter + ' ' + KernelPocsInterArgs + ' ./data/KernelPocs/' +
        #IndexKernelPocs[i] + '/' + KernelPocsName + ' ' + KernelPocArgs + ' 1> ' + './data/KernelPocs/' +
        #IndexKernelPocs[i] + '/result.txt' + ' 2>&1')
    instrucions=(
        'timeout ' + str(KernelPocMaxTime) + ' ' + KernelPocsInter + ' ' + KernelPocsInterArgs + ' /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' +
        IndexKernelPocs[i] + '/' + KernelPocsName + ' ' + KernelPocArgs + ' 1> ' + '/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' +
        IndexKernelPocs[i] + '/result.txt' + ' 2>&1')
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
            instrucions=instrucions+';'+(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:]+' >> '+'/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt')

        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>.':
            #执行<.
            time.sleep(0)
        if PocsYaml['SiteRequests']['Implement']['Inter'][j][0:2] == '>?':
            #print(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:])
            #执行<?
            if otherIns==1:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt') as file:
                    CommandReultStrs = file.read()
                os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/' + IndexKernelPocs[i] + '/tmp.txt')
                testPoc=CommandReultStrs.find(PocsYaml['SiteRequests']['Implement']['Inter'][j][3:])
            else:
                os.system(instrucions)
                with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/'+IndexKernelPocs[i]+'/result.txt',errors='ignore') as file:
                    if PocsYaml['SiteRequests']['Implement']['Inter'][j][3:] in file.read():
                        testPoc=1
    if testPoc == -1 :
        res_dict = {IndexKernelPocs[i]: {'CheckResult': 0,'solution': PocsYaml['SiteInfo']['Solution'] }}
        Result.append(res_dict)
    else:
        res_dict = {IndexKernelPocs[i]: {'CheckResult': 1,'solution': PocsYaml['SiteInfo']['Solution'] }}
        Result.append(res_dict)
    #print('')
    print(IndexKernelPocs[i]+'  finishing!')
    os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/'+IndexKernelPocs[i]+'/result.txt')
def printinfo():
    print("\n内核漏洞扫描成功，检查结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/漏洞扫描/result’目录下")
Result.append({'CheckTime':str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname': Hostname})
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/KernelPocs/KernelPocs.yaml', 'r', encoding='utf-8') as f:
    IndexKernelPocs = yaml.load(f.read(), Loader=yaml.FullLoader)
for k in range(0,len(IndexKernelPocs)):
    t=Thread(target=KernelMain,args=(k,))
    ThreadList.append(t)
    t.start()
for j in ThreadList:
    j.join()
PostString=json.dumps(Result)
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/内核漏洞检测报告.json', 'w', encoding='utf-8') as f:
    json.dump(Result, f, indent=4, ensure_ascii=False)
printinfo()