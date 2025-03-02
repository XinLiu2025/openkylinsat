#/etc/rc2.d目录权限："
rc2_file="/etc/rc2.d"
if [ -d "$rc2_file" ]; then
	rc2_stat=`stat -c %a /etc/rc2.d`
	if [ "$rc2_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc2_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc2_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

