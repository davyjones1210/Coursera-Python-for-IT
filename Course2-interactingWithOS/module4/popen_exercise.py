import subprocess

# Using Popen for asynchronous behavior: 

process = subprocess.Popen(['sleep', '10'])

message_1 = "The process is running in the background..."

# Give it a couple of seconds to demonstrate the asynchronous behavior

import time

time.sleep(5)

# Check if the process has finished

if process.poll() is None:

	message_2 = "The process is still running."

else:

	message_2 = "The process has finished."

print(message_1, message_2)