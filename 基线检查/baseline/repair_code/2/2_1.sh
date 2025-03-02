#!/bin/bash

# 标准值
STANDARD_VALUE=90

# 获取当前配置的值
CURRENT_VALUE=$(grep -E ^PASS_MAX_DAYS /etc/login.defs | awk '{print $2}')

# 如果当前值大于标准值,则写入标准值
if [ $CURRENT_VALUE -gt $STANDARD_VALUE ]; then
  sed -i "s/^PASS_MAX_DAYS.*/PASS_MAX_DAYS $STANDARD_VALUE/g" /etc/login.defs
fi

CURRENT_VALUE=$(grep -E ^PASS_MAX_DAYS /etc/login.defs | awk '{print $2}')

echo $CURRENT_VALUE
