#"其他配置-6.9:检查是否关闭绑定多ip功能"

index=$(($index+1))
flag5=1
#nospoof=`cat /etc/host.conf | grep nospoof`
#if [ -n "$nospoof" ]; then
#	nospoof1=`echo $nospoof | grep on`
#	if [ -n "$nospoof1" ]; then
#		echo "	参考父项6.9	参考《Linux系统安全配置基线》对应章节	$nospoof1	TRUE		"
#	else
#		echo "	参考父项6.9	参考《Linux系统安全配置基线》对应章节	$nospoof1	FAIL		"
#		flag5=0
#	fi
#else
#	echo "	参考父项6.9	参考《Linux系统安全配置基线》对应章节	$nospoof	FAIL		"
#	flag5=0
#fi

multi=`cat /etc/host.conf | grep multi`
if [ -n "$multi" ]; then
	multi1=`echo $multi | grep off`
	if [ -n "$multi1" ]; then
		echo "	应关闭此条检查项配置内容，使系统操作责任到人。此检查项建议调整	参考基线检测配置手册	$multi1	TRUE		"
	else
		echo "	应关闭此条检查项配置内容，使系统操作责任到人。此检查项建议调整	参考基线检测配置手册	null	FAIL		"

	fi
else
	echo "	应关闭此条检查项配置内容，使系统操作责任到人。此检查项建议调整	参考基线检测配置手册 	null	FAIL		"

fi




