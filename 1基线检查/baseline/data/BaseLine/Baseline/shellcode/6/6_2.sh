#"其他配置-6.2:检查是否设置系统引导管理器密码"
index=$(($index+1))

grub=`cat /boot/grub/menu.lst`
lilo=`cat /etc/lilo.conf`

if [ -n "$grub" ]; then
	grub_pass=`echo $grub | grep password`
	if [ -n "$grub_pass" ]; then
		echo "	应根据引导器不同类型设置引导管理器密码。此检查项建议系统管理员根据系统情况自行判断	参考基线配置手册		$grub_pass	TRUE		"
		pass=$(($pass+1))
	else
		echo "	应根据引导器不同类型设置引导管理器密码。此检查项建议系统管理员根据系统情况自行判断	参考基线配置手册		$grub_pass	FAIL		"
		fail=$(($fail+1))
	fi

else
	echo "	应根据引导器不同类型设置引导管理器密码。此检查项建议系统管理员根据系统情况自行判断	参考基线配置手册		null	FAIL		"
	
fi

if [ -n "$lilo" ]; then
	lilo_pass=`echo $lilo | grep password`
	if [ -n "$lilo_pass" ]; then
		echo "	应根据引导器不同类型设置引导管理器密码。此检查项建议系统管理员根据系统情况自行判断	参考基线配置手册	$grub_pass	TRUE		"
		pass=$(($pass+1))
	else
		echo "	应根据引导器不同类型设置引导管理器密码。此检查项建议系统管理员根据系统情况自行判断	参考基线配置手册		$grub_pass	FAIL		"
		fail=$(($fail+1))
	fi
fi


