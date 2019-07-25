import json

g_json_big_data = []


def conditional_search_():
    search_menu = """
    아래 메뉴를 선택하세요.
    1. 전체 학생 정보 조회
    조건 검색
    2. ID검색
    3. 이름 검색
    4. 나이 검색
    5. 주소 검색
    6. 과거 수강 횟수 검색
    7. 현재 강의를 수강중인 학생
    8. 현재 수강중인 강의명
    9. 현재 강사
    10. 이전 메뉴
    메뉴를 선택하세요:  """

    option = input(search_menu)

    if option == '1':
        all_student_search()
    if option == '2':
        id_search()
    if option == '3':
        name_search()
    if option == '4':
        age_search()
    if option == '5':
        address_search()
    if option == '6':
        pass
    if option == '7':
        pass
    if option == '8':
        pass
    if option == '9':
        pass
    if option == '10':
        pass
# def json_read():
#     with open('ITT_Student.json', encoding='UTF8') as json_file:
#         json_object = json.load(json_file)
#         json_string = json.dumps(json_object)
#         g_json_big_data = json.loads(json_string)
#     return g_json_big_data
#
#
# def only_print():
#     print(f" * 학생ID: {student['student_ID']}   =============")
#     print(f" * 이름: {student['student_name']}")
#     print(f" * 나이: {student['student_age']}")
#     print(f" * 주소: {student['address']}")
#     print("  * 수강정보")
#     print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
#     print("   + 현재 수강 과목 ")
#     print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
#     print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
#     print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
#     print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
#     print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")

def all_student_search():
    # g_json_big_data = json_read()
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    for student in g_json_big_data:
        # only_print()
        print(f" * 학생ID: {student['student_ID']}   =============")
        print(f" * 이름: {student['student_name']}")
        print(f" * 나이: {student['student_age']}")
        print(f" * 주소: {student['address']}")
        print("  * 수강정보")
        print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
        print("   + 현재 수강 과목 ")
        print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
        print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
        print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
        print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
        print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")

def id_search():
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    input_id = input('검색할 아이디를 입력하세요  ')

    for student in g_json_big_data:
        if student['student_ID'] == input_id:
            print(f" * 학생ID: {student['student_ID']}   =============")
            print(f" * 이름: {student['student_name']}")
            print(f" * 나이: {student['student_age']}")
            print(f" * 주소: {student['address']}")
            print("  * 수강정보")
            print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
            print("   + 현재 수강 과목 ")
            print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
            print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
            print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
            print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
            print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")

def name_search():
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    input_name = input('검색할 이름를 입력하세요  ')

    name_count = 0
    for student in g_json_big_data:
        if student['student_name'] == input_name:
            name_count += 1
    # print(name_count)
    if name_count > 1:
        print("복수개의 결과가 검색되었습니다.")
        print("----- 요약 결과 -----")
        for student in g_json_big_data:
            if student['student_name'] == input_name:
                print(f">> 학생 ID: {student['student_ID']},  학생 이름: {student['student_name']}")
    elif name_count == 1:
        for student in g_json_big_data:
            print(f" * 학생ID: {student['student_ID']}   =============")
            print(f" * 이름: {student['student_name']}")
            print(f" * 나이: {student['student_age']}")
            print(f" * 주소: {student['address']}")
            print("  * 수강정보")
            print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
            print("   + 현재 수강 과목 ")
            print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
            print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
            print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
            print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
            print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")

def age_search():    # 나이가 정수 또는 문자 입력됨
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    input_age = int(input('검색할분의 나이를 입력하세요  '))
    # for student in g_json_big_data:
    #     print(student['student_age'])    # 31, 29, 29
    same_age_count = 0
    for student in g_json_big_data:
        if student['student_age'] == input_age or student['student_age'] == str(input_age):
            same_age_count += 1
    print(same_age_count)

    if same_age_count > 1:
        for student in g_json_big_data:
            if student['student_age'] == input_age or student['student_age'] == str(input_age):
                print(f" 학생ID: {student['student_ID']}, 학생 이름: {student['student_name']}, 나이:{student['student_age']}")
    elif same_age_count == 1:
        for student in g_json_big_data:
            if student['student_age'] == input_age:
                print(f" * 학생ID: {student['student_ID']}   =============")
                print(f" * 이름: {student['student_name']}")
                print(f" * 나이: {student['student_age']}")
                print(f" * 주소: {student['address']}")
                print("  * 수강정보")
                print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
                print("   + 현재 수강 과목 ")
                print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
                print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
                print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
                print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
                print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")

def address_search():
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

    input_address = input('검색할분의 주소를 입력하세요  ')

    same_address_count = 0
    for student in g_json_big_data:
        if input_address in student['address']:
            same_address_count += 1

    print(same_address_count)
    if same_address_count > 1:
        for student in g_json_big_data:
            if input_address in student['address']:
                print(f" 학생ID: {student['student_ID']}, 학생 이름: {student['student_name']}, 나이:{student['student_age']}")
    elif same_address_count == 1:
        for student in g_json_big_data:
            if input_address in student['address']:
                print(f" * 학생ID: {student['student_ID']}   =============")
                print(f" * 이름: {student['student_name']}")
                print(f" * 나이: {student['student_age']}")
                print(f" * 주소: {student['address']}")
                print("  * 수강정보")
                print(f"   + 과거 수강 횟수: {student['total_course_info']['num_of_course_learned']}")
                print("   + 현재 수강 과목 ")
                print(f"    강의 코드: {student['total_course_info']['learning_course_info'][0]['course_code']}")
                print(f"    강의명: {student['total_course_info']['learning_course_info'][0]['course_name']}")
                print(f"    강사: {student['total_course_info']['learning_course_info'][0]['teacher']}")
                print(f"    개강일: {student['total_course_info']['learning_course_info'][0]['open_date']}")
                print(f"    종료일: {student['total_course_info']['learning_course_info'][0]['close_date']}")



def modifying_book():       # 1 학생이름 변경과 이전메뉴만 실습
    input_id = input("수정할 학생의 아이디를 입력하세요: ")
    info = """
    메뉴번호를 입력 하세요.
    1. 학생 이름
    2. 나이
    3. 주소
    4. 과거 수강회수
    5. 현재 수강중인 강의 정보
    0. 이전메뉴
    메뉴번호를 입력하세요:  """
    option = input(info)
    if option == 1:
        name_modify(input_id)
    if option == '0':
        start()

def name_modify(id):
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)

        for stdudent in g_json_big_data:
            if stdudent['student_ID'] == id:
                stdudent['student_name'] = '미애'




def start():
    menual = """
     << JSON기반 학생 정보 관리 프로그램>>
     1. 학생 정보 입력
     2. 학생 정보 조회
     3. 학생 정보 수정
     4. 학생 정보 삭제
     5. 프로그램 종료
     메뉴를 선택 하세요:  """

    option = input(menual)

    if option == '1':
        pass
    elif option == '2':
        conditional_search_()
    elif option == '3':
        modifying_book()
    elif option == '4':
        pass
    elif option == '5':
        exit()



start()
