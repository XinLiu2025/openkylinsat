import os
import datetime
import socket
import re
import requests
import json
import yaml
import time

def load_yaml_file(file_path):
    """
    加载 YAML 文件并返回数据

    Args:
        file_path (str): YAML 文件的路径

    Returns:
        加载后的 YAML 数据
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print("Format: {}".format(type(data)))
        return data

def initialize_yaml_data():
    """
    初始化 YAML 数据

    Returns:
        初始化后的 YAML 数据字典
    """
    yaml_data = {}
    # 获取当前系统时间
    current_time = datetime.datetime.now()
    yaml_data['CheckTime'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # 获取主机名称
    host_name = socket.gethostname()
    yaml_data['Hostname'] = host_name
    # 设置扫描类型
    yaml_data['ScanType'] = 'BaseLine'
    # 初始化扫描项目结果列表
    yaml_data['ScanProjects'] = []
    return yaml_data

def write_yaml(yaml_data):
    """
    将 YAML 数据写入指定文件

    Args:
        yaml_data (dict): 要写入的 YAML 数据
    """
    yaml_file_path = "../result/repair_data.yaml"
    with open(yaml_file_path, "w", encoding="utf-8") as file:
        yaml.dump(yaml_data, file, allow_unicode=True)

def print_project_info(project_info):
    """
    打印项目信息

    Args:
        project_info (dict): 项目信息字典
    """
    print("打印本次检查项目信息")
    print("FormatVer: {}".format(project_info['FormatVer']))
    print("Id: {}".format(project_info['Id']))
    print("Belong: {}".format(project_info['Belong']))
    print("SiteInfo: {}".format(project_info['SiteInfo']['Name']))
    print("Power : {}".format(project_info['Power']))

def create_command(exec_array, password):
    """
    构造命令字符串

    Args:
        exec_array (list): 执行命令数组
        password (str): 密码

    Returns:
        构造好的命令字符串
    """
    if not exec_array or len(exec_array) == 0:
        print("执行数组为空")
        return None
    command = "echo '{}' | sudo -S bash {}".format(password, exec_array[0]['Exec'])
    if exec_array[0]['Args']:
        for arg in exec_array[0]['Args']:
            command += f' {arg}'
    print("命令为: {}".format(command))
    return command

def get_result(data):
    """
    从数据中获取结果

    Args:
        data (dict): 输入数据

    Returns:
        整理后的结果字典
    """
    result_dict = {}
    result_dict['Id'] = data['Id']
    result_dict['SiteInfo_Name'] = data['SiteInfo']['Name']
    result_dict['Result'] = data['SiteRequests']['implement']['Result']
    result_dict['JudgeResult'] = data['JudgeResult']
    result_dict['Belong'] = data['Belong']
    result_dict['Advice'] = data['Advice']
    return result_dict

def read_data(base_line_all_project, password):
    """
    读取数据并处理

    Args:
        base_line_all_project (dict): 包含配置信息的字典
        password (str): 密码
    """
    global yaml_data
    base_path = base_line_all_project['ConfigFilePrefix']
    project_paths = base_line_all_project['ExplorerItems']
    for item in project_paths:
        config_file = item['ConfigFile']
        print("v={}".format(config_file))
        print(base_path + config_file)
        data = load_yaml_file(base_path + config_file)
        print_project_info(data)
        command = "sudo bash {}".format(data['SiteRequests']['implement']['ImArray'][0]['Exec'])
        file_descriptor = os.popen(command)
        output = file_descriptor.read().strip()
        file_descriptor.close()
        temp_res = output.split()
        print("tmp_res:", temp_res)
        if len(temp_res) >= 3:
            data['SiteRequests']['implement']['Result'] = temp_res[2]
        else:
            print("命令执行结果不符合预期: ", temp_res)
        data['Advice'] = temp_res[0] + temp_res[1]
        data['JudgeResult'] = temp_res[3]
        Res = get_result(data)
        yaml_data['ScanProjects'].append(Res)

def recover():
    """
    执行恢复操作
    """
    data = load_yaml_file('../repair_code/repair.yaml')
    print(data)
    global password
    password = data['Passwd']
    base_path = data['ConfigFilePrefix']
    project_paths = data['ExplorerItems']
    for item in project_paths:
        file_path = item['ConfigFile']
        os.system("sudo bash " + base_path + file_path)
        print(file_path)

def generate_report():
    """
    生成报告
    """
    global yaml_data
    # 加载基线配置文件
    base_line_all_project = load_yaml_file('../data/BaseLine/BaseLine.yaml')
    # 初始化 YAML 数据
    yaml_data = {}
    current_time = datetime.datetime.now()
    yaml_data['CheckTime'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    host_name = socket.gethostname()
    yaml_data['Hostname'] = host_name
    yaml_data['ScanType'] = 'BaseLine'
    yaml_data['ScanProjects'] = []
    # 读取文件路径配置
    print("读取文件")
    read_data(base_line_all_project, '')
    # 写入数据
    print("开始写入")
    write_yaml(yaml_data)
    # 发送数据
    test_file = open('../result/repair_data.yaml', "r", encoding="utf-8")
    generate_dict = yaml.load(test_file, Loader=yaml.FullLoader)
    generate_json = json.dumps(generate_dict, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)
    with open("../result/repair_data.json", 'w', encoding="utf-8") as write_file:
        write_file.write(generate_json)
    files = {'file': open('../result/repair_data.json', 'r')}
    url = 'http://0.0.0.0:9001/openkylin_repair_res_report/'
    with open('../result/repair_data.json','r') as file:
        post_string = json.loads(file.read())
        post_string = json.dumps(post_string)
        requests.post(url, data=post_string)

if __name__ == '__main__':
    recover()
    generate_report()