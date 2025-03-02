#/etc/rc.d/init.d目录权限："
init_file="/etc/rc.d/init.d"
if [ -d "$init_file" ]; then
	init_stat=`stat -c %a /etc/rc.d/init.d`
	if [ "$init_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$init_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$init_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

