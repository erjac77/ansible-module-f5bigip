# ANSIBLE MODULE FOR F5 BIG-IP

An Ansible module to perform specific operational and configuration tasks on F5 BIG-IP systems. It is based on the f5-sdk (iControl REST).

## REQUIREMENTS

* Ansible >= 2.2.0 (ansible)
* F5 Python SDK >= 2.3.1 (f5-sdk)
* F5 Common Utility Module for Ansible >= 0.4.0 ([ansible-common-f5](https://github.com/erjac77/ansible-common-f5))

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

# Install the F5 Common Utility Module for Ansible and all its dependencies (ansible, f5-sdk, etc.)
pip install git+git://github.com/erjac77/ansible-common-f5.git#egg=ansible-common-f5

# Get the Ansible Module for F5 BIG-IP
cd venv/share
mkdir my_modules
cd my_modules
git clone https://github.com/erjac77/ansible-module-f5bigip.git
```

Add the module folder to your library path. You can do this as an environment variable or in an Ansible config file.

### ENVIRONMENT VARIABLE

```
ANSIBLE_LIBRARY = /path/to/ansible/venv/share/my_modules
```

### ANSIBLE.CFG

The config file can be:
* `ansible.cfg` file in the same directory as the playbook;
* `.ansible.cfg` in the home directory;
* `/etc/ansible/ansible.cfg`.

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
      f5_hostname: "{{ inventory_hostname }}"
      f5_username: admin
      f5_password: admin
      f5_port: 443
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

Eric Jacob ([@erjac77](https://github.com/erjac77))