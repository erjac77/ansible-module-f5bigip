🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨

**_Ansible module for F5 BIG-IP_ (`ansible-module-f5bigip`) has been deprecated_.<br/>
Please use our new [Ansible Role for F5 systems (`ansible-role-f5`)](https://github.com/erjac77/ansible-role-f5).**

🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨

# ANSIBLE MODULE FOR F5 BIG-IP

An Ansible module to perform specific operational and configuration tasks on F5 BIG-IP systems.

* Over 190 components supported (and counting).
* Easy installation. Installing the module is quite simple and requires only two steps.

## REQUIREMENTS

* Ansible >= 2.4.0 (ansible)
* F5 Common Utility Module for Ansible >= 1.0.0 ([ansible-common-f5](https://github.com/erjac77/ansible-common-f5))
* F5 Python SDK >= 3.0.15 (f5-sdk)

## INSTALLATION

### 1) Install the F5 Common Utility Module for Ansible and all its dependencies (ansible, f5-sdk, six, etc.)

```shell
pip install git+https://github.com/erjac77/ansible-common-f5.git#egg=ansible-common-f5
```

### 2) Install the F5 BIG-IP Role from Ansible Galaxy

```shell
ansible-galaxy install erjac77.module-f5bigip
```

For alternative installation methods, see the [Wiki](https://github.com/erjac77/ansible-module-f5bigip/wiki/Alternative-Installation-Methods).

## EXAMPLE PLAYBOOK

```yaml
- hosts: bigips
  connection: local
  roles:
    - erjac77.module-f5bigip

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
```

You'll find more examples in the [Wiki](https://github.com/erjac77/ansible-module-f5bigip/wiki/Playbook-Examples).

## LICENSE

Apache 2.0

## AUTHOR INFORMATION

* Eric Jacob ([@erjac77](https://github.com/erjac77))

### CONTRIBUTORS

* Gabriel Fortin ([@GabrielFortin](https://github.com/GabrielFortin))
