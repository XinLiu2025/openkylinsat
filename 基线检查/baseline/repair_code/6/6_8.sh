#!/bin/bash

# 设置最大失败次数 
MAX_RETRY=5

# 修改login.defs
sed -i "s/^LOGIN_RETRIES.*/LOGIN_RETRIES $MAX_RETRY/" /etc/login.defs

# 修改PAM配置
sed -i "s/^auth.*requisite.*pam_tally2.so.*/auth required pam_tally2.so deny=$MAX_RETRY reset/" /etc/pam.d/common-auth

# 检查pamreload命令是否存在
if command -v pamreload >/dev/null 2>&1; then
  # 存在则重载PAM配置
  pamreload
else
  # 不存在给出提示
  echo "pamreload command not found, please reload PAM manually."  
fi

echo "User authentication failure limit set."
