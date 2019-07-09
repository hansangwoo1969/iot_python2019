def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다."%name)
    print("나의 나이는 %d입니다."%old)
    if man:
        print("남자 입니다")
    else:
        print("여자입니다")

say_myself("한상우", 30)
say_myself("한상우", 30, True)