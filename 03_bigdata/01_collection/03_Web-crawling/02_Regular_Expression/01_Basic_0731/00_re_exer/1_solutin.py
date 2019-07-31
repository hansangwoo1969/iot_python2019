import re

"""
문자열에 특정문자집합만 들어  있는지 확인하는 방법들
"""
# def is_re_expr_char(string):
#     p = re.compile(r'[^a-zA-Z0-9.]')
#     m = p.search(string)
#     return not bool(m)
#
# print(is_regular_expression_char("ABCDEFabcdef123450"))
# print(is_regular_expression_char("*&%@#!}{"))

string = "ABCDEF012345abcdef"
if re.findall('\W',string):   # \W 는 [a-zA-ZO-9]가 아닌 것
    print("Not Matched")
else:
    print("Matched")