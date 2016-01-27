Tower Licensing, Updates, and Support
---------------------------------------

.. index::
   single: license

Tower is a proprietary software product and is licensed on an annual subscription basis.

Ansible is an open source software project and is licensed under the GNU General Public License version 3, as detailed in the Ansible source code: https://github.com/ansible/ansible/blob/devel/COPYING

Support
==========

.. index::
    single: support

Ansible offers support for paid Enterprise customers seeking help with the Tower product. If you or you company has paid for a license of |at|, you can contact Ansible's support team at http://support.ansible.com/. To better understand the levels of support which match your Tower license, refer to
:ref:`license-types`.

If you are using Ansible core and are having issues, you should reach out to the "ansible-devel" mailing list or file an issue on the Github project page at https://github.com/ansible/ansible/issues/.

All of Ansible's community and OSS info can be found here: https://docs.ansible.com/ansible/community.html

.. _trial-licenses:

Trial Licenses
=====================

.. index::
   single: license; trial


While a license is required for Tower to run, there is no fee for managing up to 10 hosts. Additionally, trial licenses are available for exploring Tower with a larger number of hosts.

Trial licenses for Tower are available at: http://ansible.com/license 

To acquire a license for additional servers, visit: http://www.ansible.com/pricing/ 

.. _license-types:

License Types
=======================

.. index:: 
   single: updates
   single: support
   single: license; types

Tower is licensed at various levels as an annual subscription. Whether you have a small business or a mission-critical environment, Ansible is ready to simplify your IT work-flow. 

- Basic 
    - Manage smaller environments (up to 250 nodes)
    - 30 days of initial web support through http://support.ansible.com/, for installation and setup 
    - Maintenance and upgrades included

- Enterprise 
    - Manage any size environment
    - Enterprise 8x5 support and SLA (4 hour critical incident response)
    - Phone and web support
    - Support for Ansible core included 
    - Maintenance and upgrades included

- Premium 
    - Manage any size environment, including mission-critical environments
    - Premium 24x7 support and SLA (4 hour critical incident response, 8 hour non-critical incident response)
    - Phone and web support
    - Support for Ansible core included 
    - Maintenance and upgrades included
 
All subscriptions include regular updates and releases of both Ansible Tower and Ansible core. 

For more information, contact Ansible at http://support.ansible.com/ or at http://www.ansible.com/pricing/.


License Features
=================================

.. index:: 
   single: license; features

.. note::

    |at| version 2.2 introduced a separation of features for Basic versus Enterprise or Premium licenses. 

The following list of features are available for all new Enterprise or Premium license users:

- Custom rebranding for login (*added in Ansible Tower 2.4.0*)
- SAML and RADIUS Authentication Support (*added in Ansible Tower 2.4.0*)
- Multi-Organization Support
- Activity Streams
- Surveys
- LDAP Support
- High Availability
- System Tracking  (*added in Ansible Tower 2.2.0*)

Users with an existing license (Basic, Enterprise, or Premium) can access all of the features included with the |at| release at the time of their purchase. For example, users with an existing Basic license issued before |at| 2.2 was released would have access to all the above features, except for System Tracking--which was introduced in |at| 2.2.

Enterprise license users with versions of |at| prior to 2.2 must import a new license file to enable System Tracking. 


Tower Component Licenses
==============================

.. index::
    pair: licenses; components
    pair: licenses; RPM files
    pair: licenses; DEB files
    pair: licenses; installation bundle


|at| includes some open source components. Ansible, Inc. supports Tower’s use of and interactions with these components for both development and production purposes, subject to applicable terms and conditions. Unless otherwise agreed to in writing, the use of |at| is subject to the Ansible Software Subscription and Services Agreement located at http://www.ansible.com/subscription-agreement.  |at| is a proprietary product offered by Ansible, Inc. and its use is not intended to prohibit the rights under any open source license.

To view the license information for the components included within |at|, refer to ``/usr/share/doc/ansible-tower-<version>/README`` where ``<version>`` refers to the version of |at| you have installed.

To view a specific license, refer to ``/usr/share/doc/ansible-tower-<version>/*.txt``, where ``*`` is replaced by the license file name to which you are referring.




