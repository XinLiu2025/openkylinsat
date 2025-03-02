#"账号口令-2.4:检查设备密码复杂度策略 "
index=$(($index+1))


flag=0
info=`cat /etc/pam.d/system-auth | grep password | grep requisite`
#line=`cat /etc/pam.d/system-auth | grep password | grep pam_cracklib.so | grep -v ^#`
if [ -n "$info" ]; then
    # minlen:密码字符串长度，dcredit数字字符个数，ucredit大写字符个数，ocredit特殊字符个数，lcredit小写字符个数

echo "$dcredit"
    if [ "$dcredit" -eq 1 ] && [ "$ucredit" -eq 1 ] && [ "$lcredit" -eq 1 ] && [ "$ocredit" -eq 1 ]; then
        flag=1
    fi
fi

 # 以下检查/etc/security/pwquality.conf文件中的内容
 # minlen为密码字符串长度，minclass为字符类别
line_minlen=`cat /etc/security/pwquality.conf | grep minlen | grep -v ^#`
line_minclass=`cat /etc/security/pwquality.conf | grep minclass | grep -v ^#`

if [ -n "$line_minlen" ] && [ -n "$line_minclass" ]; then
	if [ "$minlen" -ge 6 ] && [ "$minclass" -ge 4 ];then

    	flag=1

    fi
fi


if [ "$flag" -eq 1 ]; then
	pass=$(($pass+1))
	echo "	密码复杂度过低会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，密码复杂度应包含特殊字符、大小写字母。此检查项建议调整	至少有1个大写字母、1个小写字母、1个数字、1个特殊字符	null	TRUE	 	"
else
	echo "	密码复杂度过低会增加密码被爆破风险，按照企业密码管理要求与等级保护标准，密码复杂度应包含特殊字符、大小写字母。此检查项建议调整	至少有1个大写字母、1个小写字母、1个数字、1个特殊字符	null	FAIL	 	"
	fail=$(($fail+1))


fi

