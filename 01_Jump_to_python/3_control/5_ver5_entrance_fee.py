# coding: cp949
# ������ݰ�� ���α׷� ver5

#    0 ~   3�� (����) :   ����
#    4 ~  13�� (���) : 2000��
#    14 ~ 18�� (û�ҳ�) : 3000��
#    19 ~ 65�� (����) : 5000��
#    66�� ~    (����): ����
#    [ȭ�� ���]
#    ���̸� �Է��ϼ���.
#    ���ϴ� []����̸� ����� []�� �Դϴ�.
#    ��������� �����ϼ���(1:����, 2: �������� �ſ�ī��
#    1. ������ ���
#    ����� �Է��ϼ���
#        �ݾ׹̸��� ���: " []�� ���ڶ��ϴ�. �Է��Ͻ� []�� ��ȯ�մϴ�."
#        �ݾ���ġ�ϴ� ���: " �����մϴ�. Ƽ���� ���� �մϴ�."
#        �ݾ��� �ʰ��ϴ� ���: "�����մϴ�. Ƽ���� �����ϰ� �Ž����� []�� ��ȯ�մϴ�."
#    2. �������� �ſ�ī��(�����ݾ��� 10%����, 60~65�� ����� �߰� 5%����)
#      []�� ���� �Ǿ����ϴ�. Ƽ���� ���� �մϴ�.
#
#    7��° �մԸ��� Ƽ�ϱ��Ž� ����Ƽ�� ����(�ʱ⹫��Ƽ��:5��)
#    "�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ�����Ƽ�� []��"
#    4��° �մ� ���� Ƽ�� ���Ž� ���� ȸ���� ȫ���̺�Ʈ�� �����Ѵ�. (�ʱ����� Ƽ��: 3��)
#    "�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�.�ܿ�����Ƽ��[]��"
#    - �̺�Ʈ�� ���� ī��Ʈ�� Ƽ���� ������ ���� ���Ͽ� �����Ѵ�.



count = 0
free_ticket = 5
discount_ticket = 3
while True:
    age = int(input("���̸� �Է��ϼ���: "))

# age classification
    infant = (age >= 0) and (age <= 3)
    child = (age >= 4) and (age <= 13)
    youth = (age >= 14) and (age <= 18)
    adult = (age >= 19) and (age <= 65)
    aged_man = (age >= 66)

# price by age
    infant_price = 0
    child_price = 2000
    youth_price = 3000
    adult_price = 5000
    aged_man_price = 0


    if infant:
        print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�."% ("����", infant_price))
        continue
    elif child:
        print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("���", child_price))
    elif youth:
        print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("û�ҳ�", youth_price))
    elif adult:
        print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("����", adult_price))
    elif aged_man:
        print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("����", aged_man_price))
        continue
    else:
        print("�ٽ� �Է� �ϼ���")


    payment_type = int(input("���ҹ���� �����ϼ��� (1:����, 2:���� ���� �ſ�ī��): "))

    if payment_type == 1:
        my_cash = int(input("���ұݾ��� �Է��ϼ���: "))

        if child and (my_cash < child_price):
            print(" [%d��]�� ���ڶ��ϴ�. �Է��Ͻ� [%d��]�� ��ȯ �մϴ�."%(child_price - my_cash, my_cash))
        if youth and (my_cash < youth_price):
            print(" [%d��]�� ���ڶ��ϴ�. �Է��Ͻ� [%d��]�� ��ȯ �մϴ�."%(youth_price - my_cash, my_cash))
        if adult and (my_cash < adult_price):
            print(" [%d��]�� ���ڶ��ϴ�. �Է��Ͻ� [%d��]�� ��ȯ �մϴ�."%(adult_price - my_cash, my_cash))

        if child:
            if my_cash == child_price:
                print("�����մϴ�. Ƽ���� ���� �մϴ�.")
                count += 1
            elif my_cash > child_price:
                print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - child_price))
                count += 1
        if youth:
            if my_cash == youth_price:
                print("�����մϴ�. Ƽ���� ���� �մϴ�.")
                count += 1
            elif my_cash > youth_price:
                print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - youth_price))
                count += 1
        if adult_price:
            if my_cash == adult_price:
                print("�����մϴ�. Ƽ���� ���� �մϴ�.")
                count += 1
            elif my_cash > adult_price:
                print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - adult_price))
                count += 1


    if payment_type == 2:
        if child:
            print("[%.0d��] ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%(child_price*.9))
        if youth:
            print("[%.0d��] ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%(youth_price*.9))
        if adult:
            if age>=60 and age<=65:
                print("[%.0d��] ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%(adult_price*.9*.95))
            else:
                print("[%.0d��] ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." % (adult_price * .9))
        count += 1

    if (count % 7 == 0):
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷ �Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ����� Ƽ��[%d��]"%(free_ticket-1))
        free_ticket -= 1
    if (count % 4 == 0):
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷ �Ǽ̽��ϴ�. ���� ���� Ƽ���� �����մϴ�. �ܿ� ���� Ƽ��[%d��]" % (discount_ticket - 1))
        discount_ticket -= 1
    print("ȸ����: %d"%count)
    if count == 10:
        break
