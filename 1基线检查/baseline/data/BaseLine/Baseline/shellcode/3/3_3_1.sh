#/etc/passwd的文件属性"
lsattr_pass=`lsattr /etc/passwd | awk '{ print $1 }' | awk -F- '{print $5}'`
lsattr1_pass=`lsattr /etc/passwd `
if [ "$lsattr_pass"x = "i"x  ]; then
  echo "	应设置重要文件为i属性（如：chattr +i /etc/passwd），设定文件不能删除、改名、设定链接关系 等		$lsattr1_pass	TRUE	 	"
else
	echo "	应设置重要文件为i属性（如：chattr +i /etc/passwd），设定文件不能删除、改名、设定链接关系 等		$lsattr1_pass	FAIL	 	"
  flag2=0
fi

