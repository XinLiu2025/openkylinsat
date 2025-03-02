#set umask
echo 'umask 077' | sudo tee -a /etc/csh.cshrc 
echo 'umask 077' | sudo tee -a /etc/csh.login
echo 'umask 077' | sudo tee -a /etc/bashrc
echo 'umask 077' | sudo tee -a /etc/profile
