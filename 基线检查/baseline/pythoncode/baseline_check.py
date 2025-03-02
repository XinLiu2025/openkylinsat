import os
import datetime
import socket
import re
import requests
import json
import yaml

def readyaml(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        print("format{}".format(type(data)))
        return data

def initilizeyamldata():
    # 构造yaml文件
    # 初始化空字典
    yamldata = {}
    # 1获取系统时间
    nowtime = datetime.datetime.now()
    yamldata['CheckTime'] = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    # 2获取主机名称
    hostname = socket.gethostname()
    yamldata['Hostname'] = hostname
    # 3获取扫描种类
    yamldata['ScanType'] = 'BaseLine'
    # 4获取扫描信息返回结果
    yamldata['ScanProject'] = []
    return yamldata
def printinfo():
    print("基线检查成功，修复结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result’目录下")
def writeyaml(data, yamlpath):
    # 写入到yaml文件
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)

def printproinfo(proinfo):
    print("打印本次检查项目信息")
    print("FormatVer:{}".format(proinfo['FormatVer']))
    print("Id:{}".format(proinfo['Id']))
    print("Belong:{}".format(proinfo['Belong']))
    print("SiteInfo:{}".format(proinfo['SiteInfo']['Name']))
    print("Power :{}".format(proinfo['Power']))

def CreateCommand(val, password):
    # 构造sudo命令
    str = f"echo {password} | sudo -S bash {val[0]['Exec']}"
    if val[0]['Args']:
        for i in val[0]['Args']:
            str += ' ' + i
    print(f"命令为{str}结束")
    return str
def printinfo():
    print("\n基线检查成功，检查结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result’目录下")
def Get_Result(data):
    dic = {}
    dic['Id'] = data['Id']
    dic['SiteInfo_Name'] = data['SiteInfo']['Name']
    dic['Result'] = data['SiteRequests']['Implement']['Result']
    # 将判断结果输入
    dic['JudgeResult'] = data['JudgeResult']
    dic['Belong'] = data['Belong']
    # 获取建议
    dic['Advice'] = data['Advice']
    return dic

def read(Baseline_AllProject, passwd):
    yamldata = initilizeyamldata()
    basepath = Baseline_AllProject['ConfigFilePrefix']
    propath = Baseline_AllProject['ExplorerItems']
    password = passwd

    for i in propath:
        v = i['ConfigFile']
        print(f"v={v}")
        print(basepath + v)
        data = readyaml(basepath + v)
        # 打印检查项目信息
        printproinfo(data)
        # 生成命令
        com = CreateCommand(data['SiteRequests']['Implement']['ImArray'], password)
        # 获取结果
        fd = os.popen(com)
        result = fd.read().strip().split()
        fd.close()

        # 确保result列表不为空
        if result:
            data['SiteRequests']['Implement']['Result'] = result[0]
            data['Advice'] = ' '.join(result[1:2])  # 假设建议在前两个元素中
            data['JudgeResult'] = result[2]  # 假设判断结果在第三个元素中
        else:
            data['SiteRequests']['Implement']['Result'] = 'No result'
            data['Advice'] = 'No advice'
            data['JudgeResult'] = 'No judge result'

        # 将结果写入yaml
        Res = Get_Result(data)
        yamldata['ScanProject'].append(Res)

    return yamldata

if __name__ == '__main__':
    print("请输入管理员密码:")
    passwd = 'nucss123'
    yamldata = read(readyaml('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/data/BaseLine/BaseLine.yaml'), passwd)
    writeyaml(yamldata, "/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/data.yaml")
    # 转换为JSON并写入
    with open("/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/data.json", 'w', encoding="utf-8") as write_f:
        json.dump(yamldata, write_f, ensure_ascii=False, indent=4)
    printinfo()
