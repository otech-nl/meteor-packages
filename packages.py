''' extract package data from README and write is as a packages file '''

from bs4 import BeautifulSoup

with open('README.html') as readme:
    html = readme.read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table', {'id': 'packages'})

def handle_cell(packages, subject, cell):
    links = cell.find_all('a')
    if subject.text.lower() == 'out of the box' or len(links) == 0:
        return
    packages.append('# %s' % subject.text)
    packages += [a.text for a in links]
    packages.append('')


guide, extra = ['# packages from Meteor guide\n'], ['# extra packages\n']
for row in table.find_all('tr')[1:]:
    subject, guide_cell, extra_cell = row.find_all('td')
    handle_cell(guide, subject, guide_cell)
    handle_cell(extra, subject, extra_cell)

with open('packages', 'w') as out:
    out.write('\n'.join(guide + extra))