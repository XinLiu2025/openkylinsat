#"账号口令-2.3:检查是否设置口令过期警告天数 "
index=$(($index+1))
passwarn=`cat /etc/login.defs | grep PASS_WARN_AGE | grep -v ^#`
if [ -n "$passwarn" ]; then
  if [ "$days" -lt 30 ]; then
	echo "	除入域服务器超管账号分段管理无需配置外，应配置密码过期提醒策略防止密码过期无法登陆。此检查项建议调整	>=30	20	FAIL	 	"
      fail=$(($fail+1))
  else
	echo "	除入域服务器超管账号分段管理无需配置外，应配置密码过期提醒策略防止密码过期无法登陆。此检查项建议调整	>=30	20	TRUE	 	"
      pass=$(($pass+1))
  fi
else
	echo "	除入域服务器超管账号分段管理无需配置外，应配置密码过期提醒策略防止密码过期无法登陆。此检查项建议调整	>=30	20	FAIL	 	"
  fail=$(($fail+1))
fi

