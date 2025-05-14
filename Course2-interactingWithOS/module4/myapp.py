#!/usr/bin/env python3
import os
import subprocess

my_env = os.environ.copy()
print(my_env["PATH"])
my_env["PATH"] = os.pathsep.join(["C:\\Python Projects\\Coursera-Python-for-IT\\Course2-interactingWithOS\\module4\\myapp", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
print(result.returncode)
print(result.stdout)