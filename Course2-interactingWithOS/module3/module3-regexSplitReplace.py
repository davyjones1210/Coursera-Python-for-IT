import re
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

import re
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

import re
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

import re
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

print(re.sub(r"([0-9]{3}\-[0-9]{3}\-[0-9]{3})", r"+1-\1", "Sabrina Green,802-867-5309,System Administrator"))

print(re.sub(r"#+", r"//", "### Start of program"))

print(re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", "My number is 212-345-9999."))