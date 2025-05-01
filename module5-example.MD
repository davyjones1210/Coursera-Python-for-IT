The problem and solution
Imagine this scenario: Every month, you are handed a spreadsheet with hundreds of new hires. You are asked to create user accounts for all of them on a Linux server. The formatting on the spreadsheet looks like this:

username,password,real_name

amanda,,Amanda Alonso

ian,,Ian Ortega

eugene,,Eugene Konya

[...]

Notice that the password field is empty for all the records. This means you need to generate random passwords for each user and then create their accounts. You also want to write the passwords that you generate back to a new CSV file so that you can tell the new employees their passwords. 

This task isn’t difficult, but it is time-intensive if you create passwords and accounts for the hundreds of new hires one by one. Your solution is to automate this task in Python.

The script
To automate the task of creating passwords and accounts for all of these new hires, the script should do the following:

Read a list of new hires from users_in.csv.

Generate random 16-character passwords for each user.

Create each user account.

Write the spreadsheet back to users_out.csv with the new passwords.

Your tools
To help organize all the data, create accounts for the new hires, and create passwords for each new user, you first need to import a few standard Python libraries. 

import csv

This library helps read and write the CSV files. 

import secrets

This helps generate random passwords for each user account. 

import subprocess

This calls the useradd command, which creates and adds each user account.

from pathlib import Path   # to locate the data files

This library helps to locate the data files for each user account.

Getting started
After importing the libraries that help you execute your script, you need to get the current working directory and find the subdirectory where the CSV files are stored. Use cwd for “current working directory” and identify the path of the Python directory as a string: 