#"其他配置-6.4:检查历史命令设置"
index=$(($index+1))

HISTSIZE=`cat /etc/profile | grep ^HISTSIZE | egrep -v ^\#`
HISTFILESIZE=`cat /etc/profile | grep ^HISTFILESIZE | egrep -v ^\#`
if [ -n "$HISTSIZE" ] && [ -n "$HISTFILESIZE" ]; then
  if [ "$HISTSIZE" -le 5 ] && [ "$HISTFILESIZE" -le 5 ]; then
	echo "	根据等保要求，需保证历史命令文件HISTSIZE的值修改为	参考基线配置手册	$HISTSIZE，$HISTFILESIZE	TRUE		"
    pass=$(($pass+1))
  else
	echo "	根据等保要求，需保证历史命令文件HISTSIZE的值修改为	参考基线配置手册	$HISTSIZE，$HISTFILESIZE	FAIL		"
    fail=$(($fail+1))
  fi
else
	echo "	根据等保要求，需保证历史命令文件HISTSIZE的值修改为	参考基线配置手册	null，null	FAIL		"
  fail=$(($fail+1))
fi
