#"协议安全-5.3:检查使用ip协议远程维护的设备是否配置ssh协议，禁用telnet协议"
index=$(($index+1))

msg="1.在网站上免费获取OpenSSH http://www.openssh.com/，并根据安装文件说明执行安装步骤
在/etc/services文件中，注释掉 telnet 23/tcp 一行(如不生效重启telnetd服务或xinetd服务或系统，例如，Red Hat 上重启xinetd：service xinetd restart，根据实际情况操作)"
manual=$(($manual+1))
echo "	Telnet协议名文传输，安全性低，容易被嗅探泄漏信息。此检查项建议调整手动调整	参考基线配置手册	null	MANUAL		"

