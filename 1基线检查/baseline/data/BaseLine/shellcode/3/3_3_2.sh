#/etc/shadow的文件属性"
lsattr_sha=`lsattr /etc/shadow | awk '{ print $1 }' | awk -F- '{print $5}'`
lsattr1_sha=`lsattr /etc/shadow | awk '{ print $1 }'`
if [ "$lsattr_sha"x = "i"x  ]; then
 echo "应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系    等		$lsattr1_sha	TRUE	 	"
else
	echo "应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系   等		$lsattr1_sha	FAIL	 	"
  flag2=0
fi

