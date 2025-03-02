#"日志审计-4.1:检查是否配置远程日志功能"
echo "	应对远程日至进行筛选与审核。此检查项建议调整	参考《Linux安全配置基线》对应章节	null	MANUAL		"
index=$(($index+1))

msg="请检查/etc/rsyslog.conf文件，查看是否配置日志服务器"
manual=$(($manual+1))

#