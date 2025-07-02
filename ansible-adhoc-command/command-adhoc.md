Why use ad hoc commands?
ad hoc commands are great for tasks you repeat rarely. For example, if you want to power off all the machines in your lab for Christmas vacation, you could execute a quick one-liner in Ansible without writing a playbook. An ad hoc command looks like this:

$ ansible [pattern] -m [module] -a "[module options]"
The -a option accepts options either through the key=value syntax or a JSON string starting with { and ending with } for more complex option structure. You can learn more about patterns and modules on other pages.

Use cases for ad hoc tasks
ad hoc tasks can be used to reboot servers, copy files, manage packages and users, and much more. You can use any Ansible module in an ad hoc task. ad hoc tasks, like playbooks, use a declarative model, calculating and executing the actions required to reach a specified final state. They achieve a form of idempotence by checking the current state before they begin and doing nothing unless the current state is different from the specified final state.

Rebooting servers
The default module for the ansible command-line utility is the ansible.builtin.command module. You can use an ad hoc task to call the command module and reboot all web servers in Atlanta, 10 at a time. Before Ansible can do this, you must have all servers in Atlanta listed in a group called [atlanta] in your inventory, and you must have working SSH credentials for each machine in that group. To reboot all the servers in the [atlanta] group:

$ ansible atlanta -a "/sbin/reboot"
By default, Ansible uses only five simultaneous processes. If you have more hosts than the value set for the fork count, it can increase the time it takes for Ansible to communicate with the hosts. To reboot the [atlanta] servers with 10 parallel forks:

$ ansible atlanta -a "/sbin/reboot" -f 10
/usr/bin/ansible will default to running from your user account. To connect as a different user:

$ ansible atlanta -a "/sbin/reboot" -f 10 -u username
Rebooting probably requires privilege escalation. You can connect to the server as username and run the command as the root user by using the become keyword:

$ ansible atlanta -a "/sbin/reboot" -f 10 -u username --become [--ask-become-pass]
If you add --ask-become-pass or -K, Ansible prompts you for the password to use for privilege escalation (sudo/su/pfexec/doas/etc).

Note

The command module does not support extended shell syntaxes like piping and redirects (although shell variables will always work). If your command requires shell-specific syntax, use the shell module instead.

So far all our examples have used the default ‘command’ module. To use a different module, pass -m for module name. For example, to use the ansible.builtin.shell module:

$ ansible raleigh -m ansible.builtin.shell -a 'echo $TERM'
When running any command with the Ansible ad hoc CLI (as opposed to Playbooks), pay particular attention to shell quoting rules, so the local shell retains the variable and passes it to Ansible. For example, using double rather than single quotes in the above example would evaluate the variable on the box you were on.


### ADHOC COMMNDS EXAMPLE
### TO generate ssh key (Public & private key)
ssh-keygen cd .ssh ls

### cat the keys and note the public key,
 you will drop the public key in other target machines. Then go to target machine1

cd .ssh ls

copy authorised_key and vi. Then copy the ansible controller public key under it and save
You can now ssh to the machines and type exit to go back to your ansible

ssh 172.31.44.246 ssh 172.31.45.58

go back one step cd ..
touch inventory 
vi inventory 


To ping all target machines
ansible -i inventory all -m ping

### check for the list of items on the target machines
ansible -i inventory all -a "ls" 

or
ansible -i inventory webservers -a "ls"   # in the  the webservers group inside the inventory

### check for the list of items and hidden files on the target machines
ansible -i inventory all -a "ls -lart"

### now create directory templates on all machines
ansible -i inventory all -a "mkdir templates"

### to create a file text.txt on all machines
ansible -i inventory all -a "touch templates/text.txt"

### To remove cloud folder
ansible -i inventory all -a "rm -r -f cloud"

### adhoc commands
To put simply, Ansible ad hoc commands are one-liner Linux shell commands and playbooks are like a shell script, a collective of many commands with logic.

Ansible ad hoc commands come handy when you want to perform a quick task.

### task

### ### To check the disk/memory space on all hosts in an inventory file

ansible -i inventory all -m shell -a 'df -h'

Or

ansible -i inventory webservers -m shell -a 'df -h'

### ansible ad hoc command to check the free memory or memory usage of hosts
ansible -i inventory all -a "free -m"

### To find ids on host machines
ansible -i inventory webservers -m shell -a 'id'

### first create a file touch /tmp/my-file.txt on the control server and push it to all #machines
touch /tmp/my-file.txt

ansible -i inventory webservers -m copy -a "src=/tmp/my-file.txt dest=/tmp/my-file.txt"

### To copy a file to all hosts in an inventory file
ansible -i inventory -m copy -a 'src=/local/path/to/file dest=/remote/path/to/file mode=0644'

### You can check the status of a specific service on single hosts or server1
ansible -i inventory webservers -m service -a 'name=apache2 state=started'

###  to install apache on all machines
ansible -i inventory webservers -m apt -a 'name=apache2 state=latest'

### Command above could not run because, for multiple tasks you need to run a playbook

