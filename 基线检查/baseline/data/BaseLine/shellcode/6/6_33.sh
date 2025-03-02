#"其他配置-6.33:检查Telnet banner设置"
index=$(($index+1))


#systemctl是centos7&redhat7
#tmp=`systemctl status telnet.socket  | grep active`
tmp=`service telnet.socket | grep active`
if [ -z "$tmp" ]; then
  pass=$(($pass+1))
	echo "	检查是否设置telnet成功登录后的Banner信息，提示登录系统的人员。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
else
  manual=$(($manual+1))
	echo "	检查是否设置telnet成功登录后的Banner信息，提示登录系统的人员。此检查项建议调整	参考基线检测配置手册	$tmp	MANUAL		"
fi

