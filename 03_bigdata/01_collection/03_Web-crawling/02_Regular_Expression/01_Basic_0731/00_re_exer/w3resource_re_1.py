import re

"""
1. 문자열에 특정문자 집합(이경우 azAZO9)만 들어 있는 지 확인하는 프로그램
"""

# def is_specific_char(string):
#     p = re.compile('[a-zA-Z0-9]')
#     m = p.search(string)
#     return bool(m)
#
# print(is_specific_char("ABCDEFabcdef123450"))
# print(is_specific_char("*&%@#!}{"))


# string = "ABCDEF012345abcdef"
# if re.findall('\W', string):
#     print ("Not Matched")
# else:
#     print("Matched")

"""
2. Write a Python program that matches a string that has an a followed by zero or more b's. 
"""

# def text_match(text):
#     patterns = 'ab*?'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
#
# print(text_match("ac"))
# print(text_match("abc"))
# print(text_match("abbc"))
#
# string="abbcacb"
# x=re.findall("ab*",string)
# if x:
# print("Matched")
# else:
# print("Not Matched")

"""
3. Write a Python program that matches a string that has an a followed by one or more b's. 
"""
#
# def text_match(text):
#     patterns = 'ab+?'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("ab"))
# print(text_match("abc"))
#
#
# string= "abbcad"
# x=re.findall("ab+",string)
# if x:
#     print("matched")
# else:
#     print("Not Matched")
#
# print(x)

"""
4. Write a Python program that matches a string that has an a followed by zero or one 'b'.  
"""

# def text_match(text):
#     patterns = 'ab?'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("ab"))
# print(text_match("abc"))
# print(text_match("abbc"))
# print(text_match("aabbc"))
#
#
# def find_match(string):
#     x = re.findall("ab{0}|ab{1}", string)
#
#     if x:
#         return "Matched"
#     else:
#         return "Not Matched"
#
# print(find_match("ab"))
# print(find_match("abc"))
# print(find_match("abbc"))
# print(find_match("aabbcc"))
# print(find_match("a"))

"""
5. Write a Python program that matches a string that has an a followed by three 'b'.
"""

# def text_match(text):
#     patterns = 'ab{3}?'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
#
# print(text_match("abbb"))
# print(text_match("aabbbbbc"))

# def find_match(string):
#     x=re.findall("ab{3}", string)
#     if x:
#         return "matched"
#     else:
#         return "Not Matched"
#
# print(find_match('abbb'))
# print(find_match("aabbbbc"))

"""
6. Write a Python program that matches a string that has an a followed by two to three 'b'. 
"""

# def text_match(text):
#     patterns = 'ab{2,3}?'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("ab"))
# print(text_match("aabbbbbc"))
#
#
# matcher = re.finditer('ab{2,3}', 'abbbacbabbasd')
# count = 0
# for m in matcher:
#     count +=1
#     print("start: {} group: {}".format(m.start(),m.group()))
#     print("The number of occurances are: ", count)

"""
7. Write a Python program to find sequences of lowercase letters joined with a underscore. 
"""
#
# def text_match(text):
#     patterns = '^[a-z]+_[a-z]+$'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("aab_cbbbc"))
# print(text_match("aab_Abbbc"))
# print(text_match("Aaab_abbbc"))
#
# def find_match(string):
#     x=re.findall("^[a-z]+_[a-z]+$", string)
#     if x:
#         return "Matched"
#     else:
#         return "Not Matched"
#
# print(find_match("aab_cbbbc"))
# print(find_match("aab_Abbbc"))
# print(find_match("Aaab_abbbc"))

"""
8. Write a Python program to find sequences of one upper case letter followed by lower case letters.
"""
#
# def text_match(text):
#     # patterns = '^[a-z]+_[a-z]+$'
#     patterns = '[^a-z]*_[a-z]+$'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("aab_cbbbc"))
# print(text_match("aab_Abbbc"))
# print(text_match("Aaab_abbbc"))

# def find_match(string):
#     x=re.findall("[A-Z][a-z]+", string)
#     if x:
#         return "Matched"
#     else:
#         return "Not Matched"
#
# print(find_match('Raghavendra'))
# print(find_match("samara"))
# print(find_match("VINOD"))

"""
9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
"""

# def text_match(text):
#     patterns = 'a.*?b$'
#     if re.search(patterns, text):
#         return 'Found a match!'
#     else:
#         return ('Not matched!')
#
# print(text_match("aabbbbd"))
# print(text_match("aabAbbbc"))
# print(text_match("accddbbjjjb"))

"""
10. Write a Python program that matches a word at the beginning of a string.
"""

def text_match(text):
    patterns = '^\w+'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))

def text_check(string):
    string = re.match(r'\w+', string)
    return string.group()

print(text_check('Hello, world!'))