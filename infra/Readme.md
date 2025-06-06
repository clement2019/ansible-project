# provisioning-ansible controller and the two remopte servers-with terraform
# project Outlook and Projectory

- provisioing of the ansible controller and the two remote servers
- Accessibility to this ansible controller instance through port 22 for ssh connection defined in SG
- the user me can only have access through SSH connection
- The provioning was done solely using terraform (IAC)

# Workflow for this task using Terraform?
- VPC creation effected to start with
- Internet Gateway created while attaching it the VPC using a Route Table
- Public Subnet creation and associate it with the Route Table
- Security Group creation for firewall for the EC2 Instance
- Ansible installation on the EC2 Instance done with script automation
- Attach an Elastic IP and Key Pair to the Ec2 instance created
- Making sure all works as specified

# project Prerequisites
Installation and configuration of AWS CLI
Installation of Terraform


# Run this to SSH into EC2
ssh -i devops_key.pem ubuntu@$(terraform output -raw jenkinsapp-server_public_ip)

# Use this to get the jenkins Admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
