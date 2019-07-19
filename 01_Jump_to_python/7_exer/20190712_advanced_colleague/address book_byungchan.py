# coding: utf8
print("환영합니다. 주소록 프로그램입니다.")

def search_mode():
    file = open("주소록.txt", 'r')
    lists = file.readlines()
    while True:
        print("\n검색모드 입니다")
        choose_search_mode = int(input("1. 이름 검색모드 2. 주소검색모드 (종료= 0): "))
        finded = 0
        if choose_search_mode == 1:
            input_name = input("\n검색하시려는 이름을 입력하세요: ")
            for i in lists:
                name , adress = i.split(',')
                if name == input_name:
                    print('\n'+name+' '+ adress, end='')
                    finded = 1
                    break
            if finded == 0:  print("해당하는 이름이 없습니다")
        elif choose_search_mode == 2:
            input_adress = input("\n검색하시려는 주소을 입력하세요 ex) 대구광역시: ")
            for i in lists:
                name , adress = i.split(',')
                adress, gu = adress.split(' ')
                if adress == input_adress:
                    print('\n'+name+' '+ adress+' '+gu)
                    finded = 1
            if finded == 0:  print("\n해당하는 주소가 없습니다")
        elif choose_search_mode == 0:
            print("검색모드를 종료합니다\n")
            file.close()
            return

def input_mode():
    print("\n추가 입력모드 입니다\n")
    while True:
        input_name = input("이름을 입력하세요: ")
        file = open("주소록.txt", 'r')
        lists = file.readlines()
        file.close()
        for index , list in enumerate(lists):
            name, adress = list.split(',')
            if name == input_name:
                print('\n' + name + ' ' + adress, end='')
                select_num = int(input("\n1.주소수정 2.종료: "))
                if select_num == 2:
                    print("입력모드를 종료합니다")
                    return
                elif select_num == 1:
                    adress = input("\n수정할 주소를 입력하세요: ")
                    print("\n수정할 주소는 " '\"'+adress+'\"' " 입니다")
                    add = input_name+','+adress+'\n'
                    del lists[index]
                    lists.insert(index,add)
                    file = open('주소록.txt', 'w')
                    for list in lists:
                        file.write(list)
                    file.close()
                    print("파일 수정이 완료되었습니다 초기화면으로 돌아갑니다")
                    return
                else:
                    print('\n잘못된 숫자를 입력하셨습니다 추가입력모드를 종료합니다')
                    return
        adress = input('\n입력된 이름이 없습니다 주소를 입력해주세요 ex)대구광역시 동구: ')
        print("\n입력된 이름과 주소는  " + '\"' + input_name+' '+adress+'\"'+" 입니다")
        select_num = int(input('\n1. 주소록 입력 확인 2. 취소: '))
        if select_num ==2:
            print("\n추가 입력모드를 종료하고 메인화면으로 돌아갑니다")
            break
        elif select_num == 1:
            file = open('주소록.txt', 'a')
            list = input_name+','+adress+'\n'
            file.write(list)
            file.close()
            print("추가 주소 입력이 완료되었습니다. 메인화면으로 돌아갑니다")
            return
        else:
            print('잘못된 숫자를 입력하셨습니다. 추가입력모드를 종료합니다')
            return

def delete_mode():
    file = open("주소록.txt", 'r')
    lists = file.readlines()
    file.close()
    print("\n삭제모드 입니다")
    input_name = input("삭제할 이름을 입력하세요: ")
    for index , list in enumerate(lists):
        name, adress = list.split(',')
        if name == input_name:
            print("해당하는 이름을 찾았습니다")
            print('\n' + name + ' ' + adress, end='')
            select_num = int(input("\n삭제하시겠습니까? 1. 삭제 2. 취소: "))
            if select_num == 1:
                del lists[index]
                file = open("주소록.txt", 'w')
                for list in lists:
                    file.write(list)
                file.close()
                print("삭제가 완료되었습니다. 메인화면으로 돌아갑니다")
                return
            elif select_num == 2:
                print("삭제를 취소하였습니다. 메인화면으로 돌아갑니다")
                return
    print("해당하는 이름이 없습니다. 메인화면으로 돌아갑니다")

while True:
    print("\n====모드를 선택하세요====")
    choose_start_mode = int(input("1. 검색 모드 2. 추가 입력모드 3. 삭제 (종료 = 0): "))
    if choose_start_mode == 1:
        search_mode()
    elif choose_start_mode == 2:
        input_mode()
    elif choose_start_mode == 3:
        delete_mode()
    elif choose_start_mode == 0:
        print("\n주소록 프로그램을 종료합니다. 이용해 주셔서 감사합니다. 좋은 하루되세요")
        break
    else:
        print("0~3사이의 숫자를 입력하세요")
