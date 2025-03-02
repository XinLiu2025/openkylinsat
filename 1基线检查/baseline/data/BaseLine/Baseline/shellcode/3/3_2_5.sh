#/etc/security目录权限："
security_file="/etc/security"
if [ -d "$security_file" ]; then
	security_stat=`stat -c %a /etc/security`
	if [ "$security_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$security_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$security_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	目录不存在	TRUE		"

fi

