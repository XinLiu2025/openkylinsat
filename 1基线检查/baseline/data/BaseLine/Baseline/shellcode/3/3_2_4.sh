#/etc/services文件权限："
services_file="/etc/services"
if [ -f "$shadow_file" ]; then
	services_stat=`stat -c %a /etc/services`
	if [ "$services_stat" -ge 644 ]; then
		echo "	参考父项3.2	>=644	$services_stat	TRUE		"
	else
		echo "	参考父项3.2	>=644	$services_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=644	文件不存在	TRUE		"

fi

