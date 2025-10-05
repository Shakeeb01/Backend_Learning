# Q1: Create a function that checks if a string is a palindrome.

def check_string_palindrome(text):
    # Normalize case (lowercase all letters)
    text = text.lower()
    reverse_text = ''

    for i in range(len(text)-1,-1,-1):
        reverse_text += text[i]
    
    if reverse_text == text:
        print('Your String is Palindrome')
    else:
        print('Your String is Not Palindrome')


check_string_palindrome('Heh')




# Q2: Write a program to merge two dictionaries. 
Author = {
    "name": "Ali",
    "age": 20,
    "email": 'testing@gmail.com',
}

Book = {
    "title": "The Great Gatsby",
    "year_published": 1925,
    "genre": "Novel",
}

merged_dictionaries = Author | Book

print(merged_dictionaries)
