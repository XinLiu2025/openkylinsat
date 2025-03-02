#"其他配置-6.27:检查NFS（网络文件系统）服务配置"
index=$(($index+1))

tmp=`netstat -lntp | grep nfs`
if [ -z "$tmp" ]; then
	echo "	如果需要NFS服务，需要限制能够访问NFS服务的IP范围，如果没有必要，需要停止NFS服务。此检查项建议系统管理员根据系统情况自行判断	参考基线检测配置手册	null	TRUE		"
  pass=$(($pass+1))
else
  allow=`cat /etc/hosts.allow | grep -v ^#`
  deny=`cat /etc/hosts.deny | grep -v ^#`
  if [ -n "$allow" ] && [ -n "$deny" ]; then
	echo "检查NFS(网络文件系统)服务配置 参考基线检测配置手册 $allow TRUE"
    pass=$(($pass+1))
  else
	echo "检查NFS(网络文件系统)服务配置 参考基线检测配置手册 null FAIL"
    fail=$(($fail+1))
  fi
fi

