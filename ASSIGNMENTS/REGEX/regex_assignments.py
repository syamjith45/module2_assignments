# Write a Python program that matches a string that has an a followed by zero or more b's.

# import re

# # Define the pattern
# pattern = r'ab*'

# # Test strings
# test_strings = ["a", "ab", "abb", "ac", "b", "bb", "bc"]

# # Iterate through the test strings
# for string in test_strings:
#     if re.match(pattern, string):
#         print(f"'{string}' matches the pattern.")
#     else:
#         print(f"'{string}' does not match the pattern.")

#  Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

# import re

# # Define the pattern to match only a-z, A-Z, and 0-9
# pattern = r'^[a-zA-Z0-9]+$'

# # Test strings
# test_strings = ["Hello123", "GoodMorning", "Test@123", "12345", "ABCD", "1234$", ""]

# # Iterate through the test strings
# for string in test_strings:
#     if re.match(pattern, string):
#         print(f"'{string}' contains only a-z, A-Z, and 0-9.")
#     else:
#         print(f"'{string}' does not contain only a-z, A-Z, and 0-9.")



# Write a python program that matches a string only contain 0-9 as the characters and it must be at least 1 char in length and no more than 6.
# import re

# # Define the pattern to match only digits (0-9) with a length between 1 and 6 characters
# pattern = r'^[0-9]{1,6}$'

# # Test strings
# test_strings = ["12345", "7", "890", "123456", "12a", "", "1234567"]

# # Iterate through the test strings
# for string in test_strings:
#     if re.match(pattern, string):
#         print(f"'{string}' matches the pattern.")
#     else:
#         print(f"'{string}' does not match the pattern.")

# # . Write a Python program to find sequences of lowercase letters joined with  an underscore.

# import re

# # Define the pattern to find sequences of lowercase letters joined with an underscore
# pattern = r'[a-z]+_[a-z]+'

# # Test string
# text = "hello_world is_a_test abc_def_ghi not_valid_12"

# # Find and print all matching sequences
# matches = re.findall(pattern, text)
# if matches:
#     print("Sequences of lowercase letters joined with an underscore:")
#     for match in matches:
#         print(match)
# else:
#     print("No matching sequences found.")
#  Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# import re

# # Define the pattern to match 'a' followed by anything and ending in 'b'
# pattern = r'a.*b$'

# # Test strings
# test_strings = ["apple and banana", "a quick brown fox jumps over the lazy dog b", "cabbage", "ab", "a123b"]

# # Iterate through the test strings
# for string in test_strings:
#     if re.search(pattern, string):
#         print(f"'{string}' matches the pattern.")
#     else:
#         print(f"'{string}' does not match the pattern.")


# A website requires the users to input username and password to register.         Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
# import re
# def is_valid_password(password):
#     if 6<=len(password) <=12:
#         if re.search(r'[a-z]',password):
#             if re.search(r'[A-Z]',password):
#                 if re.search(r'[0-9]',password):
#                     if re.search(r'[&#@]',password):
#                         return True
#     return False

# password = input("Enter your password: ")
# if is_valid_password(password):
#     print("Valid password.")
# else:
#     print("Invalid password. Please follow the password criteria.")





import re

txt = "abcnjbfhfewhbvjhfvbeh1ihhwevfjhb"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("a.*", txt)

print(x)