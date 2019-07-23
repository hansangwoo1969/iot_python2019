from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET


def summarize():
    tree = parse("0_students_info.xml")
    students_list = tree.getroot()

    total_student = 0
    male = 0
    major = 0
    language_user = 0
    high_level = 0
    py_user = 0
    under_30 = 0
    under_40 = 0
    over_40 = 0
    Name_20 = {}
    Name_30 = {}
    Name_40 = {}
    # Age = []
    for student in students_list:
        if student.find('./age').text:
            if 20 <= int(student.find("./age").text) < 30:
                under_30 += 1
                Name_20.update({student.get("name"): student.find('./age').text})
                #Name.append(student.get('age'))
                # dict[student.get('name')] = student.get('age')
            elif 30 <= int(student.find("./age").text) < 40:
                under_40 += 1
                Name_30.update({student.get("name"): student.find('./age').text})
                # dict[student.get('name')] = student.get('age')
            elif 40 <= int(student.find("./age").text):
                over_40 += 1
                Name_40.update({student.get("name"): student.find('./age').text})
                # dict[student.get('name')] = student.get('age')

        if student.get("name"):
            total_student += 1
        if student.get("sex")=='남':
            male += 1
        if student.findtext("major")=="컴퓨터 공학" or student.findtext("major")=="통계":
            major += 1
        if student.find('./practicable_computer_languages'):
            language_user += 1
            for language in student.find('practicable_computer_languages'):
                if language.items()[1][1]=="상":
                    high_level += 1
                if language.items()[0][1]=="파이썬":
                    py_user += 1

    print("<요약 정보>")
    print("* 전체 학생수: %s" % total_student)
    print("* 성별")
    print(" - 남학생: %s 명 (%s%%)" % (male, male/total_student*100))
    print(" - 여학생: %s 명 (%s%%)" % ((total_student-male), ((total_student-male)/total_student)*100))
    print("* 전공여부")
    print(" - 전공자(컴퓨터 공학, 통계): %s명 (%s%%)" % (major, (major/total_student)*100))
    print(" - 프로그래밍 언어 경험자: %s명 (%s%%)" % (language_user, (language_user/total_student)*100))
    print(" - 프로그래밍 언어 상급자: %s명 (%s%%)" % (high_level, (high_level/total_student)*100))
    print(" - 파이썬 경험자: %s명 (%s%%)" % (py_user, (py_user/total_student)*100))
    print("* 연령대")
    print(" - 20대: %s명 (%s%%) [%s]" % (under_30, under_30/total_student*100, Name_20))
    # print(" - 20대: %s명 (%s%%) " % (under_30, under_30/total_student*100, Name_20)))
    print(" - 30대: %s명 (%s%%) [%s]" % (under_40, under_40/total_student*100, Name_30))
    print(" - 40대: %s명 (%s%%) [%s]" % (over_40, over_40/total_student*100, Name_40))

        #
    # print("\n\n%s\n\t성별: %s\n\t나이: %s\n\t전공: %s\n\t사용 가능한 언어"
    #         % (student.items()[0][1], student.items()[1][1],
    #             student.find('age').text, student.find('major').text), end="")


def total_data_print():  # 여기서부터 파싱입니다.
    tree = parse("0_students_info.xml")
    students_list = tree.getroot()

    for student in students_list:
        print("\n\n%s\n\t성별: %s\n\t나이: %s\n\t전공: %s\n\t사용 가능한 언어"
              % (student.items()[0][1], student.items()[1][1],
                 student.find('age').text, student.find('major').text), end="")
        try:
            if student.find('practicable_computer_languages').text:
                for languages in student.find('practicable_computer_languages'):
                    print("\n\t\t->%s\t(학습기간: %s, Level: %s)"
                          % (languages.items()[0][1], languages.find('period').items()[0][1]
                             , languages.items()[1][1]), end="")
            else:
                print(": 없음", end="")
        except AttributeError:
            print(": 없음", end="")


base = """
1. 요약 정보
2. 전체 데이터 조회
3. 종료
메뉴입력: """

print("학생정보 XML데이터 분석 시작...")

while True:
    menu =input(base)
    if menu == '1':
        summarize()
    elif menu == '2':
        total_data_print()
    elif menu == '3':
        exit()
    else:
        print("1,2,3중에서 골라주삼..")





