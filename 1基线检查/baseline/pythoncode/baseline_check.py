import os
import datetime
import socket
import re
import requests
import json
import yaml

def load_yaml_file(file_name):
    """
    加载 YAML 文件并返回数据

    Args:
        file_name (str): YAML 文件的路径

    Returns:
        加载后的 YAML 数据
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        print("Format: {}".format(type(data)))
        return data

def initialize_yaml_info():
    """
    初始化 YAML 数据

    Returns:
        包含初始化信息的字典
    """
    yaml_info = {}
    # 获取系统当前时间
    current_time = datetime.datetime.now()
    yaml_info['CheckTime'] = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # 获取主机名称
    host_name = socket.gethostname()
    yaml_info['Hostname'] = host_name
    # 设置扫描类型
    yaml_info['ScanType'] = 'BaseLine'
    # 初始化扫描项目结果列表
    yaml_info['ScanProjects'] = []
    return yaml_info

def save_yaml_data(data, file_path):
    """
    将数据写入 YAML 文件

    Args:
        data (dict): 要写入的数据
        file_path (str): 文件路径
    """
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)

def display_project_info(project_info):
    """
    打印检查项目的信息

    Args:
        project_info (dict): 检查项目的信息
    """
    print("打印本次检查项目信息")
    print("FormatVer: {}".format(project_info['FormatVer']))
    print("Id: {}".format(project_info['Id']))
    print("Belong: {}".format(project_info['Belong']))
    print("SiteInfo: {}".format(project_info['SiteInfo']['Name']))
    print("Power : {}".format(project_info['Power']))

def construct_command(value, password):
    """
    构造 sudo 命令

    Args:
        value (dict): 包含执行命令和参数的字典
        password (str): 管理员密码

    Returns:
        构造好的命令字符串
    """
    command = f"echo {password} | sudo -S bash {value[0]['Exec']}"
    if value[0]['Args']:
        for arg in value[0]['Args']:
            command += f' {arg}'
    print(f"命令为: {command} 结束")
    return command

def print_success_message():
    """
    打印基线检查成功的消息
    """
    print("基线检查成功，检查结果报告已保存在‘/home/nuc/桌面/NUC_openkylin/基线检查/baseline/result’目录下")

def obtain_result(data):
    """
    从数据中获取并整理结果

    Args:
        data (dict): 包含检查结果的字典

    Returns:
        整理后的结果字典
    """
    result_dict = {}
    result_dict['Id'] = data['Id']
    result_dict['SiteInfo_Name'] = data['SiteInfo']['Name']
    result_dict['Result'] = data['SiteRequests']['implement']['Result']
    # 处理判断结果
    result_dict['JudgeResult'] = data['JudgeResult']
    result_dict['Belong'] = data['Belong']
    # 获取建议
    result_dict['Advice'] = data['Advice']
    return result_dict

def perform_read(base_line_all_project, password):
    """
    执行读取和处理操作

    Args:
        base_line_all_project (dict): 包含配置文件路径和检查项目的字典
        password (str): 管理员密码

    Returns:
        处理后的 YAML 数据
    """
    yaml_data = initialize_yaml_info()
    base_path = base_line_all_project['ConfigFilePrefix']
    project_paths = base_line_all_project['ExplorerItems']
    password = password

    for item in project_paths:
        config_file = item['ConfigFile']
        print(f"Config File: {config_file}")
        print(base_path + config_file)
        data = load_yaml_file(base_path + config_file)
        # 打印检查项目信息
        display_project_info(data)
        # 生成命令
        command = construct_command(data['SiteRequests']['implement']['ImArray'], password)
        # 获取结果
        fd = os.popen(command)
        result = fd.read().strip().split()
        fd.close()

        # 处理结果为空的情况
        if result:
            data['SiteRequests']['implement']['Result'] = result[0]
            data['Advice'] =' '.join(result[1:2])  # 假设建议在前两个元素中
            data['JudgeResult'] = result[2]  # 假设判断结果在第三个元素中
        else:
            data['SiteRequests']['implement']['Result'] = 'No result'
            data['Advice'] = 'No advice'
            data['JudgeResult'] = 'No judge result'

        # 将结果整理并添加到 YAML 数据中
        result_info = obtain_result(data)
        yaml_data['ScanProjects'].append(result_info)

    return yaml_data

if __name__ == '__main__':
    print("请输入管理员密码:")
    passwd = input()
    yaml_data = perform_read(load_yaml_file('../data/BaseLine/BaseLine.yaml'), passwd)
    save_yaml_data(yaml_data, "../result/data.yaml")
    # 转换为 JSON 并写入
    with open("../result/data.json", 'w', encoding="utf-8") as write_f:
        json.dump(yaml_data, write_f, ensure_ascii=False, indent=4)
    print_success_message()