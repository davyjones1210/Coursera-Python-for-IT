# try:
#     # code that might raise an exception
# except SomeExceptionType:
#     # handle the exception

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You tried to divide by zero.")

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        print("The list is empty. Cannot calculate the average.")
        return None
    

class InvalidInputError(Exception):
    pass


class EmptyInputError(Exception):
    pass


def calculate_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        raise InvalidInputError(f"Expected a list or tuple, but got {type(numbers)}")
    except ZeroDivisionError:
        raise EmptyInputError("The list is empty. Cannot calculate the average.")
    finally:
        print("Execution of calculate_average function completed.")

    