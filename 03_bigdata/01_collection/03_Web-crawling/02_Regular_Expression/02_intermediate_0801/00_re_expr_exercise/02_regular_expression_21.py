import re

"""
21. Write a Python program to find the substrings within a string.
"""

# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
#
# for match in re.findall(pattern, text):
#     print('Found "%s"' % match)

"""
22. Write a Python program to find the occurrence and position of the substrings within a string.
"""
# text = 'Python exercises, PHP exercises, C# exercises'
# pattern = 'exercises'
#
# for match in re.finditer(pattern, text):
#     s = match.start()
#     e = match.end()
#     print('Found "%s" at %d:%d' % (text[s:e], s, e))


"""
23. Write a Python program to replace whitespaces with an underscore and vice versa.
"""
# text = 'Python Exercises'
# text =  text.replace (" ", "_")
# print(text)
#
# text =text.replace ("_", " ")
# print(text)

"""
24. Write a Python program to extract year, month and date from a an url.
"""

# def extract_date(url):
#     return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
#
# url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
# print(extract_date(url1))

"""
25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
"""
#
# def change_date_format(dt):
#     return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\g<3>-\g<2>-\g<1>', dt)
#     # return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
#
# dt1 = "2019-08-01"
# print("Original date in YYY-MM-DD Format: ", dt1)
# print("New date in DD-MM-YYYY Format: ", change_date_format(dt1))

"""
26. Write a Python program to match if two words from a list of words starting with letter 'P'.
"""
# # Sample strings.
# words = ["Python PHP", "Java JavaScript", "c c++"]
#
# for w in words:
#         m = re.match("(P\w+)\W(P\w+)", w)
#         # Check for success
#         if m:
#             print(m.groups())

"""
27. Write a Python program to separate and print the numbers of a given string.
"""
# # Sample string.
# text = "Ten 10, Twenty 20, Thirty 30"
# result = re.split("\D+", text)   # \D 숫자가 아닌것과  매치  [^0-9]와 같은 의미
# # Print results.
# for element in result:
#     print(element)

"""
28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
"""
# # Input.
# text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# #find all the words starting with 'a' or 'e'
# list = re.findall("[ae]\w+", text)

"""
29. Write a Python program to separate and print the numbers and their position of a given string.
"""
# # Input.
# text = "The following example creates an ArrayList with a capacity of 50 elements. " \
#        "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#
# for m in re.finditer("\d+", text):
#     print(m.group(0))
#     print("Index position:", m.start())

"""
30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
"""
# street = '21 Ramkrishna Road'
# print(re.sub('Road$', 'Rd.', street))

"""
31. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
"""
# text = 'Python Exercises, PHP exercises.'
# print(re.sub("[ ,.]", ":", text))  # 공백, 쉼표, 점을 콜론으로

"""
32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
"""
# text = 'Python Exercises, PHP exercises.'
# print(re.sub("[ ,.]", ":", text, 2))  # 공백, 쉼표, 점을 콜론으로, 최대 2번

"""
33. Write a Python program to find all five characters long word in a string.
"""
# text = 'The quick brown fox jumps over the lazy dog.'
# print(re.findall(r"\b\w{5}\b", text))

"""
34. Write a Python program to find all three, four, five characters long words in a string.
"""
# text = 'The quick brown fox jumps over the lazy dog.'
# print(re.findall(r"\b\w{3,5}\b", text))

"""
35. Write a Python program to find all words which are at least 4 characters long in a string.
"""
# text = 'The quick brown fox jumps over the lazy dog.'
# print(re.findall(r"\b\w{4,}\b", text))

"""
36. Write a python program to convert camel case string to snake case string.
"""
# def camel_to_snake(text):
#     str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
#     print(str1)
#     return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
#
# print(camel_to_snake('PythonExercises'))

"""
37. Write a python program to convert snake case string to camel case string.
"""
# def snake_to_camel(word):
#     return ''.join(x.capitalize() or '_' for x in word.split('_'))
#
# print(snake_to_camel('python_exercises'))

"""
38. Write a Python program to extract values between quotation marks of a string.
"""
# text1 = '"Python", "PHP", "Java"'
# print(re.findall(r'"(.*?)"', text1))

"""
39. Write a Python program to remove multiple spaces in a string.
"""
# text1 = 'Python      Exercises'
# print("Original string:",text1)
# print("Without extra spaces:", re.sub(' +',' ',text1))

"""
40. Write a Python program to remove all whitespaces from a string.
"""
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+', '',text1))