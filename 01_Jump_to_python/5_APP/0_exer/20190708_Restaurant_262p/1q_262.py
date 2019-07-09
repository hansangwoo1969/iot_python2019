# class Calculator를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus메서드를 추가

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

cal = UpgradeCalculator()

cal.add(10)
cal.minus(7)

print(f"\n상속후 minus메서드 추가한 결과: {cal.value}")