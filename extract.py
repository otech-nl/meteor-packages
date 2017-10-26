''' extract package names from the Meteor guide and write them to packages-guide
    Uses the content folder of https://github.com/meteor/guide '''

from collections import defaultdict
import os
import sys

import markdown
from bs4 import BeautifulSoup


def get_links_from_markdown(path, name):
    try:
        with open(path, 'r') as file:
            md = file.read()
            html = markdown.markdown(md)
            soup = BeautifulSoup(html, 'html.parser')
            return soup.find_all('a')
    except PermissionError:
        print('Could not open "%s"' % path)
    except UnicodeDecodeError:
        print('Could not proccess "%s"' % path)
    return []


def get_guide_packages(src_dir='content'):
    if len(sys.argv) > 1:
        src_dir = sys.argv[1]
    subjects = defaultdict(list)
    for entry in os.scandir(src_dir):
        name = entry.name[:-3]
        for link in get_links_from_markdown(entry.path, name):
            if len(link.text.split(':')) == 2:  # packages only
                subjects[name].append(link.text)
    return subjects


def write_packages(packages, path='packages-guide'):
    with open(path, 'w') as out:
        out.write('\n# packages from http://guide.meteor.com\n')
        for subject, links in packages.items():
            out.write('\n# %s\n' % subject)
            for link in links:
                out.write('%s\n' % link)


if __name__ == '__main__':
    GUIDE = get_guide_packages()
    write_packages(GUIDE)
