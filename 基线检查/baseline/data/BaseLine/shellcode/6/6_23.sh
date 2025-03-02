#"其他配置-6.23:检查是否配置用户所需最小权限"
index=$(($index+1))
passwd=`stat -c %a /etc/passwd`
shadow=`stat -c %a /etc/shadow`
group=`stat -c %a /etc/group`

if [ "$passwd" -le 644 ] && [ "$shadow" -le 400 ] && [ "$group" -le 644 ]; then
	echo "	权限配置应为满足使用场景的最小化权限。此检查项建议调整	参考《Linux系统安全配置基线》对应章节	$passwd，$shadow，$group	TRUE		"
  pass=$(($pass+1))
else
	echo "	权限配置应为满足使用场景的最小化权限。此检查项建议调整	参考《Linux系统安全配置基线》对应章节	$passwd，$shadow，$group	FAIL		"
  fail=$(($fail+1))
fi


