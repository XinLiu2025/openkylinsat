#!/bin/bash
touch import_auth_file.txt
gdbus call --system --dest org.freedesktop.activation  --object-path /org/freedesktop/activation --method org.freedesktop.activation.interface.import_auth_file "`pwd`/import_auth_file.txt"
rm import_auth_file.txt
if ls -l /etc/import_auth_file.txt
then
echo "successfully"
fi