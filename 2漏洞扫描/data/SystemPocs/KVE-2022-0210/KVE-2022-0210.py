#!/usr/bin/env python3
import sys
import dbus
import os
def set_main_source(target_dir, src_file):
  bus = dbus.SystemBus()
  obj = bus.get_object("com.kylin.software.properties", "/com/kylin/software/properties")
  proxy = dbus.Interface(obj, "com.kylin.software.properties.interface")
  proxy.setMainSource([f'-t {target_dir} {src_file}'])
os.system('touch set_main_source.txt')
set_main_source("/etc", os.path.realpath('./set_main_source.txt'))
result=os.popen('ls /etc/set_main_source.txt')
if result.read() :
  print("successfully")
else:
  print("fail")
os.system('rm set_main_source.txt')