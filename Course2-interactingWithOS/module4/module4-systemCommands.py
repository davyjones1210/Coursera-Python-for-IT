import subprocess
import time
from datetime import datetime
print(datetime.now())

time.sleep(2)

import subprocess
print(datetime.now())
result = subprocess.run(["dir", "this_file_does_not_exist"], shell=True, capture_output=True, text=True)
print(result.returncode)


