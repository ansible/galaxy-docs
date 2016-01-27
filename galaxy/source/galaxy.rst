.. _galaxy_support_in_tower:

==========================================
Ansible Galaxy Support in Ansible Tower
==========================================

.. index::
   single: Ansible Galaxy
   single: Galaxy support


At the end of a Project update, Tower searches for a file called roles/requirements.yml in the top level of the Project directory. If this file is found, the following command automatically runs:

::

    ansible-galaxy install -r requirements.yml -p ./roles/ --force

This file allows you to reference Galaxy roles or roles within other repositories which can be checked out in conjunction with your own project. The addition of this Ansible Galaxy support eliminates the need to create git submodules for achieving this result.

For more information and examples on the syntax of the ``requirements.yml`` file, refer to `Advanced Control Over Role Requirements`_ in the Ansible documentation.

.. _Advanced Control Over Role Requirements: http://docs.ansible.com/galaxy.html#advanced-control-over-role-requirements-files
