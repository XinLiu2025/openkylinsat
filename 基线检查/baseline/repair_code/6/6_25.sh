#!/bin/bash

# 检查是否已安装ntp
if dpkg -s ntp > /dev/null 2>&1; then

  # ntp 已安装,执行配置

  # 停止系统自带时间同步服务
  systemctl stop systemd-timesyncd.service

  # 配置ntp服务器
  echo 'server ntp1.aliyun.com' > /etc/ntp.conf
  echo 'server ntp2.aliyun.com' >> /etc/ntp.conf  

  # 重新启动ntp服务
  systemctl restart ntp

  # 设置开机启动
  systemctl enable ntp

  # 检查同步状态
  ntpq -p

  echo "NTP time synchronization configured."

else

  echo "NTP not installed, skipping configuration." 

fi
