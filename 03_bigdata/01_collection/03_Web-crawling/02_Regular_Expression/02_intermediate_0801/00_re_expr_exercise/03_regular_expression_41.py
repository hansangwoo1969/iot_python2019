import re

"""
41. Write a Python program to remove everything except alphanumeric characters from a string.
"""
# text1 = '**//Python Exercises// - 12. '
# pattern = re.compile('[\W_]+')
# print(pattern.sub('', text1))

"""
42. Write a Python program to find urls in a string.
"""
# text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
# print("Original string: ",text)
# print("Urls: ",urls)

"""
43. Write a Python program to split a string at uppercase letters.
"""
# text = "PythonTutorialAndExercises"
# print(re.findall('[A-Z][^A-Z]*', text))

"""
44. Write a Python program to do a case-insensitive string replacement. 
"""
# text = "PHP Exercises"
# print("Original Text: ", text)
# redata = re.compile(re.escape('php'), re.IGNORECASE)
# new_text = redata.sub('Python', 'PHP Exercises')
# print("Using 'php' replace PHP")
# print("New Text: ",new_text)

"""
45. Write a Python program to remove the ANSI escape sequences from a string.
"""
# text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
# print("Original Text: ",text)
# reaesc = re.compile(r'\x1b[^m]*m')
# new_text = reaesc.sub('', text)
# print("New Text: ",new_text)


"""
46. Write a Python program to find all adverbs and their positions in a given sentence.
"""
# text = "Clearly, he has no excuse for such behavior."
# for m in re.finditer(r"\w+ly", text):
#     print('%d-%d: %s' % (m.start(), m.end(), m.group(0)))

"""
47. Write a Python program to split a string with multiple delimiters.
"""
# text = 'The quick brown\nfox jumps*over the lazy dog.'
# print(re.split('; |, |\*|\n',text))
# print(a)

"""
48. Write a Python program to check a decimal with a precision of 2.
"""
# def is_decimal(num):
#     import re
#     dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
#     result = dnumre.search(num)
#     return bool(result)
#
# print(is_decimal('123.11'))
# print(is_decimal('123.1'))
# print(is_decimal('123'))
# print(is_decimal('0.21'))

"""
49. Write a Python program to remove words from a string of length between 1 and a given number. 
"""
# text = "The quick brown fox jumps over the lazy dog."
# # remove words between 1 and 3
# shortword = re.compile(r'\W*\b\w{1,3}\b')
# print(shortword.sub('', text))

"""
50. Write a Python program to remove the parenthesis area in a string. 
"""
# items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# for item in items:
#     print(re.sub(r" ?\([^)]+\)", "", item))

"""
51. Write a Python program to insert spaces between words starting with capital letters.

"""
# def capital_words_spaces(str1):
#   return re.sub(r"(\w)([A-Z])", r"\g<1> \g<2>", str1)
#   # return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
#
# print(capital_words_spaces("Python"))
# print(capital_words_spaces("PythonExercises"))
# print(capital_words_spaces("PythonExercisesPracticeSolution"))
