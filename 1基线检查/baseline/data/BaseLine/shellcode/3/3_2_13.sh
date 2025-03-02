#/etc/rc5.d目录权限："
rc5_file="/etc/rc5.d"
if [ -d "$rc5_file" ]; then
	rc5_stat=`stat -c %a /etc/rc5.d`
	if [ "$rc5_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc5_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc5_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

