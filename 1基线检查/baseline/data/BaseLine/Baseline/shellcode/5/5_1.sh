#"协议安全-5.1:检查系统openssh安全配置"
index=$(($index+1))
#if [ "$PermitRootLogin" = "no" ] && [ "$Protocol" -eq 2 ]; then
if [ "$Protocol" -eq 2 ]; then
  pass=$(($pass+1))
echo "	openssh是使用加密的远程登录实现，可以有效保护登录及数据的安全。此检查项建议调整	2	$Protocol	TRUE		"
else
	echo "	openssh是使用加密的远程登录实现，可以有效保护登录及数据的安全。此检查项建议调整	2	null	FAIL		"
  fail=$(($fail+1))
fi


