from xml.etree.ElementTree import Element, parse, dump, ElementTree
import xml.etree.ElementTree as ET




def member_check():

    BASE = """
    <검색 조건>
    1. ID
    2. 이름
    3. 나이
    4. 전공
    5. 컴퓨터 언어명
    6. 컴퓨터 언어 학습기간
    7. 컴
    """











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



# def new_entry():
tree = parse("1_students_info2.xml")
students_list = tree.getroot()
# student = Element('student')
# student.attrib['id'] = "ITT"+"NUM"
NUM = 9
id_num = "%03d" % NUM
# print(id_num)

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

