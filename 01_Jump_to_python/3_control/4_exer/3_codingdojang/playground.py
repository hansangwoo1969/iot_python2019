# coding: cp949

my_class = ""
charge = {"����": 0, "���": 2000, "û�ҳ�": 3000, "����": 5000, "����": 0}
payment = 0
payment_way = 0
turn = 0
free_ticket = 5
annual_member_coupon = 3

while True:
    age = int(input("���̸� �Է��ϼ���: "))

    if age in range(4):
        my_class = "����"
    elif age in range(4, 14):
        my_class = "���"
    elif age in range(14, 19):
        my_class = "û�ҳ�"
    elif age in range(18, 66):
        my_class = "����"
    else:
        my_class = "����"
    print("������ ����� %s�̸� ����� %d�� �Դϴ�." % (my_class, charge[my_class]))

    if charge[my_class] == 0:
        print("")
        continue

    payment_way = int(input("��� ������ �����ϼ���. (1: ����, 2: ���� ���� �ſ� ī��): "))

    if payment_way == 1:
        payment = int(input("����� �Է��ϼ���: "))

        if payment < charge[my_class]:
            print("%d���� ���ڶ��ϴ�. �Է��Ͻ� %d���� ��ȯ�մϴ�.�n" % ((charge[my_class] - payment), payment))
            continue
        elif payment == charge[my_class]:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        else:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d���� ��ȯ�մϴ�." % (payment - charge[my_class]))
    elif payment_way == 2:
        print("(���� �ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����)")
        if age < 60:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." % (charge[my_class] * 0.9))
        else:
            print("%d�� �����Ǿ����ϴ�. Ƽ���� �����մϴ�." % ((charge[my_class] * 0.9) * 0.95))
    else:
        print("��� ������ ���õ��� �ʾ� ó������ ���ư��ϴ�.�n")
        continue

    turn += 1

    if turn % 7 == 0 and free_ticket >= 0:
        free_ticket -= 1
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. (�ܿ� ����Ƽ�� %d��)" % free_ticket)
    elif turn % 4 == 0 and annual_member_coupon >= 0:
        annual_member_coupon -= 1
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. (�ܿ� ����Ƽ�� %d��)" % annual_member_coupon)

    print("")