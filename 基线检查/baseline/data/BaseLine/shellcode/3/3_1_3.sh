#"认证授权-3.1.1:检查用户umask设置"



#设置flag=1，若有一项不合格，则flag=0

umask1=`/bin/cat /etc/profile | grep umask | /bin/awk -F 'umask' 'NR==2{print $2}' `
#/bin/cat /etc/csh.cshrc | grep umask | /bin/awk -F 'umask' 'NR==1{print $2}'
echo `/bin/cat /etc/profile | grep umask | /bin/awk -F 'umask' 'NR==2{print $2}' `

if [ -n"$umask1" -o -z "$umask1" ];then
 echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	null	TRUE"

elses
	if [ "$umask1" -eq 077 ] || [ "$umask1" -eq 027 ]; then
		echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	$umask1	TRUE		"
	else
		echo "	umask配置后，创建系统用户时所赋予的权限为最高权限减去umask设置的权限，保证所创建用户不可创建其他权限用户。此检查项建议调整	077/027	$umask1	FAIL		"
	
	fi
fi



