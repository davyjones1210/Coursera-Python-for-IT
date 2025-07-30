#!/usr/bin/env python3

import re
import csv

# Initialize dictionaries
error_counts = {}
user_stats = {}

# Parse the syslog.log file
with open("syslog.log", "r") as f:
    for line in f:
        # Check for ERROR messages
        error_match = re.search(r"ERROR ([\w ]*) ", line)
        if error_match:
            error_message = error_match.group(1).strip()
            if error_message not in error_counts:
                error_counts[error_message] = 0
            error_counts[error_message] += 1

        # Check for INFO and ERROR messages with usernames
        user_match = re.search(r"\((.*)\)", line)
        if user_match:
            username = user_match.group(1).strip()
            if username not in user_stats:
                user_stats[username] = {"INFO": 0, "ERROR": 0}

            if "INFO" in line:
                user_stats[username]["INFO"] += 1
            elif "ERROR" in line:
                user_stats[username]["ERROR"] += 1

# Sort the error dictionary by count (most common to least common)
sorted_errors = sorted(error_counts.items(), key=lambda item: item[1], reverse=True)

# Insert column names into the sorted error list
sorted_errors.insert(0, ("Error", "Count"))

# Sort the user dictionary by username
sorted_users = sorted(user_stats.items())

# Convert the sorted user data into a list of lists
user_data = [("Username", "INFO", "ERROR")]
for username, counts in sorted_users:
    user_data.append([username, counts["INFO"], counts["ERROR"]])

# Write the error report to a CSV file
with open("error_message.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sorted_errors)

# Write the user statistics report to a CSV file
with open("user_statistics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(user_data)