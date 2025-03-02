#ban zerocode 
sudo passwd -S $(cut -d: -f1 /etc/shadow) 2>/dev/null | awk '$2=="P" {print $1}'sudo passwd -l $(cut -d: -f1 /etc/shadow) 2>/dev/null | awk '$2=="P" {print $1}'sudo userdel $(cut -d: -f1 /etc/shadow) 2>/dev/null | awk '$2=="P" {print $1}'
