# Q1: Write a function that accepts variable number of arguments and returns their sum. (args)


# def calculate_sum(*args):
#     return sum(args)


# print(calculate_sum(5,10,15))


# Q2: Implement a simple calculator supporting +, -, *, /
import operator
import functools

# Ask user which operation to perform
user_choice = input('What Do You Want To Perform: +, -, *, / :- ')

# Ask for numbers (comma-separated)
numbers = input("Enter numbers separated by commas: ")

# Convert the string input into a list of floats
num_list = [float(num.strip()) for num in numbers.split(',')]

# Define calculation functions
def calculate_addition(*args):
    return sum(args)

def calculate_subtraction(*args):
    # Subtract all subsequent numbers from the first
    return functools.reduce(operator.sub, args)

def calculate_multiplication(*args):
    return functools.reduce(operator.mul, args)

def calculate_division(*args):
    try:
        return functools.reduce(operator.truediv, args)
    except ZeroDivisionError:
        return "Error: Division by zero!"

# Perform operation based on user choice
if user_choice == '+':
    print("Result:", calculate_addition(*num_list))
elif user_choice == '-':
    print("Result:", calculate_subtraction(*num_list))
elif user_choice == '*':
    print("Result:", calculate_multiplication(*num_list))
elif user_choice == '/':
    print("Result:", calculate_division(*num_list))
else:
    print('Invalid Choice')
