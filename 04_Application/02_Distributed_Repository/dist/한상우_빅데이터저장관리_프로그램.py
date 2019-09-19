
import csv
import os

print('빅데이터 저장소 시뮬레이션 v1.0 한상우')

base_repository_name = 'Data_Repo'
dir_delimeter = '/'
file_name = 'Demo_'
file_format = 'csv'
initial_file_name=f'{base_repository_name}{dir_delimeter}{file_name}1.{file_format}'
simulation_count = 100
simulation_data = ['1111', '종로구', '서울특별시', '창덕궁','1', '14137', '43677']
file_size_limit = 10000
is_header = False
is_first = False

def  get_request_url():
    pass
def getTourPointVisitor():
    pass
def getTourPointData(filewriter):
    filewriter.writerow(simulation_data)
    return

def get_dest_file_name(file_index):
    global is_header
    dest_file_name = \
    f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index)}.{file_format}'

    try:
        file_size = os.path.getsize(dest_file_name)
        print(f"'{dest_file_name}' file size: {file_size}")
        print(f"파일당 size 제한: {file_size_limit}")

        if file_size > file_size_limit:
            dest_file_name =\
            f'{base_repository_name}{dir_delimeter}{file_name}{str(file_index+1)}.{file_format}'
            is_header=True
        else:
            is_header=False
    except:
        pass

    return dest_file_name

def save_file(index):
    dest_file_name = get_dest_file_name(index)

    csv_out_file = open(dest_file_name,'a', newline='')
    filewriter = csv.writer(csv_out_file)

    if is_header == True or is_first == True:
        header_list = ['addrCd', 'gungu', 'sido', 'resnNm', 'rnum','csForCnt','csNatCnt']
        filewriter.writerow(header_list)

    for index in range(simulation_count):
        getTourPointData(filewriter)
    csv_out_file.close()

def file_count():
    index = len(os.listdir(base_repository_name))
    return index

def main():
    file_size = 0
    if not os.path.exists(base_repository_name):
        os.mkdir(base_repository_name)
    if not os.path.exists(initial_file_name):
        is_first = True
        save_file(1)
    else:
        save_file(file_count())

def config_set_up():
    global base_repository_name, simulation_count,file_size_limit,file_format
    print('\n 현재 설정된 환경')
    print(f'1. base_repository_name: {base_repository_name}')
    print(f'2. simulation_count: {simulation_count}')
    print(f'3. file_size_limit: {file_size_limit}')
    print(f'4. file_format: {file_format}\n')

    menu_choice = input(set_up)
    if menu_choice == '1':
        base_repository_name = input("변경할 base_repository_name을  입력하세요: ")
        print(f"변경된 저장소는 : {base_repository_name}")
        # save_file(1)   main함수에 새로 시작하는 코드 있음
    elif menu_choice =='2':
        simulation_count = int(input("변경할 simulation_count을  입력하세요 "))
        print(f"변경된 simulation_count는 : {simulation_count}")
    elif menu_choice =='3':
        file_size_limit = int(input("변경할 file_size_limit을  입력하세요 "))
        print(f"변경된 파일사이즈 임계치는 : {file_size_limit}")
    elif menu_choice == '4':
        file_format = input("변경할 file_format을  입력하세요 ")
        print(f"변경된 파일 포맷은 : {file_format}")
    else:
        print("잘 못 입력 하였습니다.")
    return

set_up = '''

        <Configurartion set_up>
    1. base_repository_name
    2. simulation_count
    3. file_size_limit
    4. file_format
    변경할 환경변수를 선택하세요(숫자로):   '''

script  = '''

        <메인 메뉴>
    1. 환경 설정
    2. 작업 수행
    3. 종료
    메뉴를 선택 하세요(숫자로):    '''

while True:
    menu_choice = input(script)

    if menu_choice == '1':
        config_set_up()
        # print('1입니다.')
    elif menu_choice == '2':
        main()
    elif menu_choice == '3':
        break


