# Q1: Write a program to remove duplicates from a list while preserving order.

numbers = [0,1,2,3,12,13,1,3,4,5,0]

unique_elements_list = []

for i in range(len(numbers)):
    if numbers[i] not in unique_elements_list:
        unique_elements_list.append(numbers[i])


print(unique_elements_list)



# Q2: Implement a function to flatten a nested list.

def flatten_nested_list(numbers):
    flatten_list = []

    for i in numbers:
        for j in i:
            flatten_list.append(j)

    return flatten_list


numbers = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

result = flatten_nested_list(numbers)
print(result)