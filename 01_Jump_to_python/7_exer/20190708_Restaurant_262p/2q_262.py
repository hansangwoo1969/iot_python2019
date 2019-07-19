# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator클래스 만들기

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value



class MaxLimitCalculator(Calculator):

    def add(self, num):
        self.value += num
        if self.value >= 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
cal.add(50)  # 50더하기
cal.add(60)  # 60더하기

print(f"\n한정된 두 수의 최대값: {cal.value}")  # 100출력