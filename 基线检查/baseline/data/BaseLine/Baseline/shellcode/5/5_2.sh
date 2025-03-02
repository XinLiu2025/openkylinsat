#"协议安全-5.2:检查是否修改SNMP默认团体字"
index=$(($index+1))

snmp=`ps -ef|grep "snmpd"|grep -v "grep"`
if [ -z "$snmp" ]; then
	echo "	snmp的默认团体字存在安全漏洞，容易导致服务器信息泄漏。此检查项建议调整	参考基线配置手册	null	TRUE		"
  pass=$(($pass+1))
else
  string=`cat /etc/snmp/snmpd.conf | grep com2sec  | grep public | grep -v ^# `
  if [ -n "$string" ]; then
	echo "	snmp的默认团体字存在安全漏洞，容易导致服务器信息泄漏。此检查项建议调整	参考基线配置手册	$snmp	FAIL		"
    fail=$(($fail+1))
  else
	echo "	snmp的默认团体字存在安全漏洞，容易导致服务器信息泄漏。此检查项建议调整参考基线配置手册	null	TRUE		"
    pass=$(($pass+1))
  fi
fi

