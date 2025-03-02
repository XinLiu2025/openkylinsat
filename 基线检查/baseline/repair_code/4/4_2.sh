#
# 配置文件路径
CONFIG_FILE=/etc/rsyslog.conf

# 日志文件路径
LOG_FILE=/var/log/messages

# 过滤规则
FILTER_RULE="*.err;kern.debug;auth.notice"

# 检查日志文件是否存在
if [ ! -f $LOG_FILE ]; then
  sudo touch $LOG_FILE
  sudo chmod 666 $LOG_FILE
fi

# 添加日志记录规则
sudo sed -i "/$FILTER_RULE/d" $CONFIG_FILE
echo "$FILTER_RULE $LOG_FILE" | sudo tee -a $CONFIG_FILE

# 重启日志服务
sudo systemctl restart rsyslog

echo "Config log service done."
