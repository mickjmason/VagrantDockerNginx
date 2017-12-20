# VagrantDockerNginx
Nginx running in an Alpine linux container, in a VirutalBox VM configured via Ansible

OVERVIEW
--------

When executed, the code in this repository will use Vagrant to build an Ubuntu (Trusty) VirtualBox VM
It will then use Ansible to configure the VM with Docker, and create a new container based on Apline linux.
Finally, it will install and configure nginx in the container, such that the hosted page can be viewed from the originating machine, at http://localhost:18081

REQUIREMENTS
------------
Vagrant (1.8.1 was used to test this configuration)
VirtualBox
