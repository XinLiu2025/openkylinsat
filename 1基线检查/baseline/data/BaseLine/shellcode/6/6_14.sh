#"其他配置-6.14:检查系统内核参数配置"
index=$(($index+1))

tcp_syncookies=`cat /proc/sys/net/ipv4/tcp_syncookies`
if [ "$tcp_syncookies" -eq 1 ]; then
	echo "	该项配置主要为了缓解拒绝服务攻击。此检查项建议调整	参考基线检测配置手册	$tcp_syncookies	TRUE		"
  pass=$(($pass+1))
else
	echo "	该项配置主要为了缓解拒绝服务攻击。此检查项建议调整	参考基线检测配置手册	$tcp_syncookies	FAIL		"
  fail=$(($fail+1))
fi


