import os
import pkg_resources

FORTUNES = []
INPUT_FILE = pkg_resources.resource_filename(__package__, 'fortune.txt')

with open(INPUT_FILE) as f:
    fortune = ''
    for line in f.readlines():
        if '%' in line:
            FORTUNES.append(fortune)
            fortune = ''
        else:
            fortune += '\n' + str(line)

FORTUNES.sort()
__all__ = ['FORTUNES']
