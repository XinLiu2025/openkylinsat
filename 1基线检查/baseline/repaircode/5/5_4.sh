#!/bin/bash

# 检查vsftpd是否已安装
if dpkg -s vsftpd >/dev/null 2>&1; then

  # vsftpd已安装,执行禁用root步骤
  
  sed -i 's/^root/#root/' /etc/vsftpd.conf
  service vsftpd restart 

else

  echo "VSFTP not installed, skip configuration."

fi

# 检查是否安装了WU-FTP
if [ -f /etc/ftpaccess ]; then

  # WU-FTP已安装

  # 禁止root登录
  sed -i 's/^root/#root/' /etc/ftpaccess  
  service wu-ftpd restart 

else
  echo "WU-FTP not installed, skip configuration."  
fi

echo "Root login disabled for VSFTP and WU-FTP."
