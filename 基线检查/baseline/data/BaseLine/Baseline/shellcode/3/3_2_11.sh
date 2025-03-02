#/etc目录权限："
etc_file="/etc"
if [ -d "$etc_file" ]; then
	etc_stat=`stat -c %a /etc`
	if [ "$etc_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$etc_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$etc_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

