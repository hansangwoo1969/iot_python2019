# 'test.txt'내의 'java'라는 문자열을 'pyhon'으로 바꾸어 저장
text = '''
    Life is too short
    you need java
'''

f = open('test1.txt', 'w')
f.write(text)
f.close()

f = open("test1.txt", 'r')
body = f.read().replace("java", "python")
f.close()

f = open('test1.txt', 'w')
f.write(body)
f.close()