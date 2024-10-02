ansible-playbook -i inventory startnginx.yaml

# to test if nginx was installed on the remote server run the command
curl localhost nginx


# now to stop nginx on all the remote machines run the playbook below

ansible-playbook -i inventory stopingnginx.yaml

# to check if nginx was stooped on all  the remote server run the command
curl localhost nginx

to ping all machines in the group of webservers inside the inventory file

[webservers]
172.31.17.115
172.31.19.148
172.31.24.8 

ansible -i inventory webservers -m ping

================

now after successfully executing and installing java on the dbservers, enter below command to make sure Java is installed in target node:

java -version

Note:

If you have issues in installing Java on target node, please do the following on target node to install python modules:

sudo apt-get update
sudo apt-get install python-software-properties

============
# for troubleshoting
sudo journalctl -u apache2


=======
# To kill all the running process on the port 80

sudo apt-get install psmisc
 sudo fuser 80/tcp sudo lsof -i tcp:80 
sudo lsof -i tcp:80 -s tcp:listen 
sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill


=====

# To purge apache2

sudo apt-get purge apache2

#now run the ansible installation for apache 2

# And now run the 
sudo systemctl status apache2.service

Troubleshooting

sudo journalctl -u apache2

