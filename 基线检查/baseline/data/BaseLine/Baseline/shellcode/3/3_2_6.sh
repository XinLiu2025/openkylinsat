#/etc/passwd文件权限："
passwd_file="/etc/passwd"
if [ -f "$passwd_file" ]; then
	passwd_stat=`stat -c %a /etc/passwd`
	if [ "$passwd_stat" -ge 644 ]; then
		echo "	参考父项3.2	>=644	$passwd_stat	TRUE		"
	else
		echo "	参考父项3.2	>=644	$passwd_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=644	文件不存在	TRUE		"

fi

