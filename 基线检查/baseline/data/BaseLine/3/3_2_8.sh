#/etc/rc0.d目录权限："
rc0_file="/etc/rc0.d"
if [ -d "$rc0_file" ]; then
	rc0_stat=`stat -c %a /etc/rc0.d`
	if [ "$rc0_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc0_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc0_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

