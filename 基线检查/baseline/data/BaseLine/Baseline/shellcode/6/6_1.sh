#"其他配置-6.1:检查是否设置命令行界面超时退出"
index=$(($index+1))

TMOUT=`cat /etc/profile |grep -i TMOUT | grep -v ^#`
if [ -z "$TMOUT" ]; then
	echo "	根据等保要求，建议设置超时时间不大于	<=600	null	FAIL		"
  fail=$(($fail+1))
else
#echo "$TMOUT"
  if [ "$TMOUT" -gt 600 ]; then
	echo "	根据等保要求，建议设置超时时间不大于	<=600	$TMOUT	FAIL		"
    fail=$(($fail+1))
  else
	echo "	根据等保要求，建议设置超时时间不大于	<=600	$TMOUT	TRUE		"
    pass=$(($pass+1))
  fi
fi



