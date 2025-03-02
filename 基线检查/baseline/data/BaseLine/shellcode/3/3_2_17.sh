#/etc/grub.conf文件权限："
grub_file="/etc/grub.conf"
if [ -d "$grub_file" ]; then
	grub_stat=`stat -c %a /etc/grub.conf`
	if [ "$grub_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$grub_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$grub_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	目录不存在	TRUE		"

fi

