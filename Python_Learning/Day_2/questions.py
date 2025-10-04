# Q1: Convert Celsius to Fahrenheit.

Celsius_temp = int(input('Enter the temperatur in celsius like... 23/32/40: '))

Fahrenheit_temp = Celsius_temp * (9/5) + 32
print(f'After Converting Celsius Temperatur into Fahrenheit the result is {Fahrenheit_temp}°F')




# Q2: Calculate factorial using a loop

def calculate_fact(num):
    if num < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact



print(calculate_fact(5))
print(calculate_fact(1))
print(calculate_fact(0))