#coding: cp949

coffee = 3
money = 0
coffee_price = 300

while True:
    money = int(input("���� �־� �ּ���: "))
    if money == coffee_price:
        print("Ŀ�Ǹ� �ݴϴ�")
        coffee = coffee - 1
    elif money > coffee_price:
        print("Ŀ�Ǹ� �ݴϴ�")
        print("�Ž����� %d�� �ݴϴ�."% (money - 300))
        coffee = coffee - 1
    else:
        print("���� �ٽ� �����ְ� Ŀ�Ǹ� ���� �ʽ��ϴ�.")
        
    print("���� Ŀ���� ���� %d�� �Դϴ�." % coffee)

    if coffee == 0:
        print("Ŀ�ǰ� �� ���� �����ϴ�. �ǸŸ� �����մϴ�")
        break

    

