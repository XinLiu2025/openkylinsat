#/var/log/localmessages"

localmessages_file=`find /var/log/localmessages`
if [ -n "$localmessages_file" ]; then
	localmessages=`stat -c %a /var/log/localmessages`
	if [ "$localmessages" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$localmessages	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$localmessages	FAIL		"
		flag3=0
	fi
else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi


