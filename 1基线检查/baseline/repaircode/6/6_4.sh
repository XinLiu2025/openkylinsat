#!/bin/bash

# 检查/etc/profile文件是否存在
if [ -f "/etc/profile" ]; then

  # 文件存在,添加配置
  sed -i 's/^HISTFILESIZE=.*/HISTFILESIZE=5/' /etc/profile
  sed -i 's/^HISTSIZE=.*/HISTSIZE=5/' /etc/profile  

else

  # 文件不存在,显示错误
  echo "Error: /etc/profile not found."
  exit 1

fi

# 重载bash配置使其生效
source /etc/profile 

echo "Bash history settings modified in /etc/profile."
