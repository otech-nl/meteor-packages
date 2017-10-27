''' extract package data from README and write as a packages file '''

import re

from bs4 import BeautifulSoup
import markdown

with open('README.md') as readme:
    md = readme.read()
html = markdown.markdown(md)
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'id': 'packages'})

def handle_cell(packages, subject, cell):
    # for some reason markdown doesn't parse links in table cells properly,
    # so we do it by regexp:
    links = re.findall('\[(.*?)\]',cell.text)
    if len(links) == 0:
        return
    packages.append('# %s' % subject.text)
    packages += links
    packages.append('')


guide, extra = ['### packages from Meteor guide ###\n'], ['### extra packages ###\n']
for row in table.find_all('tr')[1:]:
    subject, guide_cell, extra_cell = row.find_all('td')
    if subject.text.lower() == 'out of the box':
        next
    handle_cell(guide, subject, guide_cell)
    handle_cell(extra, subject, extra_cell)

with open('packages', 'w') as out:
    out.write('\n'.join(guide + extra))