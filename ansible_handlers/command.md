## How to use handlers in ansible?

In this blog, we are talking about how to use handlers in ansible playbook.

# Introduction to Ansible Handlers

Handlers are commonly used in Ansible to start, reload, restart, and stop services. If your playbook calls for changing configuration files, you’ll almost certainly need to restart a service to see the changes take effect. In this case, you must define a handler for that service and include the notify directive in any tasks that require it.

Handlers are executed last by default, regardless of where they are in the playbook. In a playbook, you can define and call one or more handlers based on the tasks to be completed.

# Using Ansible Handlers

Handlers, as previously stated, are similar to other tasks in a playbook, with the exception that they are triggered using the notify directive and are only executed when the state changes.

# Some points to keep in mind while using handlers.

Within the playbook, a handler should have a globally unique name.
Only the first handler will be called if more than one with the same name are defined. All other handlers will be disregarded.
Handlers are always executed in the order they are defined in the handler’s section, not in the notify section.
A handler task only runs if the state changes; otherwise, it does not.
The notify and handlers directives are used to define a handler. The notify directive causes the task(s) specified in the handler's section to be executed.
Handler Example

# To start with the hands-on lab for handlers we need to have the below set in AWS console.

# Prerequisites

1. server.cnl.com — 1 CPU — 1GB RAM Ansible Server
2. node1.cnl.com — 1 CPU — 1GB RAM Ansible Client 1
3. node2.cnl.com — 1 CPU — 1GB RAM Ansible Client 2

# From ansible server execute below command

ansible all -m ping

ping command should return with ping / pong green colour. Now create a yaml file with below content added in it.



- name: Install Apache on RHEL server
  hosts: all
  tasks:
   - name: Install latest version of Apache
     yum:
      name: httpd
      state: latest
     notify:
      - start apache
  handlers:
     - name: start apache
       service:
         name: httpd
         state: restarted




# In the preceding projects, we install the most recent Apache package and then restart the service. However, if the most recent package is already present, the service will not be restarted. To accomplish this, we use handlers.

The handlers are not executed because the Apache is already present. So, we’ve removed Apache from node 1 and attempted to run the above playbook. Because Apache is not present in node1, it installs the most recent package of Apache and then executes the handler.


Ansible only bounces Apache once to avoid unnecessary restarts when multiple tasks update a configuration file and notify a handler to restart Apache.

# Using the ‘listen’ Directive to Group Handlers

You can use the listen keyword to group handlers and call them all with a single notify statement. The notify directive is set to restart services in the following playbook, which triggers all handler tasks with the listen directive.

# Determine When Handlers Should Run

If you want handlers to run before the end of the play or between tasks, use the meta module to add a meta task to flush them. The following is the definition of the meta task.


- name: Flush handlers
  meta: flush_handlers
