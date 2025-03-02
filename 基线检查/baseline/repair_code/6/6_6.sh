#!/bin/bash

# 指定要禁止登录的账号
DISABLED_ACCOUNTS="daemon bin sys adm lp uucp nuucp smmsp"

# 遍历账号并修改login.defs
for account in $DISABLED_ACCOUNTS; do
  sed -i "/^$account/ s/^/#/" /etc/login.defs
done

# 重载login服务
service login restart

# 给账号添加nologin壳
for account in $DISABLED_ACCOUNTS; do
  if [ ! -f "/etc/nologin/$account" ]; then
    touch /etc/nologin/$account
  fi  
done

# 确认配置
grep -q "^#test001" /etc/login.defs
if [ $? -eq 0 ]; then
  echo "Accounts test001 and test002 disabled for interactive login."
else
  echo "Failed to disable accounts."
fi
