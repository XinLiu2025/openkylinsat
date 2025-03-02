#!/bin/bash
gdbus call --system --dest org.ukui.kds --object-path / --method org.ukui.kds.interface.toggleCameraDevice "1';id>/tmp/toggleCameraDevicTest.txt;'"
if ls /tmp/toggleCameraDevicTest.txt
then
gdbus call --system --dest org.ukui.kds --object-path / --method org.ukui.kds.interface.toggleCameraDevice "1';rm /tmp/toggleCameraDevicTest.txt;'"
echo 'successfully'
else
echo 'fail'
fi