#!/bin/bash

# 检查文件是否存在
if [ -f "/etc/host.conf" ]; then

  # 文件存在,使用 echo 追加配置
  echo "multi off #关闭多IP绑定" >> /etc/host.conf

else

  # 文件不存在,输出错误
  echo "/etc/host.conf not found."
  exit 1

fi

# 重载相关服务
service network restart

echo "/etc/host.conf modified to disable multi IP binding."
