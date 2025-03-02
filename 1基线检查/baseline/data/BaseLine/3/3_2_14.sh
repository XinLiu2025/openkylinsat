#/etc/rc3.d目录权限："
rc3_file="/etc/rc3.d"
if [ -d "$rc3_file" ]; then
	rc3_stat=`stat -c %a /etc/rc3.d`
	if [ "$rc3_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc3_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc3_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

