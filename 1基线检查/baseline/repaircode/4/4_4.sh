#!/bin/bash

# 创建登录日志文件
touch /var/log/login.log  
chmod 400 /var/log/login.log

# 修改sshd_config开启日志记录  
echo "LogLevel INFO" >> /etc/ssh/sshd_config
echo "SyslogFacility AUTHPRIV" >> /etc/ssh/sshd_config

# 重新加载sshd配置
service sshd reload   

# 修改login.defs开启本地登录日志记录
echo "LOG_OK_LOGINS yes" >> /etc/login.defs

# 重启登录管理服务  
service login restart   

# 完成配置,不需要人工操作vim等编辑器
