#!/bin/bash

# 检查pam_wheel模块是否存在
if [ ! -f "/lib/security/pam_wheel.so" ]; then
  echo "Error: pam_wheel module not found, please install libpam-modules."
  exit 1
fi

# 修改su的PAM配置
if ! grep -q "pam_wheel.so" /etc/pam.d/su; then
  sed -i '/@include common-auth/a auth required pam_wheel.so use_uid' /etc/pam.d/su
fi

# 检查wheel组只包含管理员
wheel_users=$(grep wheel /etc/group | cut -d: -f4)
if [ "$wheel_users" != "root" ]; then
  echo "Warning: wheel group contains users other than root"
fi

# 重启PAM服务
service pam restart

echo "PAM configuration updated to restrict su to wheel group."
