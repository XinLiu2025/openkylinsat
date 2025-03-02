#"其他配置-6.30:检查FTP用户上传的文件所具有的权限"
index=$(($index+1))

tmp=`netstat -lntp | grep ftp`
if [ -z "$tmp" ]; then
	echo "	限制FTP用户登录后上传文件的属性，保证同组用户、其他用户不得有写入权限。此检查项建议调整	参考基线检测配置手册	 null	TRUE		"
  pass=$(($pass+1))
else
  local_umask=`cat /etc/vsftpd/vsftpd.conf | grep local_umask | grep 022 | grep -v ^#`
  anon_umask=`cat /etc/vsftpd/vsftpd.conf | grep anon_umask | grep 022 | grep -v ^#`
  if [ -n "$local_umask" ] && [ -n "$anon_umask" ]; then
	echo "	限制FTP用户登录后上传文件的属性，保证同组用户、其他用户不得有写入权限。此检查项建议调整	参考基线检测配置手册	$tmp	TRUE		"
    pass=$(($pass+1))
  else
	echo "	限制FTP用户登录后上传文件的属性，保证同组用户、其他用户不得有写入权限。此检查项建议调整	参考基线检测配置手册	null	FAIL		"
    fail=$(($fail+1))
  fi
fi

