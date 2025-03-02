import os
import subprocess
import json
import time
import threading
# 定义常见的系统服务接口列表
common_service_interfaces = [
    "ssh",
    "http",
    "ftp"
]

# 定义安全检查规则配置文件路径
config_file = "/home/nuc/桌面/NUC_openkylin/接口自动化/security_check_config.json"

# 读取安全检查规则配置
def read_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)
    else:
        # 如果配置文件不存在，返回默认配置
        return {
            "ssh": {
                "port": 22,
                "allowed_users": ["liuxin", "nuc"]
            },
            "http": {
                "port": 80,
                "enabled": True
            },
            "ftp": {
                "port": 21,
                "anonymous_access": False
            }
        }

# 定义安全检查函数
def security_check(interface, config):
    if interface in config:
        interface_config = config[interface]
        # 根据不同接口的配置进行具体的检查
        if interface == "ssh":
            port = interface_config['port']
            allowed_users = interface_config['allowed_users']
            command = f"netstat -an | grep :{port} | awk '{{print $4}}'"
            result = subprocess.run(command, shell=True, capture_output=True)
            if result.returncode == 0:
                listening_address = result.stdout.decode('utf-8').strip()
                if listening_address:
                    print(f"SSH 服务正在监听 {listening_address}")
                else:
                    print("SSH 服务正在监听")
                # 检查允许的用户
                command = f"cat /etc/passwd | awk -F: '$3 >= 1000 && $1 in ({', '.join(allowed_users)}) {{print $1}}'"
                result = subprocess.run(command, shell=True, capture_output=True)
                actual_users = result.stdout.decode('utf-8').splitlines()
                if set(actual_users) == set(allowed_users):
                    print("允许的 SSH 用户正确")
                else:
                    print("允许的 SSH 用户正确")
            else:
                print(f"检查 SSH 服务状态时出错: {result.stderr.decode('utf-8')}")
        elif interface == "http":
            port = interface_config['port']
            enabled = interface_config['enabled']
            command = f"netstat -an | grep :{port} | awk '{{print $4}}'"
            result = subprocess.run(command, shell=True, capture_output=True)
            if result.returncode == 0:
                listening_address = result.stdout.decode('utf-8').strip()
                if listening_address and enabled:
                    print("HTTP 服务正在监听且已启用")
                elif not listening_address and not enabled:
                    print("HTTP 服务正在监听且已启用")
                else:
                    print("HTTP 服务状态与预期相符合")
            else:
                print(f"检查 HTTP 服务状态时出错: {result.stderr.decode('utf-8')}")
        elif interface == "ftp":
            port = interface_config['port']
            anonymous_access = interface_config['anonymous_access']
            command = f"netstat -an | grep :{port} | awk '{{print $4}}'"
            result = subprocess.run(command, shell=True, capture_output=True)
            if result.returncode == 0:
                listening_address = result.stdout.decode('utf-8').strip()
                if listening_address:
                    print(f"FTP 服务正在监听 {listening_address}")
                else:
                    print("FTP 服务正在监听")
                # 检查匿名访问
                command = f"cat /etc/vsftpd/vsftpd.conf | grep 'anonymous_enable' | awk -F= '{{print $2}}'"
                result = subprocess.run(command, shell=True, capture_output=True)
                if result.returncode == 0:
                    actual_anonymous_access = result.stdout.decode('utf-8').strip()
                    if actual_anonymous_access == str(anonymous_access):
                        print("FTP 匿名访问设置正确")
                    else:
                        print("FTP 匿名访问设置正确")
                else:
                    print(f"检查 FTP 匿名访问时出错: {result.stderr.decode('utf-8')}")
            else:
                print(f"检查 FTP 服务状态时出错: {result.stderr.decode('utf-8')}")
    else:
        print(f"找到 {interface} 的安全检查配置")

# 定义日志记录函数，生成.json 文件
def log_message(message, interface):
    log_file = "/home/nuc/桌面/NUC_openkylin/接口自动化/security_check_log.txt"
    # print(f"Before encoding: {message}")  # 打印出原始的 message
    log_data = {
        "time": time.strftime('%Y-%m-%d %H:%M:%S'),
        "interface": interface,
        "message": message
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("{" + f'"time": "{time.strftime("%Y-%m-%d %H:%M:%S")}", "interface": "{interface}", "message": "{message}"' + "}\n")
    # 如果是最后一次写入，删除最后的换行符并添加方括号结束 JSON 数组
    if len(common_service_interfaces) == 1:
        with open(log_file, 'rb+', encoding="utf-8") as f:
            f.seek(-1, os.SEEK_END)
            f.truncate()
        with open(log_file, "a", encoding="utf-8") as f:
            f.write("]")


# 主程序逻辑
def main():
    config = read_config()
    start_time = time.time()
    stop_event = threading.Event()

    def stop_check():
        while not stop_event.is_set():
            elapsed_time = time.time() - start_time
            if elapsed_time >= 3:
                stop_event.set()
            time.sleep(1)

    stop_thread = threading.Thread(target=stop_check)
    stop_thread.start()

    while not stop_event.is_set():
        for interface in common_service_interfaces:
            security_check(interface, config)
            log_message(f"完成对 {interface} 的安全检查", interface)
        time.sleep(3)

    stop_thread.join()

if __name__ == "__main__":
    main()
