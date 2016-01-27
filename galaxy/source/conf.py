import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Ansible Galaxy Cookbook'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Ansible Galaxy Cookbook'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Galaxy Cookbook'

htmlhelp_basename = 'AnsibleGalaxyCookbookdoc'

latex_documents = [
  (master_doc, 'AnsibleGalaxyCookbook.tex', u'Ansible Galaxy Cookbook',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'ansiblegalaxycookbook', u'Ansible Galaxy Cookbook',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AnsibleGalaxyCookbook', u'Ansible Galaxy Cookbook',
   author, 'Ansible, Inc./Red Hat, Inc.', 'One line description of project.',
   'Miscellaneous'),
]
