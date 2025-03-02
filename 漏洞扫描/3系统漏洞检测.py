import yaml
import os
import time
import json
import datetime
from threading import Thread
import requests
import socket
#读取总yaml文件
Result=[]
ThreadList=[]

Hostname=socket.gethostname()
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
    instrucions='timeout ' + str(SystemPocMaxTime) + ' ' + SystemPocsInter + ' ' + SystemPocsInterArgs + '/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' +IndexSystemPocs[i] + '/' + SystemPocsName + ' ' + SystemPocArgs + ' 1> ' + '/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/' +IndexSystemPocs[i] + '/result.txt' + ' 2>&1'
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
        res_dict = {IndexSystemPocs[i]: {'CheckResult': 1,'solution': PocsYaml['SiteInfo']['Solution'] }}
        Result.append(res_dict)
    #print('')
    print(IndexSystemPocs[i]+'  finishing!')
    os.system('rm /home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/'+IndexSystemPocs[i]+'/result.txt')

def printinfo():
    print("\n系统漏洞扫描成功，检查结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/漏洞扫描/result’目录下")

Result.append({'CheckTime':str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
Result.append({'Hostname':Hostname})
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/data/SystemPocs/SystemPocs.yaml', 'r', encoding='utf-8') as f:
    IndexSystemPocs = yaml.load(f.read(), Loader=yaml.FullLoader)
for k in range(0, len(IndexSystemPocs)):
    t = Thread(target=SystemMain, args=(k,))
    ThreadList.append(t)
    t.start()
for j in ThreadList:
    j.join()
with open('/home/nuc/桌面/NUC_openkylin/漏洞扫描/result/系统漏洞检测报告.json', 'w', encoding='utf-8') as f:
   json.dump(Result, f,ensure_ascii=False, indent=4)
printinfo()

