# coding: cp949

# ������ݰ�� ���α׷� ver3

#    0 ~   3�� (����) :   ����
#    4 ~  13�� (���) : 2000��
#    14 ~ 18�� (û�ҳ�) : 3000��
#    19 ~ 65�� (����) : 5000��
#    66�� ~    (����): ����
#    [ȭ�� ���]
#    ���̸� �Է��ϼ���.
#    ���ϴ� []����̸� ����� []�� �Դϴ�.
#    ����� �Է��ϼ���
#        �ݾ׹̸��� ���: " []�� ���ڶ��ϴ�. �Է��Ͻ� []�� ��ȯ�մϴ�."
#        �ݾ���ġ�ϴ� ���: " �����մϴ�. Ƽ���� ���� �մϴ�."
#        �ݾ��� �ʰ��ϴ� ���: "�����մϴ�. Ƽ���� �����ϰ� �Ž����� []�� ��ȯ�մϴ�."
#




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
elif child:
    print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("���", child_price))
elif youth:
    print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("û�ҳ�", youth_price))
elif adult:
    print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("����", adult_price))
elif aged_man:
    print("���ϴ� [%s]����̸�, ����� [%d��] �Դϴ�." % ("����", aged_man_price))
else:
    print("�ٽ� �Է� �ϼ���")


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
    elif my_cash > child_price:
        print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - child_price))
if youth:
    if my_cash == youth_price:
        print("�����մϴ�. Ƽ���� ���� �մϴ�.")
    elif my_cash > youth_price:
        print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - youth_price))
if adult_price:
    if my_cash == adult_price:
        print("�����մϴ�. Ƽ���� ���� �մϴ�.")
    elif my_cash > adult_price:
        print("�����մϴ�. Ƽ���� �����ϰ�, �Ž����� [%d��]�� ��ȯ�մϴ�."%(my_cash - adult_price))

