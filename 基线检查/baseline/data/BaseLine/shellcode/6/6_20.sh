#"其他配置-6.20:检查磁盘空间占用率"
space=$(df -h | awk -F "[ %]+" 'NR!=1''{print $5}')
index=$(($index+1))
flag=0
for i in $space
do
  if [ $i -ge 80 ];then
    flag=1
  fi
done
if [ "$flag" -eq 1 ];then
  manual=$(($manual+1))
  echo "	磁盘动态分区空间不足，可能会导致系统卡慢与崩溃。此检查项建议系统管理员根据系统情况自行判断	<=80	由于数据过于冗长，可通过命令自行查看略	FAIL		"
else
  pass=$(($pass+1))
  echo "	磁盘动态分区空间不足，可能会导致系统卡慢与崩溃。此检查项建议系统管理员根据系统情况自行判断	<=80	null	TRUE		"
fi


