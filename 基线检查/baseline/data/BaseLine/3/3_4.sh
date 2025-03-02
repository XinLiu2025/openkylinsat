#"认证授权-3.4:检查用户目录缺省访问权限设置 "
index=$(($index+1))
tmp=`cat /etc/login.defs | grep umask | grep -v ^#`
tmp1=`cat /etc/login.defs | grep UMASK | grep -v ^#`

tt=`echo $tmp | grep 027`
tt1=`echo $tmp1 | grep 027`
if [ -n "$tt" ] || [ -n "$tt1" ];then
	echo "	控制用户缺省访问权限，当在创建新文件或目录时应屏蔽掉新文件或目录不应有的访问允许权限，防止同属于改组的其他用户及别的组的用户修改用户的文件或更高限制。此检查项建议调整	027	$tt	TRUE		"
  	pass=$(($pass+1))
else
	echo "	控制用户缺省访问权限，当在创建新文件或目录时应屏蔽掉新文件或目录不应有的访问允许权限，防止同属于改组的其他用户及别的组的用户修改用户的文件或更高限制。此检查项建议调整	027	null	FAIL		"
  	fail=$(($fail+1))
fi

