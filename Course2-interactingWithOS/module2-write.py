with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")


with open("sample_data/declaration.txt", "rt") as textfile:
    for line in textfile:
        print(line)

f = open("sample_data/declaration.txt", "rw+")
         
f.write("We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.")


f = open('workfile', 'w', encoding="utf-8")