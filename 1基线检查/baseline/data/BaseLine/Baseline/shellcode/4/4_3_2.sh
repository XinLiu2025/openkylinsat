#/var/log/secure"


secure_file=`find /var/log/secure`
if [ -n "$secure_file" ]; then
	secure=`stat -c %a /var/log/secure`
	if [ "$secure" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$secure	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$secure	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi



