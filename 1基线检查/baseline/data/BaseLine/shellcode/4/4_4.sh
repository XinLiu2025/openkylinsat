#"日志审计-4.4:检查是否对登录进行日志记录"
index=$(($index+1))
tmp=`cat /etc/rsyslog.conf | grep /var/log/secure | egrep 'authpriv'.\('info|\*'\) | grep -v ^#`

if [ -n "$tmp" ]; then
echo "	应对登录时间日志文件进行配置，保证日志的完整性。此检查项建议调整	参考基线检测配置手册	$tmp	TRUE		"
  
else
	echo "	应对登录时间日志文件进行配置，保证日志的完整性。此检查项建议调整	参考基线检测配置手册	null	FAIL		"
  
fi

