#"其他配置-6.21:检查是否删除了潜在危险文件"
index=$(($index+1))

rhost=`locate .rhost | egrep 'rhost$'`
equiv=`locate .netrc | egrep 'netrc$'`
equiv=`locate .equiv | egrep 'hosts.equiv$'`
if [ -z "$rhost" ] && [ -z "$netrc" ] && [ -z "$equiv" ]; then
	echo "	危险文件未删除可能导致用户无口令登录系统，存在较大风险。此检查项建议调整	参考基线检测配置手册	null，null，null	TRUE		"
  pass=$(($pass+1))
else
	echo "	危险文件未删除可能导致用户无口令登录系统，存在较大风险。此检查项建议调整	参考基线检测配置手册	$rhost，$netrc，$equiv	FAIL		"
  fail=$(($fail+1))
fi

