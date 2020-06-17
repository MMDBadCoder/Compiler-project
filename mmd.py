regex1 = '^/\*' + '([^\*]|\*[^/])*' + '\*/$'

import re

text = '/* /* hellow sclsdcsdc * *csd sdcskdc */'
obj = re.search(regex1, text)
print(obj)
