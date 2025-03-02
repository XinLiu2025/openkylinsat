#"账号口令-2.2:检查是否设置口令最小长度 "
index=$(($index+1))
passminlen=`cat /etc/login.defs | grep PASS_MIN_LEN | grep -v ^#`

if [ -n "$passminlen" ]; then
  if [ "$days" -lt 8 ]; then
	echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应为	>=8	$days	FAIL		"
      fail=$(($fail+1))
  else
	echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应为	>=8	$days	TRUE		"
      pass=$(($pass+1))
  fi
else
  echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应为	>=8	null	FAIL		"
  fail=$(($fail+1))
fi

