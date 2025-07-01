### Ansible-Project

#### Welcome to an Ansible project,In this project i showed the integration of aws services, terraform ansible.It guides you through the workings of ansible adhoc commands, ansible playbook, ansible handlers, ansible galaxy roles, ansible optimisation using ansible varibles.Ansible uses the push mode configuration model mechanism.It showcases how ansible pushes adhoc commands for single task and in case of multiple task using ansible playbook all to remote servers.The ansible controlller and the remote servers was provisioned using terraform(iac)

### Project Directories 📂

Infra: Explore Terraform scripts for deploying three servers(three ec2 instances) named as ansible-controler, remote_server1 and remotes server2) on AWS.

Ansible-Adhoc-Commands: This show the use cases of how ansible can be used to deploy single task on remote machines

ansible-Plabook: This show the use cases of how asnsible can be used to implement multiple task on those remote machies using ansible playbook

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