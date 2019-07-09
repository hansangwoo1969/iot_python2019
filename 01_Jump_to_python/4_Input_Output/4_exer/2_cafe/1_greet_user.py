# 인사하기
import sys

user_names = sys.argv[1:]

def greet_users(usernames):
     for i in range(len(user_names)):
        print("Hello, %s" % user_names[i].capitalize())

greet_users(user_names)