f = open("새파일.txt", 'r', encoding='UTF-8')

data = f.read()    # 파일 전체의 내용을 파악할때 적합
print(data)

f.close()