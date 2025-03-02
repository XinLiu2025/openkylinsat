#/tmp目录权限："
tmp_file="/tmp"
if [ -d "$tmp_file" ]; then
	tmp_stat=`stat -c %a /tmp`
	if [ "$tmp_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$tmp_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$tmp_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	FAIL		"

fi

