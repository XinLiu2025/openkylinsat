#!/bin/bash

# 检查sshd配置文件是否存在
if [ -f /etc/ssh/sshd_config ] || [ -f /etc/ssh2/sshd2_config ]; then

  # sshd配置文件存在

  # 在配置文件中追加Protocol 2
  if [ -f /etc/ssh/sshd_config ]; then
    echo "Protocol 2" >> /etc/ssh/sshd_config 
  elif [ -f /etc/ssh2/sshd2_config ]; then  
    echo "Protocol 2" >> /etc/ssh2/sshd2_config
  fi

  # 重新加载sshd服务
  systemctl reload sshd.service


  fi
  # sshd配置文件不存在,跳过配置

	

# 以上检查并有条件地配置Protocol 2
