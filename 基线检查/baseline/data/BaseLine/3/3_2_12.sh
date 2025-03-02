#/etc/rc4.d目录权限："
rc4_file="/etc/rc4.d"
if [ -d "$rc4_file" ]; then
	rc4_stat=`stat -c %a /etc/rc4.d`
	if [ "$rc4_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc4_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc4_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

