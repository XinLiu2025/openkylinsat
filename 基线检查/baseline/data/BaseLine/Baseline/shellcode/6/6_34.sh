#"其他配置-6.34:检查是否限制FTP用户登录后能访问的目录"
index=$(($index+1))

tmp=`ps -ef | grep ftp | grep -v grep`
if [ -z "$tmp" ]; then
	echo "	限制FTP用户登录后能访问的目录，防止机密文件非授权访问，此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
else
  chroot_local_user=`cat /etc/vsftpd/vsftpd.conf | grep ^chroot_local_user=NO`
  chroot_list_enable=`cat /etc/vsftpd/vsftpd.conf | grep ^chroot_list_enable=YES`
  chroot_list_file=`cat /etc/vsftpd/vsftpd.conf | grep ^chroot_list_file=/etc/vsftpd/chroot_list`
  if [ -n "$chroot_local_user" ] && [ -n "$chroot_list_enable" ] && [ -n "$chroot_list_file" ]; then
    pass=$(($pass+1))
	echo "	限制FTP用户登录后能访问的目录，防止机密文件非授权访问，此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	$chroot_local_user,$chroot_list_enable,$chroot_list_file	TRUE		"
  else
	echo "	限制FTP用户登录后能访问的目录，防止机密文件非授权访问，此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	null	FAIL		"
    fail=$(($fail+1))
  fi
fi

