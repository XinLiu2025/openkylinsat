#!/bin/bash

# 标准值
STANDARD_VALUE=30 

# 获取当前设置的值
CURRENT_VALUE=$(grep -E ^PASS_WARN_AGE /etc/login.defs | awk '{print $2}')

# 如果当前值小于标准值,写入标准值  
if [ $CURRENT_VALUE -lt $STANDARD_VALUE ]; then
  sed -i "s/^PASS_WARN_AGE.*/PASS_WARN_AGE $STANDARD_VALUE/g" /etc/login.defs
fi

CURRENT_VALUE=$(grep -E ^PASS_WARN_AGE /etc/login.defs | awk '{print $2}')

echo $CURRENT_VALUE
