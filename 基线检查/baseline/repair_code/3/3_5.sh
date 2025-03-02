#create banner
sudo touch /etc/ssh_banner
sudo chown bin:bin /etc/ssh_banner
sudo chmod 644 /etc/ssh_banner
echo "Authorized only. All activity will be monitored and reported" | sudo tee -a /etc/ssh_banner 
echo "Banner /etc/ssh_banner" | sudo tee -a /etc/ssh/sshd_config
sudo systemctl restart sshd.service
