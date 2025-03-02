#!/bin/bash

# 标准值 
STANDARD_VALUE=8

# 获取当前设置的值
CURRENT_VALUE=$(grep -E ^PASS_MIN_LEN /etc/login.defs | awk '{print $2}')

# 如果当前值小于标准值,则写入标准值
if [ $CURRENT_VALUE -lt $STANDARD_VALUE ]; then
  sed -i "s/^PASS_MIN_LEN.*/PASS_MIN_LEN $STANDARD_VALUE/g" /etc/login.defs 
fi
