import os
os.system("echo http://archive.kylinos.cn/kylin/KYLIN-ALL 10.1 main restricted universe multiverse >> /etc/apt/sources.list")
os.system("apt update")
os.system("apt install kylin-activation")