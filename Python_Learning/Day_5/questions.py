# Q1: Write a program to check if two strings are anagrams

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted letters are the same
    return sorted(str1) == sorted(str2)


if are_anagrams("listen", "silent"):
    print('Your words are anagrams.')
else:
    print('Your Words are not anagrams.')




# Q2: Create a function to calculate frequency of characters in a string.

def calculate_freq(text):
    count_dict = {}
    for i in range(len(text)):
        if text[i] not in count_dict:
            count_dict[text[i]] = 1
        else:
            count_dict[text[i]] += 1

    print(count_dict)


calculate_freq('Shakeeb')