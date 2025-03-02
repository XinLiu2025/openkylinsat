
#"其他配置-6.7:检查密码重复使用次数限制"
index=$(($index+1))
line=`cat /etc/pam.d/system-auth | grep password | grep sufficient | grep pam_unix.so | grep remember | grep -v ^#`
times=`echo $line|awk -F "remember=" '{print $2}'`
if [ -n "$line" ]; then
	 
  if [ $times -ge 5 ]; then

	echo "	检测密码重复使用次数，预防密码重复使用被爆破的风险。此检查项建议调整	>=5	$times	TRUE		"

  else
	echo "	检测密码重复使用次数，预防密码重复使用被爆破的风险。此检查项建议调整	>=5	$times	FAIL		"

  fi
else
	echo "	检测密码重复使用次数，预防密码重复使用被爆破的风险。此检查项建议调整	>=5	null	FAIL		"
 
fi


