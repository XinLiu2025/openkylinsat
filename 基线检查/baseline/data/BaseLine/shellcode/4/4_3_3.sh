#/var/log/messages"

messages_file=`find /var/log/messages`
if [ -n "$messages_file" ]; then
	messages=`stat -c %a /var/log/messages`
	if [ "$messages" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$messages	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$messages	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi



