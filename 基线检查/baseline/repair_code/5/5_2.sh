#!/bin/bash

# 检查是否安装了snmp服务
if ! dpkg -s net-snmp >/dev/null 2>&1; then
  # 未安装snmp服务,跳过配置
  echo "SNMP service not installed, skip configuration."
  exit 0
fi

# snmp服务已安装

# 检查snmpd.conf文件是否存在
if [ ! -f /etc/snmp/snmpd.conf ]; then
  # 文件不存在,在目录下创建
  touch /etc/snmp/snmpd.conf
fi

# 修改private团体字
sed -i 's/private/custom_private/g' /etc/snmp/snmpd.conf

# 修改public团体字  
sed -i 's/public/custom_public/g' /etc/snmp/snmpd.conf

# 重启snmp服务
service snmpd restart

echo "SNMP configuration updated."
