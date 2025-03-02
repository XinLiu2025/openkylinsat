#/var/log/spooler"


spooler_file=`find /var/log/spooler`
if [ -n "$spooler_file" ]; then
	spooler=`stat -c %a /var/log/spooler`
	if [ "$spooler" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$spooler	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$spooler	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi



