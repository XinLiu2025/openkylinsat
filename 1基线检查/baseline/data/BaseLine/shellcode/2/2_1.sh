#"账号口令-2.1：检查是否设置口令生存周期"
index=$(($index+1))
#在文件etc/login.defs中搜索pass_max_days的值，并且去掉#自开头的值
#grep -v ^#    ------>  不匹配以#开头的行
passmax=`cat /etc/login.defs | grep PASS_MAX_DAYS | grep -v ^#`

if [ -n "$passmax" ]; then
	days=`echo $passmax | awk '{print $2}'`
	if [ "$days" -gt 90 ]; then
		echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	$days	FAIL	 	 "
		fail=$((fail+1))
	else
		pass=$(($pass+1))
		echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	$days	TRUE	 	 "
	fi
else
	fail=$(($fail+1))
	echo "	长期不修改密码会增加密码暴露风险，除入域服务器或服务器超管账号分段管理无需配置外，应对服务器密码最长使用期限进行限制。此检查项建议调整	<=90	无此配置	FAIL	 	 "
fi

#
