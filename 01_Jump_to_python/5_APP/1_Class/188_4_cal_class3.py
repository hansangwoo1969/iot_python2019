class FourCal:

    def __init__(self, first,  second):
        # self.first=first
        # self.second=second
        self.first=first
        if second == 0:
            print("두번째 값에는 0이 올 수 없습니다.")
            print("프로그램 강제 종료 하겠습니다.")
            exit()
        self.second=second

    def print_number(self):
        print("first: %d, second: %d"%(self.first, self.second))
        # self를 사용하지 않으면 멤버함수에서 사용하는 지역변수로 인식한다.
        # 따라서 아래 코드는 빌드시 에러를 발생하게 된다.
        # print("first: %d, second: %d"%(first, second))

a = FourCal(1, 2)
a.print_number()
b = FourCal(3, 0)
b.print_number()