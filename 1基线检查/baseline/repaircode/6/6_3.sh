#!/bin/bash

# 检查limits.conf文件是否存在
if [ -f "/etc/security/limits.conf" ]; then

  # 文件存在,添加配置 
  echo "* hard core 0" >> /etc/security/limits.conf
  echo "* soft core 0" >> /etc/security/limits.conf

else
  # 文件不存在,输出错误
  echo "Error: /etc/security/limits.conf not found."
  exit 1
fi

# 重载系统 limits 配置
sysctl -p

echo "Core file size limits set in /etc/security/limits.conf"
