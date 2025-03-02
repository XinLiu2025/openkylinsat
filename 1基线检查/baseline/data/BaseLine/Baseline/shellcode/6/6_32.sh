#"其他配置-6.32:检查/usr/bin/目录下可执行文件的拥有者属性"
index=$(($index+1))

find=`find /usr/bin -type f \( -perm -04000 -o -perm -02000 \) -exec ls -lg {} \; `
if [ -n "$find" ]; then
	echo "	可执行文件拥有s属性在运行时可所以获得拥有者的权限，所以为了安全需要，需要作出修改。此检查项建议调整	参考基线检测配置手册	$find	FAIL		"
	fail=$(($fail+1))
else
	echo "	可执行文件拥有s属性在运行时可所以获得拥有者的权限，所以为了安全需要，需要作出修改。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
	pass=$(($pass+1))
fi

