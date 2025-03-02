#"认证授权-3.5:检查是否设置SSH登录前警告Banner"
index=$(($index+1))
banner1=`cat /etc/ssh/sshd_config | grep Banner`

# 如果banner为空或者为 None，则符合要求
if [ -z "$banner1" ]; then
	echo "	检查是否设置ssh登陆前的警告Banner信息，警示登陆系统的人员。此检查项建议调整	设置	null	TRUE		"
  pass=$(($pass+1))
else
  if [ -n "$banner2" ]; then
	echo "	检查是否设置ssh登陆前的警告Banner信息，警示登陆系统的人员。此检查项建议调整	设置	null	TRUE		"
    pass=$(($pass+1))
  else
	echo "	检查是否设置ssh登陆前的警告Banner信息，警示登陆系统的人员。此检查项建议调整	设置	$banner2	FAIL		"
    manual=$(($manual+1))
  fi
fi

