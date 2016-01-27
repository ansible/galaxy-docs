
.. this is common content between the install and reference guide and the quick install guide

.. index::
   single: download Ansible Tower
   single: installation program

Using the link provided in the email you received based on your interest in Ansible Tower, download and extract the Tower installation tarball. 

.. note::
    To obtain a trial version of Ansible Tower, visit: http://www.ansible.com/tower-trial
    
    For pricing information, visit: http://www.ansible.com/pricing

    To download the latest version of Tower directly (note, you must also obtain a license before using this), visit: https://releases.ansible.com/awx/setup/ansible-tower-setup-latest.tar.gz 

Once extracted,  ``cd`` into the setup directory using a command line console. In the following commands, replace the string ``VERSION`` with the version of Tower that you are installing ( e.g., "2.4.0").

::

  root@localhost:~$ tar xvzf ansible-tower-setup-latest.tar.gz
  root@localhost:~$ cd ansible-tower-setup-VERSION


Using Vagrant/Amazon AMI Images
=================================
.. index::
    single: Vagrant image
    single: Amazon AMI image

One easy way to try |at| is to use a Vagrant box or an Amazon EC2 instance, and launching a trial of |at| just takes a few minutes.

If you use the Vagrant box or Amazon AMI Tower images provided by Ansible, you can find the auto-generated admin password by connecting to the image and reading it from the *message of the day* (MOTD) shown at login.

Vagrant
^^^^^^^^

For Vagrant images, use the following commands to connect:

::

  $ vagrant init tower http://vms.ansible.com/ansible-tower-2.4.X-virtualbox.box
  $ vagrant up
  $ vagrant ssh

Replace ``ansible-tower-2.4.X`` with the version that you are trying to install. That last command provides your admin password and the Tower log-in URL. Upon login, you will receive directions on obtaining a trial license.

An up-to-date link to Ansible's Vagrant image is available from the `LAUNCH TOWER IN VAGRANT <http://www.ansible.com/tower-trial#hs_cos_wrapper_module_144352331448329539>`_ section of Ansible's main website.

Amazon EC2
^^^^^^^^^^^

To launch the AMI, you must have an AMI ID (which varies based on you particular AWS region). A list of regions with links to AMI IDs is available in the `LAUNCH TOWER IN AMAZON EC2 <http://www.ansible.com/tower-trial#hs_cos_wrapper_module_144352331448329539>`_ section of Ansible's main website.

For Amazon AMI images, use the following command to connect:

::

  ssh root@<your amazon instance>

You must use the SSH key that you configured the instance to accept at launch time. 


.. _bundled_install:

Using the Bundled Tower Installation Program
=============================================

.. index::
    single: bundled installer

Beginning in |at| version 2.3.0, Tower installations can be performed using a bundled installation program. The bundled installation program is meant for customers who cannot, or would prefer not to, install Tower (and its dependencies) from online repositories. Access to Red Hat Enterprise Linux or Centos repositories is still needed.

To download the latest version of the bundled Tower installation program directly (note, you must also obtain a license before using this), visit: https://releases.ansible.com/ansible-tower/setup-bundle/ 

.. note::

  The bundled installer only supports Red Hat Enterprise Linux and CentOS. Ubuntu support has not yet been added.


Next, select the installation program which matches your distribution (``el6`` or ``el7``):

::

  ansible-tower-setup-bundle-latest.el6.tar.gz 
  ansible-tower-setup-bundle-latest.el7.tar.gz 

.. note::

  Red Hat Enterprise Linux customers must enable the following repositories which are disabled by default:

   - Red Hat Enterprise Linux 7 users must enable the ``extras`` repositories.
   - Red Hat Enterprise Linux 6 users must enable the ``optional`` repository.




