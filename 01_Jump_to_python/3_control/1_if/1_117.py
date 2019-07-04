# coding: cp949
# print("기본 if문법") # if, for, while 없이 단독으로 indentation이 불가능
money = True

#if money:
#print("택시를 타고 가라") # if 이하에는 반드시 1개 이상의 statement가 있어야 한다.

#if money:
# print("택시를 타고 가라") # indentation은 공백, 탭 모두 허용한다.

#if money:
#    print("현금이 있는것으로 확인 되었음") #동일한 indentation으로 구성된 statement는
#    print("택시타고,,")                    # 같은 statement block을 형성한다.

#if money:
#   print("현금이 있는것으로 확인 되었음") #동일한 indentation으로 맞춰야한다
#    print("택시타고,,")                    
#else:
#    print("걸어 가라")

if money:
    print("현금이 있는것으로 확인 되었음") 
    print("택시타고,,")                    
else:
    print("현금이 없네요")
    print("걸어가세요")
print("프로그램을 종료합니다") # if, else statement block과 상관없는 최상위 레벨의 statement
