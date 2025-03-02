#/etc/rc6.d目录权限："
rc6_file="/etc/rc6.d"
if [ -d "$rc6_file" ]; then
	rc6_stat=`stat -c %a /etc/rc6.d`
	if [ "$rc6_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc6_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc6_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

