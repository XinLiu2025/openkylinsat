#/etc/rc1.d目录权限："
rc1_file="/etc/rc1.d"
if [ -d "$rc1_file" ]; then
	rc1_stat=`stat -c %a /etc/rc1.d`
	if [ "$rc1_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc1_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc1_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

