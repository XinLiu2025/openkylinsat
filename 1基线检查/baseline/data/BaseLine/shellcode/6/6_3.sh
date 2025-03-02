#"其他配置-6.3:检查系统coredump设置"
index=$(($index+1))

soft=`cat /etc/security/limits.conf | grep soft | grep core | grep 0 | grep ^*`
hard=`cat /etc/security/limits.conf | grep hard | grep core | grep 0 | grep ^*`
if [ -z "$soft" ] && [ -z "$hard" ]; then

	echo "	需要检查系统cire dump设置，防止内存状态信息暴露，此检查项建议调整	参考基线配置手册		null	FAIL		"
    	fail=$(($fail+1))
else
	echo "	需要检查系统cire dump设置，防止内存状态信息暴露，此检查项建议调整	参考基线配置手册	$soft	TRUE		"
    pass=$(($pass+1))
fi

