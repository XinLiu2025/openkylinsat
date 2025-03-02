#"协议安全-5.4:检查是否禁止root用户登录FTP"
index=$(($index+1))

tmp=`ps -ef | grep ftp | grep -v grep`
if [ -z "$tmp" ]; then
	echo "	由于root用户权限过大，容易导致系统文件误删除。此检查项建议调整	null	null	TRUE		"
  pass=$(($pass+1))
else
  root=`cat /etc/vsftpd/ftpusers | grep root | grep -v ^#`
  if [ -n "$root" ]; then
echo "	由于root用户权限过大，容易导致系统文件误删除。此检查项建议调整	null	$root	TRUE		"
    pass=$(($pass+1))
  else
	echo "	由于root用户权限过大，容易导致系统文件误删除。此检查项建议调整	null	$root	FAIL		"
    fail=$(($fail+1))
  fi
fi


