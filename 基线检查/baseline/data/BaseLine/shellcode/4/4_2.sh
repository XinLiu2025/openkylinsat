#"日志审计-4.2:检查安全事件日志配置"
index=$(($index+1))

tmp=`cat /etc/rsyslog.conf | grep /var/log/messages | egrep '\*.info;mail.none;authpriv.none;cron.none' | grep -v ^#`
if [ -n "$tmp" ]; then
	echo "	应对安全时间日志文件进行配置。此检查项建议调整	参考《Linux安全配置基线》对应章节	$tmp	TRUE		"	
  pass=$(($pass+1))
else
	echo "	应对安全时间日志文件进行配置。此检查项建议调整	参考《Linux安全配置基线》对应章节	null	FAIL		"
  fail=$(($fail+1))
fi

