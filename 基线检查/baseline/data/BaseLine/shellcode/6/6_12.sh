#"其他配置-6.12:检查拥有suid和sgid权限的文件"
index=$(($index+1))

find=`find /usr/bin/chage /usr/bin/gpasswd /usr/bin/wall /usr/bin/chfn /usr/bin/chsh /usr/bin/newgrp /usr/bin/write /usr/sbin/usernetctl /usr/sbin/traceroute /bin/mount /bin/umount /bin/ping /sbin/netreport -type f -perm +6000 2>/dev/null`
if [ -n "$find" ]; then
	echo "	suid的管理上有漏洞，易被黑客利用suid来踢拳，来放后门控制linux主机。此检查项建议调整	参考基线检测配置手册 $dind		FAIL		"
	fail=$(($fail+1))
else
	echo "	suid的管理上有漏洞，易被黑客利用suid来踢拳，来放后门控制linux主机。此检查项建议调整	参考基线检测配置手册 null		TRUE		"
	pass=$(($pass+1))
fi


