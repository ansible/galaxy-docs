import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', '../'))
from common.source.conf import *

project = u'Ansible Galaxy Guide'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = 'Ansible Galaxy Guide'

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'Galaxy Guide'

htmlhelp_basename = 'AnsibleGalaxyGuidedoc'

latex_documents = [
  (master_doc, 'AnsibleGalaxyGuide.tex', u'Ansible Galaxy Guide',
   u'Red Hat, Inc.', 'manual'),
]

man_pages = [
    (master_doc, 'ansiblegalaxyGuide', u'Ansible Galaxy Guide',
     [author], 1)
]

texinfo_documents = [
  (master_doc, 'AnsibleGalaxyGuide', u'Ansible Galaxy Guide',
   author, 'Ansible, Inc./Red Hat, Inc.', 'One line description of project.',
   'Miscellaneous'),
]
