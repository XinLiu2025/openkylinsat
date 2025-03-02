#"口令策略-2.5 :检查是否存在空口令账号"
index=$(($index+1))
tmp=`/bin/cat /etc/shadow | /bin/awk -F: '($2 == "" ) { print "user " $1 " does not have a password "}'`
if [ -z "$tmp" ]; then
  echo "	由于空口令会让攻击者不需要口令进入系统，存在较大风险。此检查项建议调整	不存在空口令账户	null	TRUE	 	"
  pass=$(($pass+1))
else
  echo "	由于空口令会让攻击者不需要口令进入系统，存在较大风险。此检查项建议调整	不存在空口令账户	$tmp	FAIL	 	"
  fail=$(($fail+1))
fi
