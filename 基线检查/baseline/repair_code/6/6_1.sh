#!/bin/bash

# 设置超时时间为5分钟
timeout=600 

# 修改profile,加上超时逻辑
sed -i '/^# Set timeout/a TMOUT='"$timeout"'; export TMOUT' /etc/profile

# 修改bashrc,加上超时逻辑
sed -i '/^# Set timeout/a TMOUT='"$timeout"'; export TMOUT' /etc/bash.bashrc

# 立即应用改动
source /etc/profile
source /etc/bash.bashrc

echo "Command line interface timeout set to $timeout seconds."
