#/var/log/mail"

mail_file=`find /var/log/mail`
if [ -n "$mail_file" ]; then
	mail=`stat -c %a /var/log/mail`
	if [ "$mail" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$mail	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$mail	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi



