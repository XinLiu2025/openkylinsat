#"其他配置-6.24:检查是否关闭数据包转发功能"
index=$(($index+1))

ip_forward=`sysctl -n net.ipv4.ip_forward`
if [ 0 -eq "$ip_forward" ]; then
	echo "	Linux系统默认是禁止数据包转发的，如非系统需要，请关闭该功能。此检查项建议系统管理员根据系统情况自行判断	=0	$ip_forward	TRUE		"
  pass=$(($pass+1))
else
	echo "	Linux系统默认是禁止数据包转发的，如非系统需要，请关闭该功能。此检查项建议系统管理员根据系统情况自行判断	=0	$ip_forward	FAIL		"
  fail=$(($fail+1))
fi

