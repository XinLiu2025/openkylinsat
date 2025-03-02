#/etc/xinetd.conf文件权限："
xineted_file="/etc/xineted.conf"
if [ -f "$xineted_file" ]; then
	xineted_stat=`stat -c %a /etc/xineted.conf`
	if [ "$xineted_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$xineted_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$xineted_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	文件不存在	TRUE		"

fi

