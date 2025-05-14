import subprocess
result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True, text=True)
print(result.stdout)



result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True)
print(result.returncode)



result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True)
print(result.stdout)



result = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())

import subprocess
result = subprocess.run(["del", "does_not_exist"], capture_output=True, shell=True)


import subprocess
result = subprocess.run(["del", "does_not_exist"], capture_output=True, shell=True)
print(result.returncode)

import subprocess
result = subprocess.run(["del", "does_not_exist"], capture_output=True, shell=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
