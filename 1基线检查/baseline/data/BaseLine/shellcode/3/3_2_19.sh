#/etc/lilo.conf文件权限："
lilo_file="/etc/lilo.conf"
if [ -d "$lilo_file" ]; then
	lilo_stat=`stat -c %a /etc/lilo.conf`
	if [ "$lilo_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$lilo_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$lilo_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	文件不存在	TRUE		"

fi

if [ "$flag1" -eq 1 ];then
	pass=$(($pass+1))
else
	fail=$(($fail+1))
fi
