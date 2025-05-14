import re
result = re.search(r"aza", "plaza")
print(result)

import re
result = re.search(r"aza", "bazaar")
print(result)

import re
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))

import re
print(re.search(r"p.ng", "penguin"))

import re
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

import re
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))