# Q1: Write a program that takes a user’s name and prints a greeting.

name = input('Enter Your Name: ').capitalize()
print(f'Good Morning {name}')




# Q2: Check if a number is even or odd.
def even_odd_check(num):
    if num % 2 == 0:
        print(f'{num} is Even Number')
    else:
        print(f'{num} is Odd Number')



even_odd_check(3)
even_odd_check(6)