# 사칙연산 계산기 완성하기
# print("=== 1안 내가 버벅거린 코드 =======")
# class Calculator:
#     def __init__(self, a_list):
#         self.total = 0
#         self.a_list = a_list
#         # self.avg = total / len(a_list)
#
#     def sum(self):
#         for i in range(len(self.a_list)):
#            self.total += self. a_list[i]
#         print(self.total)
#
#     def avg(self):
#         average = self.total / len(self.a_list)
#         print(average)
#
# cal1 = Calculator([1,2,3,4,5])
# cal1.sum()   # 15
# cal1.avg()   # 3.0
#
# cal2 = Calculator([6, 7, 8, 9, 10])
# cal2.sum()   # 40
# cal2.avg()   # 8.0

print("=== 2안 교재 풀이 ===")
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def add(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.add()
        return total/len(self.numberList)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.add())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.add())
print(cal2.avg())
