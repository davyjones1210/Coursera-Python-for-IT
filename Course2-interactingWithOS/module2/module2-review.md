Prerequisites
We have created the employee list for you. Navigate to the data directory using the following command:

cd data
Copied!
To find the data, list the files using the following command:

ls
Copied!
You can now see a file called employees.csv, where you will find your data. You can also see a directory called scripts. We will write the python script in this directory.

To view the contents of the file, enter the following command:

cat employees.csv
Copied!
Let's start by writing the script. You will write this python script in the scripts directory. Go to the scripts directory by using the following command:

cd ~/scripts
Copied!
Create a file named generate_report.py using the following command:

nano generate_report.py
Copied!
You will write your python script in this generate_report.py file. This script begins with a line containing the #! character combination, which is commonly called hash bang or shebang, and continues with the path to the interpreter. If the kernel finds that the first two bytes are #! then it uses the rest of the line as an interpreter and passes the file as an argument. We will use the following shebang in this script:

#!/usr/bin/env python3
Copied!
Convert employee data to dictionary
The goal of the script is to read the CSV file and generate a report with the total number of people in each department. To achieve this, we will divide the script into three functions.

Let's start with the first function: read_employees(). This function receives a CSV file as a parameter and returns a list of dictionaries from that file. For this, we will use the CSV module.

The CSV module uses classes to read and write tabular data in CSV format. The CSV library allows us to both read from and write to CSV files.

Now, import the CSV module.

import csv
Copied!
Define the function read_employees. This function takes file_location (path to employees.csv) as a parameter.

def read_employees(csv_file_location):
Copied!
Open the CSV file by calling open and then csv.DictReader.

DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.

We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

Dialect classes can be registered by name so that callers of the CSV module don't need to know the parameter settings in advance. We will now register a dialect empDialect.

  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
Copied!
The main purpose of this dialect is to remove any leading spaces while parsing the CSV file.

The function will look similar to:

  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
Copied!
You now need to iterate over the CSV file that you opened, i.e., employee_file. When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).

Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.

  employee_list = []
  for data in employee_file:
    employee_list.append(dict(data))
Copied!
Now return this list.

  return employee_list
Copied!
To test the function, call the function and save it to a variable called employee_list. Pass the path to employees.csv as a parameter to the function. Print the variable employee_list to check whether it returns a list of dictionaries.

employee_list = read_employees('<file_location>')
print(employee_list)
Copied!
Replace <file_location> with the path to the employees.csv (this should look similar to the path /home/student/data/employees.csv).


Chromebook users: Instructions for saving a file in the nano editor
keyboard_arrow_right
Save the file by clicking Ctrl-o, Enter, and Ctrl-x.

For the file to run it needs to have execute permission (x). Let's update the file permissions and then try running the file. Use the following command to add execute permission to the file:

chmod +x generate_report.py
Copied!
Now test the function by running the file using the following command:

./generate_report.py
Copied!
The list employees_list within the script should return the list of dictionaries as shown below.

[{'Full Name': 'Audrey Miller', 'Username': 'audrey', 'Department': 'Development'}, {'Full Name': 'Arden Garcia', 'Username': 'ardeng', 'Department': 'Sales'}, {'Full Name': 'Bailey Thomas', 'Username': 'baileyt', 'Department': 'Human Resources'}, {'Full Name': 'Blake Sousa', 'Username': 'sousa', 'Department': 'IT infrastructure'}, {'Full Name': 'Cameron Nguyen', 'Username': 'nguyen', 'Department': 'Marketing'}, {'Full Name': 'Charlie Grey', 'Username': 'greyc', 'Department': 'Development'}, {'Full Name': 'Chris Black', 'Username': 'chrisb', 'Department': 'User Experience Research'}, {'Full Name': 'Courtney Silva', 'Username': 'silva', 'Department': 'IT infrastructure'}, {'Full Name': 'Darcy Johnsonn', 'Username': 'darcy', 'Department': 'IT infrastructure'}, {'Full Name': 'Elliot Lamb', 'Username': 'elliotl', 'Department': 'Development'}, {'Full Name': 'Emery Halls', 'Username': 'halls', 'Department': 'Sales'}, {'Full Name': 'Flynn McMillan', 'Username': 'flynn', 'Department': 'Marketing'}, {'Full Name': 'Harley Klose', 'Username': 'harley', 'Department': 'Human Resources'}, {'Full Name': 'Jean May Coy', 'Username': 'jeanm', 'Department': 'Vendor operations'}, {'Full Name': 'Kay Stevens', 'Username': 'kstev', 'Department': 'Sales'}, {'Full Name': 'Lio Nelson', 'Username': 'lion', 'Department': 'User Experience Research'}, {'Full Name': 'Logan Tillas', 'Username': 'tillas', 'Department': 'Vendor operations'}, {'Full Name': 'Micah Lopes', 'Username': 'micah', 'Department': 'Development'}, {'Full Name': 'Sol Mansi', 'Username': 'solm', 'Department': 'IT infrastructure'}]
Click Check my progress to verify the objective.