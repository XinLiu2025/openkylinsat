#/etc/grub/grub.conf文件权限："
grub1_file="/etc/grub/grub.conf"
if [ -d "$grub1_file" ]; then
	grub1_stat=`stat -c %a /etc/grub/grub.conf`
	if [ "$grub1_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$grub1_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$grub1_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	文件不存在	TRUE		 "

fi

