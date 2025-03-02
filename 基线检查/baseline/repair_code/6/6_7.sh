#!/bin/bash

# 设置重复使用限制为5次
REPEAT_LIMIT=5

# 修改login.defs配置
sed -i "s/^PASSWORD_HISTORY_DEPTH.*/PASSWORD_HISTORY_DEPTH   $REPEAT_LIMIT/" /etc/login.defs

# 重载配置
service login restart

echo "Password reuse limit set to $REPEAT_LIMIT."
