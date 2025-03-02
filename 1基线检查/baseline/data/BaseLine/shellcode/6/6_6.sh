#"其他配置-6.6:检查是否对系统账户进行登录限制"
index=$(($index+1))


msg="请手动检查文件文件/etc/passwd，/etc/shadow，并使用命令：usermod -s /sbin/nologin username"
manual=$(($manual+1))
echo "	对系统账户登录进行限制，禁止账户交互式登录。此检查项建议调整	参考基线配置手册	null	MANUAL  "

