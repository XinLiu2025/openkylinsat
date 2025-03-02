#"其他配置-6.5:检查是否使用PAM认证模块禁止wheel组之外的用户su为root"
index=$(($index+1))

pam_rootok=`cat /etc/pam.d/su | grep auth | grep sufficient | grep pam_rootok.so | grep -v ^#`
pam_wheel=`cat /etc/pam.d/su | grep auth | grep pam_wheel.so | grep group=wheel | grep -v ^#`
if [ -n "$pam_rootok" ] && [ -n "$pam_wheel" ]; then
	echo "	禁止wheel组外用户使用su命令，提高操作系统的完整性。此检查项建议调整	参考基线配置手册	略	TRUE		"
  	pass=$(($pass+1))
else
	echo "	禁止wheel组外用户使用su命令，提高操作系统的完整性。此检查项建议调整	参考基线配置手册	null	FAIL		"
  	fail=$(($fail+1))

fi


