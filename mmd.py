regex1 = '^/\*' + '([^\*]|\*[^/])*' + '\*/$'

import re

text = '''/* /* hellow sclsdcsdc * *
sdc
sdcsd
csdc
sdccsd sdcskdc */'''
obj = re.search(regex1, text)
print(obj)
