#"其他配置-6.31:检查FTP banner设置"
index=$(($index+1))

tmp=`ps -ef | grep ftp | grep -v grep`
if [ -z "$tmp" ]; then
	echo "	检查是否设置ftp成功登录后的Banner信息，提示登录系统人员。此检查项建议调整	参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
else
	echo "	检查是否设置ftp成功登录后的Banner信息，提示登录系统人员。此检查项建议调整	参考基线检测配置手册	$tmp	MANUAL		"
  manual=$(($manual+1))
fi


