#"其他配置-6.18:检查系统是否禁用Ctrl+Alt+Delete组合键"
index=$(($index+1))
tmp=`cat /usr/lib/systemd/system/ctrl-alt-del.target | grep "Alias=ctrl-alt-del.target" | grep -v ^#`

if [ -n "$tmp" ]; then
	echo "	linux操作系统只要按下Ctrl+Alt+Del快捷键，系统有时会重启。 参考基线检测配置手册	$tmp	FAIL		"
  fail=$(($fail+1))
else
	echo "	linux操作系统只要按下Ctrl+Alt+Del快捷键，系统有时会重启。 参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
fi


