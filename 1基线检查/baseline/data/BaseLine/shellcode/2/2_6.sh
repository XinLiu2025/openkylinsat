#"帐号管理-2.6:检查是否设置除root之外UID为0的用户"
index=$(($index+1))

result=`/bin/cat /etc/passwd | /bin/awk -F: '($3 == 0) { print $1 }'`


if [ "root" = $result  ]; then
	echo "	不可设置除root之外，第二个具有root权限的账户。此检查项建议调整	root	null	TRUE		"
  pass=$(($pass+1))
else
	echo "	不可设置除root之外，第二个具有root权限的账户。此检查项建议调整	root	$result	FAIL		"
  fail=$(($fail+1))
fi


