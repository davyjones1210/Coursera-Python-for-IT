#!/usr/bin/env python3
import os
import subprocess

# Copy the current environment variables
my_env = os.environ.copy()

# Print the current PATH
print("my_env type:")
print(type(my_env))

print("Raw my_env:")
print(my_env)

# Add a custom directory to the PATH
custom_path = "C:\\Python Projects\\Coursera-Python-for-IT\\Course2-interactingWithOS\\module4\\myapp"
my_env["PATH"] = os.pathsep.join([custom_path, my_env["PATH"]])

# Print the updated PATH
# print("\nUpdated PATH:")
# print(my_env["PATH"])

# Create a test environment variable
my_env["MY_CUSTOM_VAR"] = "HelloWorld"

# Run a simple command to verify the environment
try:
    result = subprocess.run(
        ["echo", "%MY_CUSTOM_VAR%"],  # Use 'echo' to print the custom variable
        env=my_env,
        capture_output=True,
        text=True,
        shell=True  # Required for Windows to interpret environment variables
    )
    print("\nCommand Output:")
    print(result.stdout)
    print("Return Code:", result.returncode)
    print("Result object:", result)
except FileNotFoundError:
    print("The command could not be found. Ensure the executable exists in the PATH.")