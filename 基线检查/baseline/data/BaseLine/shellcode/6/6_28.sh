#"其他配置-6.28:检查是否安装OS补丁"
echo "	及时安装操作系统补丁保证系统稳定性，此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	null	MANUAL		"
index=$(($index+1))

os=`uname -a`
manual=$(($manual+1))

