import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["C:\\MyApp\\", my_env["PATH"]])

try:
    result = subprocess.run(["myapp"], env=my_env)
    print(result.returncode)
except FileNotFoundError:
    print("The 'myapp' executable was not found. Please check the PATH or the executable name.")

# Orignial BASH code:
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
print(result.returncode)
print(result.stdout)