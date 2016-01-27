
.. note::

    Tower is a full application and the installation process installs several dependencies such as PostgreSQL, Django, Apache, and others. 
    It is required that you install Tower on a standalone VM or cloud instance and do not co-locate any other applications on that machine (beyond possible monitoring or logging software). Although Tower and Ansible are written in Python, they are not just simple Python libraries. Therefore Tower cannot be installed in a Python virtualenv, a Docker container, or any similar subsystem; you must install it as described in the installation instructions in this guide.

Primary Requirements
=======================

Ansible Tower has the following requirements:

-  Supported Operating Systems:

    -  Red Hat Enterprise Linux 6 64-bit
    -  Red Hat Enterprise Linux 7 64-bit
    -  CentOS 6 64-bit
    -  CentOS 7 64-bit
    -  Ubuntu 12.04 LTS 64-bit
    -  Ubuntu 14.04 LTS 64-bit

-  An HTML5 compliant web browser 
-  2 GB RAM minimum (4+ GB RAM recommended)
    
    - 2 GB RAM (minimum and recommended for Vagrant trial installations)
    - 4 GB RAM is recommended per 100 forks

-  20 GB hard disk 

    - 10 GB of the 20 GB requirement must be dedicated to ``/var/``, where Tower stores its files and working directories (dedicating less space will cause the installation to fail)
    
-  64-bit support required (kernel and runtime)
-  For Amazon EC2:

    -  Instance size of m3.medium or larger
    -  An instance size of m3.xlarge or larger if there are more than 100 hosts

- For HA MongoDB setups:

    -  If you plan to run MongoDB, the following guidelines provide a rough estimate for the amount of space required. The basic calculation is:

        ``(number of hosts in inventory) * (number of scans) * (average module fact size) * (number of modules scanning)``

    - For example:

        hosts = 1,000

        number of scans = 365 (1 scan per day for a year)
        
        average module fact size = 100 kb
        
        number of modules = 4 (ansible, packages, services, files)
        
        = 146 GB


    The default scan operation has the four (4) modules listed, but you can add your own. Depending on the kinds of modules and the size of the facts you are gathering, that size might be larger.

    To help keep the size down, you can use a management job to purge old facts. Refer to :ref:`Management Jobs <ag_management_jobs>` in the *Ansible Tower Administration Guide* for more information

Ansible Software Requirements
==================================

.. index::
    single: Ansible, 1.9.4
    single: Ansible, latest stable
    single: Ansible, 2.0

While Ansible Tower depends on Ansible playbooks and requires the installation of the latest stable version of Ansible before installing Tower, manual installations of Ansible are no longer required.

Beginning with |at| version 2.3, the Tower installation program attempts to install Ansible as part of the installation process. Previously, Tower required manual installations of the Ansible software release package before running the Tower installation program. Now, Tower attempts to install the latest stable Ansible release package, which is Ansible version 1.9.4. 

If performing a bundled tower installation, the installation program attempts to install Ansible (and its dependencies) from the bundle for you (refer to :ref:`bundled_install` for more information).

If you choose to install Ansible on your own, the Tower installation program will detect that Ansible has been installed and will not attempt to reinstall it. The latest stable version (Ansible version 1.9.4) must be installed for |at| to work properly.

At this time, Ansible 2.0 is not supported or recommended for Ansible Tower as it is still in beta and has not become the latest stable release package. Ansible modules which are 2.0 versions have not yet been tested against Ansible Tower and are not yet supported or recommended for use. 

Additional Notes
======================

While other operating systems may technically function, currently only the above list is supported to host an Ansible Tower installation. If you have a firm requirement to run Tower on an unsupported operating system, please contact Ansible at http://support.ansible.com/. Management of other operating systems (nodes) is documented by the Ansible project itself and allows for a wider list.

Actual RAM requirements vary based on how many hosts Tower will manage simultaneously (which is controlled by the ``forks`` parameter in the job template or the system ``ansible.cfg`` file). To avoid possible resource conflicts, Ansible recommends 4 GB of memory per 100 forks. For example, if ``forks`` is set to 100, 4 GB of memory is recommended; if ``forks`` is set to 400, 16 GB of memory is recommended.

A larger number of hosts can of course be addressed, though if the fork number is less than the total host count, more passes across the hosts are required. These RAM limitations are avoided when using rolling updates or when using the provisioning callback system built into Tower, where each system requesting configuration enters a queue and is processed as quickly as possible; or in cases where Tower is producing or deploying images such as AMIs. All of these are great approaches to managing larger environments. For further questions, please contact http://support.ansible.com/.

The requirements for systems managed by Tower are the same as for Ansible at: http://docs.ansible.com/intro_getting_started.html
