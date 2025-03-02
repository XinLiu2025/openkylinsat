#!/bin/bash

# 检查vsftpd是否已安装
if dpkg -s vsftpd >/dev/null 2>&1; then

  # vsftpd已安装,执行禁用匿名登录步骤
  
  sed -i 's/^anonymous_enable=YES/anonymous_enable=NO/' /etc/vsftpd.conf
  service vsftpd restart

else

  echo "VSFTP not installed, skip configuration."
  
fi

# 检查wu-ftp是否已安装
if [ -f /etc/ftpaccess ]; then

  # wu-ftp已安装,执行禁用匿名登录步骤
  
  sed -i 's/^anonymous-access/no anonymous-access/' /etc/ftpaccess
  service wu-ftpd restart
  
else

  echo "WU-FTP not installed, skip configuration."

fi

echo "Anonymous login disabled for VSFTP and WU-FTP"
