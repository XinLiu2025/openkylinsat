#/etc/group的文件属性"
lsattr_gro=`lsattr /etc/group | awk '{ print $1 }' | awk -F- '{print $5}'`
lsattr1_gro=`lsattr /etc/group | awk '{ print $1 }'`
if [ "$lsattr_gro"x = "i"x  ]; then
  echo "	应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系	等	$lsattr1_gro	TRUE	 	"
else
	echo "	应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系等	等	$lsattr1_gro	FAIL	 	"
  flag2=0
fi

