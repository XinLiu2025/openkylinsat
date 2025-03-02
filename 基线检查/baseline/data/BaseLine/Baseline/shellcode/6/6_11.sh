#"其他配置-6.11:检查别名文件/etc/aliase"
index=$(($index+1))

#aol=`cat  ~/.bashrc | grep "^alias ls='ls -aol'"`
#rmi=`cat  ~/.bashrc | grep "^alias rm='rm -i"`
#if [ -n "$aol" ] && [ -n "$rmi" ]; then
#	echo "	/etc/aliases是linux系统下的一种配置文件，作用是将使用者名称进行转换，此检查项建议系统管理员根据系统情况自行判断	参考《Linux系统安全配置基线》对应章节	$aol，$rmi	TRUE		"
 # pass=$(($pass+1))
#else
#	echo "	/etc/aliases是linux系统下的一种配置文件，作用是将使用者名称进行转换，此检查项建议系统管理员根据系统情况自行判断	参考《Linux系统安全配置基线》对应章节	$aol，$rmi	FAIL		"
 # fail=$(($fail+1))
#fi

echo "	/etc/aliases是linux系统下的一种配置文件，作用是将使用者名称进行转换，此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	null	MANUAL		"



