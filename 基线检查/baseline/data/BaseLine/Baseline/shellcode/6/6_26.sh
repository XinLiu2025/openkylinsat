#"其他配置-6.26:检查是否使用NTP（网络时间协议）保持时间同步"
index=$(($index+1))

ntpd=`ps -ef|egrep "ntp|ntpd"|grep -v grep | grep "/usr/sbin/ntpd"`
if [ -n "$ntpd" ]; then
  server=`cat /etc/ntp.conf | grep ^server`
  if [ -n "$server" ]; then
	echo "	应保证windows系统的时间同步，提高系统日志的准确性。此检查项建议调整	参考基线检测配置手册	$server	TRUE		"
    pass=$(($pass+1))
  else
	echo "	应保证windows系统的时间同步，提高系统日志的准确性。此检查项建议调整	参考基线检测配置手册	null	FAIL		"
    fail=$(($fail+1))
  fi
else
	echo "	应保证windows系统的时间同步，提高系统日志的准确性。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
fi

