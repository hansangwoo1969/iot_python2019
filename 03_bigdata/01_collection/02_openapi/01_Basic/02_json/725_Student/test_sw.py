import  json


g_json_big_data=[]
# def conditional_search_():
#     search_menu = """
#     아래 메뉴를 선택하세요.
#     1. 전체 학생 정보 조회
#     조건 검색
#     2. ID검색
#     3. 이름 검색
#     4. 나이 검색
#     5. 주소 검색
#     6. 과거 수강 횟수 검색
#     7. 현재 강의를 수강중인 학생
#     8. 현재 수강중인 강의명
#     9. 현재 강사
#     10. 이전 메뉴
#     메뉴를 선택하세요:  """
#
#     option = input(search_menu)
#
#     if option == '1':
#         all_student_search()
#     if option == '2':
#         pass
#     if option == '3':
#         pass
#     if option == '4':
#         pass
#     if option == '5'
#         pass
#     if option == '6'
#         pass
#     if option == '7'
#         pass
#     if option == '8'
#         pass
#     if option == '9'
#         pass
#     if option == '10'
#         pass

# def all_student_search():




with open('ITT_Student.json', encoding='UTF8') as json_file:
 json_object = json.load(json_file)
 json_string = json.dumps(json_object)
 g_json_big_data = json.loads(json_string)

# print(g_json_big_data[0]['total_course_info']['num_of_course_learned'])
# print(g_json_big_data[])
# n = len(g_json_big_data)
# add_ID = "ITT"+str("%03d" % (n + 1))

new_ID_Num = int(g_json_big_data[len(g_json_big_data)-1]['student_ID'][3:])
# print(new_ID_Num)
add_ID = "ITT"+"0"*(3-len(str(new_ID_Num)))+ str(new_ID_Num+1)
#
# print(add_ID)
add_name = input("이름: ")
add_age =  input("나이:  ")
add_address = input("주소: ")
add_past_learning = input("과거 수강 횟수: ")
add_cur_subject = input("현재 수강과목이 있습니까 (y/n):  ")
add_lec_code = input("강의 코드(예, IB117112): ")
add_lec_name = input("강의명: ")
add_teacher = input("강사: ")
add_open_date = input("개강일(예,2017-11-11): ")
add_close_date = input("종료일(예, 2018-07-12): ")

g_json_big_data['student_ID'] = add_ID
g_json_big_data['student_name'] = add_name
g_json_big_data['student_age'] = add_age
g_json_big_data['student_address'] = add_address
g_json_big_data['total_course_info']['num_of_course_learned'] = add_past_learning
# add_cur_subject = input("현재 수강과목이 있습니까 (y/n):  ")
while True:
    add_cur_subject = input("현재 수강과목이 있습니까 (y/n):  ")
    if add_cur_subject == n:
        break
    g_json_big_data['total_course_info']['learning_course_info']['course_code'] = add_lec_code
    g_json_big_data['total_course_info']['learning_course_info']['course_name'] = add_lec_name
    g_json_big_data['total_course_info']['learning_course_info']['teacher'] = add_teacher
    g_json_big_data['total_course_info']['learning_course_info']['open_date'] = add_open_date
    g_json_big_data['total_course_info']['learning_course_info']['close_date'] = add_close_date






# print(new_ID)