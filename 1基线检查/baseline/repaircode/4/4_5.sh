#!/bin/bash

# 创建登录日志文件 
touch /var/log/su.log
chmod 400 /var/log/su.log

# 修改PAM配置开启su日志记录
echo "session required pam_tty_audit.so enable=* log=/var/log/su.log" >> /etc/pam.d/su

# 现在su命令使用就会记录到/var/log/su.log文件中了
