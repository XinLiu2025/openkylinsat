#"认证授权-3.2:检查重要目录或文件权限设置"
echo "	需检查重要目录或文件权限设置是否合规，保障系统安全性，此检查项建议系统管理员根据系统情况自行判断	参考《Linux系统安全配置基线》对应章节	参考子项	参考子项		"
index=$(($index+1))


flag1=1
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

security_file="/etc/security"
if [ -d "$security_file" ]; then
	security_stat=`stat -c %a /etc/security`
	if [ "$security_stat" -ge 600 ]; then
		echo "	参考父项3.2	>=600	$security_stat	TRUE		"
	else
		echo "	参考父项3.2	>=600	$security_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=600	目录不存在	TRUE		"

fi

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

rc6_file="/etc/rc6.d"
if [ -d "$rc6_file" ]; then
	rc6_stat=`stat -c %a /etc/rc6.d`
	if [ "$rc6_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc6_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc6_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

rc0_file="/etc/rc0.d"
if [ -d "$rc0_file" ]; then
	rc0_stat=`stat -c %a /etc/rc0.d`
	if [ "$rc0_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc0_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc0_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

rc1_file="/etc/rc1.d"
if [ -d "$rc1_file" ]; then
	rc1_stat=`stat -c %a /etc/rc1.d`
	if [ "$rc1_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc1_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc1_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

rc2_file="/etc/rc2.d"
if [ -d "$rc2_file" ]; then
	rc2_stat=`stat -c %a /etc/rc2.d`
	if [ "$rc2_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc2_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc2_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

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

rc4_file="/etc/rc4.d"
if [ -d "$rc4_file" ]; then
	rc4_stat=`stat -c %a /etc/rc4.d`
	if [ "$rc4_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc4_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc4_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

rc5_file="/etc/rc5.d"
if [ -d "$rc5_file" ]; then
	rc5_stat=`stat -c %a /etc/rc5.d`
	if [ "$rc5_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc5_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc5_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

rc3_file="/etc/rc3.d"
if [ -d "$rc3_file" ]; then
	rc3_stat=`stat -c %a /etc/rc3.d`
	if [ "$rc3_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$rc3_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$rc3_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

init_file="/etc/rc.d/init.d"
if [ -d "$init_file" ]; then
	init_stat=`stat -c %a /etc/rc.d/init.d`
	if [ "$init_stat" -ge 750 ]; then
		echo "	参考父项3.2	>=750	$init_stat	TRUE		"
	else
		echo "	参考父项3.2	>=750	$init_stat	FAIL		"
		flag1=0
	fi
else
	echo "	参考父项3.2	>=750	目录不存在	TRUE		"

fi

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
	echo "	参考父项3.2	>=600	文件不存在	TRUE		 ">> "$csvFile"

fi

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


