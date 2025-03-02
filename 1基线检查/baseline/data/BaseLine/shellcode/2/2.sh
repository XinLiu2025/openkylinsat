#"账号口令-2:检查是否设置口令更改最小间隔天数 "
#index=$(($index+1))
#passmin=`cat /etc/login.defs | grep PASS_MIN_DAYS | grep -v ^#`

#if [ -n "$passmin" ]; then
#  if [ "$days" -lt 7 ]; then
#	echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应##为	>=8	$days	FAIL"
#      fail=$(($fail+1))
#  else
#	echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应#为	>=8	$days	TRUE"  >> "$csvFile"
#      pass=$(($pass+1))
#  fi
#else
#  echo "	密码长度过短会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，口令长度最小值应为	>=8	null	FAIL"
#  fail=$(($fail+1))
#fi

