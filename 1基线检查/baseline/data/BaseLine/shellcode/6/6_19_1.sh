#"其他配置-6.19:检查系统是否关闭系统信任机制"


equiv=`find / -maxdepth 2 -name hosts.equiv`
rhosts=`find / -maxdepth 3 -type f -name .rhosts 2>/dev/null`
if [ -n "$equiv" ]; then
	echo "	如不关闭系统信任机制，在信任地址列表中的来访用户可不用提供口令就在本地计算机上执行远程命令。此检查项建议调整	=0		$equiv	FAIL		"
	fail=$(($fail+1))
else
	echo "	如不关闭系统信任机制，在信任地址列表中的来访用户可不用提供口令就在本地计算机上执行远程命令。此检查项建议调整	=0	null	TRUE		"
	pass=$(($pass+1))
fi

if [ -n "$rhosts" ]; then
	echo "	如不关闭系统信任机制，在信任地址列表中的来访用户可不用提供口令就在本地计算机上执行远程命令。此检查项建议调整	=0	$rhosts	FAIL		"
	fail=$(($fail+1))
else
	echo "	如不关闭系统信任机制，在信任地址列表中的来访用户可不用提供口令就在本地计算机上执行远程命令。此检查项建议调整	=0	null	TRUE		"
	pass=$(($pass+1))
fi

