import pdb


def add_numbers(a, b):
    pdb.set_trace()  # This will set a breakpoint in the code
    result = a + b
    return result


print(add_numbers(3, 4))

# If your program crashes, you can use pdb to inspect 
# its state at the time of the crash. 
# Run your script with: 
# python -m pdb your_script.py