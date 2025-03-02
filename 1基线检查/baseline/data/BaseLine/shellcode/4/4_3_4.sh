#/var/log/boot.log"

boot_file=`find /var/log/boot.log`
if [ -n "$boot_file" ]; then
	boot=`stat -c %a /var/log/boot.log`
	if [ "$boot" -ge 755 ]; then
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$boot	TRUE		"
	else
		echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	$boot	FAIL		"
		flag3=0
	fi

else
	echo "	应配置日志文件非全局可写，保证日至不可篡改。此检查项建议调整	>=755	文件不存在	TRUE		"

fi



