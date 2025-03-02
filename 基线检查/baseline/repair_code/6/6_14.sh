#!/bin/bash

# 先用sysctl -a输出所有参数到文件
sysctl -a > /tmp/sysctl.bak

# 禁止icmp源路由
sysctl -w net.ipv4.conf.all.accept_source_route=0

# 禁止icmp重定向报文 
sysctl -w net.ipv4.conf.all.accept_redirects=0

# 检查send_redirects配置
sysctl -w net.ipv4.conf.all.send_redirects=0

# 检查ip_forward配置
sysctl -w net.ipv4.ip_forward=0 

# 检查icmp_echo_ignore_broadcasts配置
sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1
