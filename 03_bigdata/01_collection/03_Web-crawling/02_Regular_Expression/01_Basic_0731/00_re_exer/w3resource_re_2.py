import re

"""
11. Write a Python program that matches a word at end of string, with optional punctuation. 
"""

# def text_match(text):
#     patterns = '\w+\S*$'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("The quick brown fox jumps over the lazy dog. "))
# print(text_match("The quick brown fox jumps over the lazy dog "))



"""
12. Write a Python program that matches a word containing 'z'.
"""

# def text_match(text):
#     patterns = '\w*z.\w*'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
#
# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("Python Exercises."))
#
# def find_match(string):
#     x = re.search("\w*z\w*", string)
#     if x:
#         print(x.group())
#         return "matched"
#     else:
#         print(x.group())
#         return "not matched"
#
# print(find_match("The quick brown fox jumps over the lazy dog."))

"""
13. Write a Python program that matches a word containing 'z', not start or end of the word. 
"""
#
# def text_match(text):
#     patterns = '\Bz\B'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("Python Exercises."))



"""
14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
"""

# def text_match(text):
#     patterns = '^[a-zA-Z0-9_]*$'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
#
# print(text_match("The quick brown fox jumps over the lazy dog."))
# print(text_match("Python_Exercises_1"))

"""
15. Write a Python program where a string will start with a specific number.
"""

# def match_num(string):
#     text = re.compile(r"^5")
#     if text.match(string):
#         return True
#     else:
#         return False
# print(match_num('5-2345861'))
# print(match_num('6-2345861'))

"""
16. Write a Python program to remove leading zeros from an IP address.  
"""

# ip = "216.08.094.196"
# string = re.sub('\.[0]*', '.', ip)
# print(string)


"""
17. Write a Python program to check for a number at the end of a string.  
"""

# def end_num(string):
#     text = re.compile(r".*[0-9]$")
#     if text.match(string):
#         return True
#     else:
#         return False
#
# print(end_num('abcdef'))
# print(end_num('abcdef6'))


# def pattern_match(pattern, s):
#     regexp_object = re.compile(pattern)
#     result = regexp_object.search(s)
#     # print(result)
#     if result:
#         print("Match Found")
#     else:
#         print("Match Not Found")
#
# pattern_match('\d$', '1232333s')

"""
18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
"""

# results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
# print("Number of length 1 to 3")
# for n in results:
#      print(n.group(0))

"""
19. Write a Python program to search some literals strings in a string.
"""
# patterns = ['fox', 'dog', 'horse']
# text = 'The quick brown fox jumps over the lazy dog.'
# for pattern in patterns:
#     print('Searching for "%s" in "%s" ->' % (pattern, text),)
#     if re.search(pattern,  text):
#         print('Matched!')
#     else:
#         print('Not Matched!')


"""
20. Write a Python program to search a literals string in a string and also find the location 
within the original string where the pattern occurs. 
"""

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))