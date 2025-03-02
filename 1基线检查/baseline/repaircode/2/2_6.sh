#ban UID=0
awk -F: '$3==0 {print $1}' /etc/passwd
awk -F: '$3==0{print $1}' /etc/passwd | xargs -I {} sudo passwd -l {}
awk -F: '$3==0{print $1}' /etc/passwd | grep -v root | xargs -I {} sudo userdel -r {}
