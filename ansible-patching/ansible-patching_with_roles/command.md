# to create a role in ansible run the comand below

ansible-galaxy init nginx_role


# Now to run ansible patching role on the remote servers run the command below

ansible-palybook -i inventory playbook_nginx_role.yaml
