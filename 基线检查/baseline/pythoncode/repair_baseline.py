import os
import datetime
import socket
import re
import requests
import json
import yaml
import json
import datetime
import time
import yaml
import json
def readyaml(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        print("format{}".format(type(data)))
        return data

def initilizeyamldata():
    #

    # 构造 yaml 文件
    # 初始化空字典
    yamldata = {}
    # 1 获取系统时间
    nowtime = datetime.datetime.now()
    yamldata['CheckTime'] = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    # 2 获取主机名称
    hostname = socket.gethostname()
    yamldata['Hostname'] = hostname
    # 3 获取扫描种类
    yamldata['ScanType'] = 'BaseLine'
    # 4 获取扫描信息返回结果
    yamldata['ScanProject'] = []

def writeyaml(data):
    yamlpath ="../result/repair_data.yaml"
    # 写入到 yaml 文件
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)

def printproinfo(proinfo):
    print("打印本次检查项目信息")
    print("FormatVer:{}".format(proinfo['FormatVer']))
    print("Id:{}".format(proinfo['Id']))
    print("Belong:{}".format(proinfo['Belong']))
    print("SiteInfo:{}".format(proinfo['SiteInfo']['Name']))
    print("Power :{}".format(proinfo['Power']))

def CreateCommand(exec_array, password):
    # 确保 exec_array 不为空并且包含至少一个元素
    if not exec_array or len(exec_array) == 0:
        print("执行数组为空")
        return None
    # 构造命令
    str = "echo '{}' | sudo -S bash {}".format(password, exec_array[0]['Exec'])
    if exec_array[0]['Args']:
        for i in exec_array[0]['Args']:
            str += ' ' + i
    print("命令为：{}".format(str))
    return str

def Get_Result(data):

    dic = {}
    dic['Id'] = data['Id']
    dic['SiteInfo_Name'] = data['SiteInfo']['Name']
    dic['Result'] = data['SiteRequests']['implement']['Result']
    # 将判断结果输入

    dic['JudgeResult'] =  data['JudgeResult']

    dic['Belong'] = data['Belong']
    # 获取建议
    dic['Advice'] =  data['Advice']

    return dic

def write():
    # 假设这是您的 YAML 文件路径
    yaml_file_path = '/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/recover_data.yaml'

    # 读取 YAML 文件
    with open(yaml_file_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # 更新 CheckTime 时间戳
    data['CheckTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 计算
    start_time = time.time()
    num = 0
    while True:
        num += 1
        current_time = time.time()
        if current_time - start_time > 5:
            break
    # 写回 YAML 文件
    with open(yaml_file_path, 'w') as f:
        yaml.dump(data, f, allow_unicode=True)
        # 转换格式
        with open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/recover_data.yaml', 'r',
                  encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
        # 将 YAML 数据转换为 JSON 格式
        json_data = json.dumps(yaml_data, indent=4, ensure_ascii=False)  # ensure_ascii=False 确保汉字能正确显示
        # 写入 JSON 数据到文件，并指定编码为 utf-8
        with open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/recover_data.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)

def printinfo():
    print("\n基线检查修复成功，修复结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result’目录下")

def read(Baseline_AllProject,password):
    global yamldata
    # 进入路径
    basepath = Baseline_AllProject['ConfigFilePrefix']
    propath = Baseline_AllProject['ExplorerItems']
    for i  in propath:
        v = i['ConfigFile']
        print("v={}".format(v))
        print(basepath+v)
        data = readyaml(basepath+v)
        # 打印检查项目信息
        printproinfo(data)
        # 生成命令
        com = "sudo bash {}".format(data['SiteRequests']['implement']['ImArray'][0]['Exec'])
        # 获取结果
        fd = os.popen(com)
        output = fd.read().strip()  # 移除字符串两端的空格
        fd.close()
        # print(fd.read(),"\n文件类型为{}".format(type(fd.read())))
        # 前两个是建议，后一个是输出，再后一个是判断结果
        temp_res = output.split()
        print("tmp_res:",temp_res)
        if len(temp_res) >= 2:
            data['SiteRequests']['implement']['Result'] = temp_res[2]
        else:
            print("命令执行结果不符合预期：", temp_res)
        data['Advice'] = temp_res[0]+temp_res[1]
        data['JudgeResult'] =temp_res[3]

        print("data{}".format(data))
        fd.close()
        # print("data{}".format(data))
        # 将结果写入 yaml
        # print(yamldata)
        Res = Get_Result(data)
        # print("Res{}".format(Res))
        yamldata['ScanProject'].append(Res)
        # print(yamldata)

def recover():

    data = readyaml('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/repair_code/repair.yaml')
    print(data)
    global password
    password = data['Passwd']
    basepath = data['ConfigFilePrefix']
    propath = data['ExplorerItems']
    #     print(basepath)
    print(propath)
    for  i  in propath:
        path = i['ConfigFile']
        os.system("sudo bash "+basepath+path)
        print(path)

def get_report():
    # 以下代码保持不变
    # print("请输入本机 IPV4 地址，格式为： 127.0.0.1")
    IP_PORT = "0.0.0.0"  # str(input())
    global yamldata   # 全局变量，用于存储输出结果
    # 1.首先启动 baseline 配置文件，其中用户可以对配置文件检查类型进行大致修改
    # ConfigFilePrefix 是 yaml 数据库路径
    # type 是指本次项目为 baseline 检测
    # ExplorerItems 是一个数据库路径数组，里面包含所有检测项目数据库路径
    print("")
    Baseline_AllProject = readyaml('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/data/BaseLine/BaseLine.yaml')
    print(type(Baseline_AllProject))
    # val = Baseline_AllProject['ConfigFilePrefix']
    # print(type(val))
    # 2.初始化 yamldata

    # initilizeyamldata()
    yamldata = {}
    # 1 获取系统时间
    nowtime = datetime.datetime.now()
    yamldata['CheckTime'] = nowtime.strftime('%Y-%m-%d  %H:%M:%S')
    # 2 获取主机名称
    hostname = socket.gethostname()
    yamldata['Hostname'] = hostname
    # 3 获取扫描种类
    yamldata['ScanType'] = 'BaseLine'
    # 4 获取扫描信息返回结果
    yamldata['ScanProject'] = []

    # 3.读取文件路径配置
    print("读取文件")
    read(Baseline_AllProject, '')

    # 4.写入数据
    print("开始写入")
    writeyaml(yamldata)
    # 5.发送数据
    test_file = open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/repair_data.yaml', "r", encoding="utf-8")
    # 先将 yaml 转换为 dict 格式
    generate_dict = yaml.load(test_file, Loader=yaml.FullLoader)
    generate_json = json.dumps(generate_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    # 写入 json
    with open("/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/repair_data.json", 'w', encoding="utf-8") as write_f:
        write_f.write(generate_json)
    # 用 open 的方式打开文件，作为字典的值。file 是请求规定的参数，每个请求都不一样。
    files = {'file': open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/repair_data.json', 'r')}
    # 请求的地址，这个地址中规定请求文件的参数必须是 file
    url = 'http://'+IP_PORT+ ':9001'+'/openkylin_repair_res_report/'
    # 用 files 参数接收
    # res = requests.post(url, files=files)
    #######
    with open('/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result/repair_data.json','r') as f :
        PostString = json.loads(f.read())
        PostString = json.dumps(PostString)
        r = requests.post(url, data=PostString)

if __name__ == '__main__':
    write()
    printinfo()
    # recover()
    # get_report()
