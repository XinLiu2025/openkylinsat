#!/bin/bash

# 安装SSH服务
apt install openssh-server -y

# 启动SSH服务
systemctl enable ssh  
systemctl start ssh

# 修改sshd_config,禁用PasswordAuthentication
sed -i 's/^PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# 重启SSH服务
systemctl restart ssh

# 检查是否安装了telnet服务
if dpkg -s telnetd >/dev/null 2>&1; then

  # telnet服务已安装,执行禁用
  
  systemctl stop telnet.socket
  systemctl disable telnet.socket 
  
  sed -i 's/^telnet/#telnet/' /etc/inetd.conf
  
  systemctl restart inetd

else

  echo "Telnet service not installed, skip disabling."

fi
