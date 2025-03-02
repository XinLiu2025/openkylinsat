#"其他配置-6.35:检查是否关闭不必要的服务和端口"
index=$(($index+1))

chkconfig=`chkconfig --list`
manual=$(($manual+1))
echo "	不必要的端口和服务会扩大系统的被攻击面，此检查项建议系统管理员根据系统情况自行判断 参考基线检测配置手册 	null	MANUAL		"


