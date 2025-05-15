#!/bin/env/python3

import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((.+)\)$"
    result = re.search(pattern, line)
    print(result[1])


# chmod +x check_cron.py 
# ./check_cron.py syslog 


# cd Course2-interactingWithOS/module4