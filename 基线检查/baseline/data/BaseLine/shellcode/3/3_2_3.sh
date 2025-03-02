#/etc/shadow文件权限："
shadow_file="/etc/shadow"
if [ -f "$shadow_file" ]; then
	shadow_stat=`stat -c %a /etc/shadow`
	if [ "$shadow_stat" -ge 400 ]; then
		echo "	参考父项3.2	>=400	$shadow_stat	TRUE		"
	else
		echo "	参考父项3.2	>=400	$shadow_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=400	文件不存在	TRUE		"

fi

