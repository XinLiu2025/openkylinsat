#"日志审计-4.5:检查是否配置su命令使用情况记录"


tmp=`cat /etc/rsyslog.conf | grep /var/log/secure | egrep 'authpriv'.\('info|\*'\) | grep -v ^#`
if [ -n "$tmp" ]; then
echo "	应配置su命令使用情况记录，保证高权限命令可审计。此检查项建议调整	参考基线检测配置手册	$tmp	TRUE		"
  
else
	echo "	应配置su命令使用情况记录，保证高权限命令可审计。此检查项建议调整	参考基线检测配置手册	null	FAIL		"
  
fi

#
