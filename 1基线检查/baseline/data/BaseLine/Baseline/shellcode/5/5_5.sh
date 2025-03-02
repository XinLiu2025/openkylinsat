#"协议安全-5.5:检查是否禁止匿名用户登录FTP"
index=$(($index+1))

tmp=`ps -ef | grep ftp | grep -v grep`
tmp1=`cat /etc/vsftpd/vsftpd.conf`
if [ -z "$tmp" ]; then
	echo "	由于匿名用户对被黑客用来进入ftp，导致系统文件的保密性和完整性遭到破坏。此检查项建议调整	参考基线配置手册	 	null	TRUE		"
  
else
  tmp=`cat /etc/vsftpd/vsftpd.conf | grep "anonymous_enable=NO" | grep -v ^#`
  if [ -z "$tmp1" ]; then
	echo "	由于匿名用户对被黑客用来进入ftp，导致系统文件的保密性和完整性遭到破坏。此检查项建议调整	参考基线配置手册		null	FAIL		"
    
  else
	echo "	由于匿名用户对被黑客用来进入ftp，导致系统文件的保密性和完整性遭到破坏。此检查项建议调整	参考基线配置手册		$tmp	TRUE		"
    
  fi
fi


