from xml.etree.ElementTree import Element, parse, dump, ElementTree
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    i = "\n"+level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+" "
        if not elem.tail or not elem.tail.strip():
            elem.tail=i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not  elem.tail.strip()):
            elem.tail = i


def new_entry():

    tree = parse("1_students_info2.xml")
    students_list = tree.getroot()
    NUM = 9
    id_num = "%03d" % NUM

    while True:

        new_name = input("이름을 입력하세요(종료는 'Enter'입력): ")
        if not new_name:
            break
        new_sex = input("성별을 입력하세요 ")
        new_age = input("나이을 입력하세요 ")
        new_major = input("전공을 입력하세요 ")
        print("사용 가능한 컴퓨터 언어를 입력하세요  ")
        new_language = input("> 언어 이름(종료는 'Enter'입력: ")
        if not new_language:
            break
        study_period = input("> 학습 기간(년/개월 단위): ")
        new_level = input("> 수준(상/중/하): ")

        student = Element('student')
        student.attrib['ID'] = "ITT" + id_num
        student.attrib['name'] = new_name
        student.attrib['sex'] = new_sex

        new_tag_m = ET.SubElement(student, 'major')
        new_tag_m.text = new_major

        # major = Element('major')
        # student.major.text = new_major
        # age = Element('age')
        new_tag_a = ET.SubElement(student, 'age')
        new_tag_a.text = new_age
        # age.text = new_age
        if new_language:
            new_tag_lan = ET.SubElement(student, 'language')
            new_tag_lan.attrib['name'] = new_language
            # language = Element('practicable_computer_languages')
            # language.attrib['name'] = new_language

            new_tag_lev = ET.SubElement(student, 'level')
            new_tag_lev.attrib['level'] = new_level

            # language.attrib['level'] = new_level
        if study_period:
            new_tag_pe = ET.SubElement(student, 'period')
            new_tag_pe.attrib['value'] = study_period
            # period = Element('period')
            # period.text = study_period
        NUM += 1

    students_list.append(student)
    indent(students_list)
    ElementTree(students_list).write('student_info_3.xml')
    dump(students_list)


# def new_entry():
#     tree = parse("1_students_info2.xml")
#     students_list = tree.getroot()
#     # student = Element('student')
#     # student.attrib['id'] = "ITT"+"NUM"
#     NUM = '009'
#
#     while True:
#         new_name = input("이름을 입력하세요(종료는 'Enter'입력): " )
#         new_sex = input("성별을 입력하세요 ")
#         new_age = input("나이을 입력하세요 ")
#         new_major = input("전공을 입력하세요 ")
#         print("사용 가능한 컴퓨터 언어를 입력하세요  " )
#         new_language = input("> 언어 이름(종료는 'Enter'입력: ")
#         study_period = input("> 학습 기간(년/개월 단위): ")
#         new_level = input("> 수준(상/중/하): ")
#
#
#         student = Element('student')
#         student.attrib['ID'] = "ITT"+"NUM"
#         student.attrib['name'] = new_name
#         student.attrib['sex'] = new_sex
#         student.attrib['name'] = new_name
#         major = Element('major')
#         major.text = new_major
#         age = Element('age')
#         age.text = new_age
#         if new_language:
#             language = Element('practicable_computer_languages')
#             language.attrib['name'] = new_language
#             language.attrib['level'] = new_level
#             period = Element('period')
#             period.text = study_period










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
2. 입력
3. 조회
4. 수정
5. 삭제
6. 종료
메뉴입력: """

print("학생정보 XML데이터 분석 시작...")

while True:
    menu =input(base)
    if menu == '1':
        summarize()
    elif menu == '2':
        new_entry()
    elif menu =='3':
        member_check()

    elif menu == '2':
        total_data_print()
    elif menu == '3':
        exit()
    else:
        print("1,2,3중에서 골라주삼..")





