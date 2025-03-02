#/etc/group文件权限："
group_file="/etc/group"
if [ -f "$group_file" ]; then
	group_stat=`stat -c %a /etc/group`
	if [ "$group_stat" -ge 644 ]; then
		echo "	参考父项3.2	>=644	$group_stat	TRUE		"
	else
		echo "	参考父项3.2	>=644	$group_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=644	文件不存在	TRUE		"

fi


