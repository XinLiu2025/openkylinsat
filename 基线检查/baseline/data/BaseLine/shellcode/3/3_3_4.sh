#/etc/gshadow的文件属性"
lsattr_gsh=`lsattr /etc/gshadow | awk '{ print $1 }' | awk -F- '{print $5}'`
lsattr1_gsh=`lsattr /etc/gshadow | awk '{ print $1 }'`
if [ "$lsattr_gsh"x = "i"x  ]; then
  echo "	应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系	等	$lsattr1_gsh	TRUE	 	"
else
	echo "	应设置重要文件为i属性（如：chattr+i/etc/passwd），设定文件不能删除、改名、设定链接关系	等	$lsattr1_gsh	FAIL	 	"
  flag2=0
fi


