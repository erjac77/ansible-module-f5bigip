# ANSIBLE MODULE FOR F5 BIG-IP

This repository enables you to use Ansible to perform specific operational and configuration tasks on F5 BIG-IP systems. It is based solely on the f5-sdk (icontrol REST).

## REQUIREMENTS

* Ansible >= 2.2.0 (ansible)
* F5 Python SDK >= 2.1.0 (f5-sdk)
* F5 BIG-IP Common Utility Module for Ansible >= 0.1.0 (ansible-common-f5bigip)

## INSTALLATION

Example using Virtualenv:

```
# Install pip
sudo apt-get install python-pip

# Install virtualenv
sudo pip install virtualenv

# Make a virtual environment for your Ansible installation and activate it
mkdir ansible
cd ansible
virtualenv venv
source ./venv/bin/activate

# Install the F5 BIG-IP Common Utility Module for Ansible and all its dependencies (ansible, f5-sdk, etc.)
pip install git+git://github.com/erjac77/ansible-common-f5bigip.git#egg=ansible-common-f5bigip

# Get the Ansible Module for F5 BIG-IP
cd venv/share
mkdir my_modules
cd my_modules
git clone https://github.com/erjac77/ansible-module-f5bigip.git
```

Add the module folder to your library path. You can do this as an environment variable, or in an Ansible config file.
The config file can be:
* `ansible.cfg` file in the same directory as the playbook;
* `.ansible.cfg` in the home directory;
* `/etc/ansible/ansible.cfg`.

### ENVIRONMENT VARIABLE

```
ANSIBLE_LIBRARY = /path/to/ansible/venv/share/my_modules
```

### ANSIBLE.CFG

```
# config file for ansible -- http://ansible.com/
# ==============================================

[defaults]
library = /path/to/ansible/venv/share/my_modules
```

## EXAMPLE PLAYBOOK

```
---

- hosts: bigips
  connection: local

  tasks:

  - name: Create LTM Pool
    f5bigip_ltm_pool:
      f5bigip_hostname: "{{ inventory_hostname }}"
      f5bigip_username: admin
      f5bigip_password: admin
      f5bigip_port: 443
      name: my_pool
      partition: Common
      description: My Pool
      load_balancing_mode: least-connections-members
      state: present
    delegate_to: localhost
```

## LICENSE

Apache 2.0

## AUTHOR INFORMATION

Eric Jacob (@erjac77)