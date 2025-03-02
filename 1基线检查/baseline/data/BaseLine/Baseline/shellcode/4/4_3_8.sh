#/var/log/maillog"

maillog_file=`find /var/log/maillog`
if [ -n "$maillog_file" ]; then
	maillog=`stat -c %a /var/log/maillog`
	if [ "$maillog" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$maillog	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$maillog	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi




