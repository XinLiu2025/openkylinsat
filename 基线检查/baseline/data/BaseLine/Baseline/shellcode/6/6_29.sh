#"其他配置-6.29:检查是否设置SSH成功登录后Banner"
index=$(($index+1))

#systemctl is centos7 or redhat 7 
#tmp=`systemctl status sshd | grep running`
tmp=`service sshd status | grep running`
if [ -z "$tmp" ]; then
	echo "	检查是否设置ssh成功登录后的Banner信息，提示登录系统的人员。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
else
  temp=`cat /etc/motd`
  if [ -n "$temp" ]; then
	echo "	检查是否设置ssh成功登录后的Banner信息，提示登录系统的人员。此检查项建议调整	参考基线检测配置手册	$tmp	MANUAL		"
    manual=$(($manual+1))
  else
	echo "	检查是否设置ssh成功登录后的Banner信息，提示登录系统的人员。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
    pass=$(($pass+1))
  fi
fi

#
