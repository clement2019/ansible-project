### Ansible-Project

#### Welcome to an Ansible project,In this project i showed the integration of aws services, terraform ansible.It guides you through the workings of ansible adhoc commands, ansible playbook, ansible handlers, ansible galaxy roles, ansible optimisation using ansible varibles.Ansible uses the push mode configuration model mechanism.It showcases how ansible pushes adhoc commands for single task and in case of multiple task using ansible playbook all to remote servers.The ansible controlller and the remote servers was provisioned using terraform(iac).Ansible is agentless and it works with passwordless connection unlike other configuration management tools like chef and puppet that uses pull mode configuration


### Project Directories 📂

Infra: Explore Terraform scripts for deploying three servers(three ec2 instances) named as ansible-controler, remote_server1 and remotes server2) on AWS.

Ansible-Adhoc-Commands: This show the use cases of how ansible can be used to deploy single task on remote machines

ansible-Playbook: This shows the use cases of how asnsible can be used to implement multiple task on those remote machies using ansible playbook

ansible-handlers: using ansble handlers to implement multiple task on a playbook and inserting handlers in the yaml file when there is need to restart a software already started.

ansible-roles: Implement ansible roles for files management in a project when the files becomes too large.

ansible-variables: Enhanced code optimisation using ansible variables.

### Getting Started 🚀
To run locally, clone the repository:

git clone https://github.com/clement2019/ansible-project.git

Explore the Directories: Navigate into each directory to find detailed scripts,yaml files, and configurations on terraform and ansible.

### Tools and services Explored 🛠️
IAM user: Created an Iam user with administrative access
Aws cli: install aws cli thios allows you to be able to intercte with aws insfrastructure

Terraform: For proviioning of the servers within aws cloud

Ansible : For configuration managment of filesand soaftre deployment into the remote servers

To implement this project, follow the step-by-step guide in our as shown below. Learn how each tool plays a crucial role in achieving the project excellence.

### confirm aws cli was installed on the local machine
aws --version
### confirm authentication into aws cloud
aws configure: For authentication into aws cloud using 
access_key: 
secret_key:
Region:
formart:

### run this comand
aws s3 ls
aws sts get-caller-identity

### After cloning the project carry out these commanda
cd ansible-project
### now 
cd infra
### Want to deploy it to the cloud?
cd infra

terraform init

![Image](https://github.com/user-attachments/assets/a7c10105-402b-4a1f-bf7a-ab1aea36627d)

terraform plan

![Image](https://github.com/user-attachments/assets/76640605-4fc7-44fb-ba4f-93827ac00a89)

terraform apply --auto-approve

![Image](https://github.com/user-attachments/assets/720a6991-ab74-4673-be75-3d1c7ac13bb7)

### Visit the aws cloud and see the three servers provisioned as shown beloe

![Image](https://github.com/user-attachments/assets/714a0119-af32-40a5-ad50-cf3141e2acb3)

### now connect to the ansible controller machine that has the script already ruuning on it, using ssh connection. as shown below

![Image](https://github.com/user-attachments/assets/2e1a8989-4925-446a-a39c-de7d2d17403c)

### cd to the downloads folder locally on the vscode to connect to the aisnle machines as shown below

![Image](https://github.com/user-attachments/assets/467f741a-6f14-4c95-8ae7-e07196351bd8)

### confirm ansible with this command below

ansible --version

### for asible to be able to ssh connect to the other remote servers
run the command below on the ansible controlller
ssh-keygen

![Image](https://github.com/user-attachments/assets/91626f86-a523-425b-bd37-5a34b08a1030)

### If the above its ok check ifconfig on all the target machines and the ansible controller machine

sudo apt install net-tools
==============

# now lets go back to the ansible controller

cd .ssh/
ubuntu@ip-10-0-1-202:~/.ssh$ ls

authorized_keys  id_rsa  id_rsa.pub

# Now cat the public key

cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKCmrwNATFtTm8AZFfHRFIsBW67jJoNr//YTsjUr81RhN/esMFdPbCOy4w0lCT22dqpV8AVDCOPTYh72s9/W/0d/lJzoVhmr9MZVyIjIZXwwc1LDcdLPcm7AD1F3fRIF7Clskqcf2R4a7r6zslUHHIFNjKCSOEHl3AD4jbTBpKxVybDAP2viEjnmonnBSmHIHUF/5VYXjPn1FU4fr0dhQEkf0d87H8P7GkzLdPrAdPbet31ItvceZcX6NocSzTa3P6E1bkyEk3tT9b8yg6HlxW56rDTUE1LrT/sfTKasRguaKPXuMfovpnestscgBeVqbYHaJAinGADBdvxKtwxSAMH7t+wRMziZT1xLLOTSZpL9AI/TtrVrIsZZZA+y+ZHw9GCHzUx5LgPPy4l1jBGBa7wDW6v0Ekjpegl/mqFbOfPD/VOTG0yKCQYUf+ns57PZxS5oWhwN9CTOIGcUJdxJXcaIbc7OXCLaNuEo4ynmVCcJzfqai547QAqzGnwDaGZIc= ubuntu@ip-10-0-1-202

### Now copy and dump the above on all the remote machines inside the authorized_keys 

### but first ssh connection to one of the remote machines again  as usual

ssh -i "devopskey2.pem" ubuntu@3.9.118.137

once done and connected to the machines , run the command below on the remote machine
cd .ssh 

vi authorized_keys 

 ![Image](https://github.com/user-attachments/assets/805aef99-65af-401a-b5c8-bf26bb02f6c1)


### Do the same thing for the second remote machines

![Image](https://github.com/user-attachments/assets/da9755ad-3997-400a-8e29-d43e4c7bb64a)

ubuntu@ip-10-0-2-244:~$ cd .ssh
ubuntu@ip-10-0-2-244:~/.ssh$ ls
authorized_keys
ubuntu@ip-10-0-2-244:~/.ssh$ vi authorized_keys
ubuntu@ip-10-0-2-244:~/.ssh$ 

### now go back to the ansible controler 

### Now create a file called inventory, that will house the private ips of the two machines..

### i created a group webservers to house the first remote machine and another groyp call dbservers to house the seceond machine as shown below

### Now create the file weith commend below
touch  inventory
vi inventory

[webservers]
10.0.2.244

[dbservers]
10.0.3.254
              
### Now try to ssh into any opf the remote servers using the private ip address
ssh 10.0.2.244
### run  the command below to go back to ansible controller machine
exit 

### run the command on the second machine you will be able to ssh into the secind machine

ssh 10.0.3.254
### run the exit below  to go back
exit

# We can now confirm we can ssh into all the target(remote) machines but lets do it with ansible for now if we can ping these machines

ansible all -i inventory -m ping

![Image](https://github.com/user-attachments/assets/86fff424-804d-4693-a414-7d4e42798811)

# the command tells ansible that this is an inventory files and the ping shows the type of module am using

==================
In shell u cal iot shell script
In python u call python files
In ansible u call ansible playbooks

   ### =========================
    ANSIBLE ADHOC COMMANDS
   ### =========================

### You dont want to always write ansible playbooks you may want to do simple task then use adhoc commands such as below . while on the ansiblke controller

ansible -i inventory all -a "ls -lart"

![Image](https://github.com/user-attachments/assets/c952df3c-1303-4a2e-846a-284961486945)

### to create a file text.txt on all machines
ansible -i inventory all -a "touch text.txt"

### now make directory cloud on all machines

ansible -i inventory all -a "mkdir cloud"
### find the list of items in the target machines

ansible -i inventory all -a "ls"

# remove the cloud folder on all machines
ansible -i inventory all -a "rm -r cloud"

### confirm if done
ansible -i inventory all -a "ls"

### So i don't always have to do 
vi shell.sh

### So my main point is that u dont have to write playbooks all the time u can also write from ansible cli
## Understanding Ad-hoc commands in Ansible
To put simply, Ansible ad hoc commands are one-liner Linux shell commands and playbooks are like a shell script, a collective of many commands with logic.
Ansible ad hoc commands come handy when you want to perform a quick task.
task
# To check the disk space on all hosts in an inventory file
ansible -i inventory all -m shell -a 'df -h'
Or 
ansible -i inventory webservers -m shell -a 'df -h'
# ansible ad hoc command to check the free memory or memory usage of hosts

ansible -i inventory all -a "free -m"


# to find ids on host machines

ansible -i inventory webservers -m shell -a 'id'


# to install apache on all machines

ansible -i inventory webservers -m apt -a 'name=apache2 state=present'

# first create a file touch /tmp/my-file.txt on the control server and push it to all #machines

touch /tmp/my-file.txt 

ansible -i inventory webservers -m copy -a "src=/tmp/my-file.txt dest=/tmp/my-file.txt"


### =========================
    ANSIBLE PLAYBOOK
### =========================

### The first task using ansible to install nginx webserver on all the remote machines, obviousely thisn is a multiple task so use the ansible playbook below

    ![Image](https://github.com/user-attachments/assets/1c37c114-893c-446b-9ffe-5a9b4a036d51)     


### Now run the command below
      ansible-playbook -i inventory startnginx.yml

      ![Image](https://github.com/user-attachments/assets/ac85fcd7-9cb7-4d50-9cc0-76138faa6a0b)


### Now confirm if nginx is running on all servers, go to the terminal of the remote machine and run below comamnd 

     ![Image](https://github.com/user-attachments/assets/bf1fb027-2ad2-4e44-a2e1-6d0c8aa48932)

### To stop the nginx from running on all servers create theis file stopnginx.yml in ansible controler

 
        ![Image](https://github.com/user-attachments/assets/6fe9e33f-ebd1-43d9-b41f-3527403e5454)

### run this command below

     ansible-playbook -i inventory stopnginx.yml

     ### Now confirm if nginx has been stopped on all servers, go to the terminal of the remote machine and run below comamnd 

     $ sudo systemctl ststud nginx

     ![Image](https://github.com/user-attachments/assets/8697edb5-907f-4c68-b6c3-68162c6eb984)


    ### to remove nginx from the remote machine colpletely, run thei command

   sudo systemctl purge nginx

### ====================================================
    ANOTHE ANSIBLE PLAYBOOK TASK TO INSTALL JENKINS ON ALL MACHINES
### =================================================================

### make sure you are on the ansible controller machine 
### create a playbook file 

touch jenkins.yml

![Image](https://github.com/user-attachments/assets/579fcaf4-1192-4762-9241-1088e70239f6)

 ![Image](https://github.com/user-attachments/assets/07feb6ff-92f7-48f2-b8d7-efdb69fa092a)  


    ### run this command below

    ansible-playbook -i inventory jenkins.yml


    ![Image](https://github.com/user-attachments/assets/08c81d83-89ff-4b40-a329-ee3e9ee095eb)


#### if you now copy the public ip of the remote machines  on the aws console
http://3.9.118.137:8080/login?from=%2F

    ![Image](https://github.com/user-attachments/assets/04f1d0aa-0836-45e5-82cf-812d3a6c6360)


# confirm if JENKINS was installed on the remote server using  the command below

sudo systemctl status jenkins.service

sudo systemctl status jenkins

curl localhost jenkins

### Troubleshooting

sudo journalctl -u jenkins


#### Now to stop jenkins run this command below

![Image](https://github.com/user-attachments/assets/9f352fd6-ae5e-4346-b825-37ccd53203c5)

 ### =====================================
    ANSIBLE VARIABLE FOR CODE OPTIMISATION
### ======================================
Ansible code or yaml files optimisation is very key and helps to manage and optimised our code. Am example is given below installing appache2 

![Image](https://github.com/user-attachments/assets/bb3086f3-44be-4b54-99ea-167d260f6ab2)


![Image](https://github.com/user-attachments/assets/49020e24-47ab-47b0-bd8a-cd199730814d)


### No to remove the appache from the remote machines run this optmised code

![Image](https://github.com/user-attachments/assets/331b38c8-47dc-4356-a7d8-303c58503fc8)


#### Creating user, group, dowwnloding files and installing appache 


![Image](https://github.com/user-attachments/assets/45a35c50-04fc-4e3e-9ee7-66b4f4a8208f)


   ### no cd to the infra folder
   cd infra
### now to clean up run the terraform destroy command below

terraform destroy --auto-approve

![Image](https://github.com/user-attachments/assets/0c526b92-7a76-400a-b73a-f0ef378fb1b0)