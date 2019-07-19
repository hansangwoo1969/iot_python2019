import time
import random
import threading
from datetime import datetime
global start_num
start_num = 0
def start_number():
    # 입력대기와 점수 출력 쓰래드 동작
    t = threading.Thread(target=show_the_scores, daemon=True)
    global start_num
    t.start()
    start_num = input('1 입력시 시작 합니다. (종료 = q): ')
    t.join()

def show_the_scores():
    # 등록된 순위가 차례대로 보여짐
    global start_num
    list_levels = ['쉬움 순위', '보통 순위', '어려움 순위']
    while True:
        for index1 in range(1, 4):
            time.sleep(2)
            if start_num:  return
            print('\n'+('-'*10) +list_levels[index1-1]+('-'*10))
            try:
                f_name = "score"+str(index1)+'.txt'
                file = open(f_name, 'r')
                score_lines = file.readlines()
                file.close()
                for index2, score in enumerate(score_lines):
                    score_name, score_try, score_time = score.rstrip().split()
                    print((str(index2 + 1)) + '\t등\t' + score_name +'\t'+ score_try+'번 시도\t'+ score_time)
            except:
                print(f"{list_levels[(index1-1)]} 파일이 없습니다. 순위 등록후 파일이 생성됩니다")

            if start_num:  return
            print('\n1 입력시 시작 합니다. (종료 = q): ')

def select_level():
    # 난이도 선택
    while True:
        level = int(input("\n숫자를 입력하여 난이도를 선택해 주세요 1. 쉬움 2. 보통 3. 어려움 (0 = 난이도 설명보기): "))
        if level == 1:
            try_num = 10
            print(f"쉬움 난이도가 선택되었습니다. {try_num}번의 기회와 {level+2}자리 숫자가 생성되었습니다.")
            break
        elif level == 2:
            try_num = 8
            print(f"보통 난이도가 선택되었습니다. {try_num}번의 기회와 {level+2}자리 숫자가 생성되었습니다.")
            break
        elif level == 3:
            try_num = 6
            print(f"어려움 난이도가 선택되었습니다. {try_num}번의 기회와 {level+2}자리 숫자가 생성되었습니다.")
            break
        elif level == 0:
            print("\n 쉬움 난이도: 3개 숫자, 10번시도\n 보통 난이도: 4개 숫자, 8번시도\n 어려움 난이도: 5개 숫자, 6번시도\n")
        else:
            print("0~3 숫자를 입력해주세요")

    # 랜덤 숫자 생성
    random_number_list = []
    random_number_list.append(str(random.randrange(10)))
    while len(random_number_list) < (level+2):
        random_number_list.append(str(random.randrange(10)))
        for index in range(len(random_number_list)-1):
            if random_number_list[index] == random_number_list[len(random_number_list)-1]:
                del random_number_list[len(random_number_list)-1]
    return random_number_list , try_num, level

def game_start(correct_game_numbers, limit_try_num, level):
    print("\n"+'*'*10 +'Bulls and Cows 게임을 시작합니다' +'*'*10 +'\n')
    s_dt = datetime.now()
    user_try_num = 0
    print(correct_game_numbers)   # 작동 점검용 정답 미리보기
    while user_try_num < limit_try_num:
        user_try_num = user_try_num + 1
        Bulls = 0
        Cows = 0
        input_numbers = list(input(f"{level+2} 개의 숫자를 입력해주세요: "))   # 사용자로부터 숫자 입력받음

        # 입력된 숫자와 정답 숫자 비교
        for index, num in enumerate(input_numbers):
            if num in correct_game_numbers:
                try:
                    if num == correct_game_numbers[index]:
                        Bulls = Bulls + 1
                    else:
                        Cows = Cows + 1
                except: break

        # 정답이 맞을 경우 승리 메세지 출력
        if Bulls == len(correct_game_numbers):
            e_dt = datetime.now()
            take_time = e_dt - s_dt
            print('\n맞추었습니다! 정답번호는 %s 입니다!' % ''.join(correct_game_numbers))
            print(f"시도 횟수: {user_try_num} 클리어 시간: {take_time}")
            print('\n'+'@'*15+'게임에서 이겼습니다. 축하드립니다!!' +'@'*15+ '\n')
            score_list = insert_score(user_try_num, level, str(take_time))               # 순위 입력 함수 호출
            if score_list:                                                          # 수정된 리스트가 있을경우 작동
                if len(score_list) > 10:                                            # 10명 이상 일경우 마지막 11등 삭제
                    score_list.pop()
                f_name = "score" + str(level) + '.txt'
                file = open(f_name, 'w')
                for r_list in score_list:
                    file.write(r_list)
                file.close()
            return
        # 게임마다 결과 공개
        print(f"\nBulls: {Bulls}  Cows: {Cows}  남은 횟수: {limit_try_num-user_try_num}")
    print('게임에서 졌습니다')

def insert_score(try_num, level, t_time):
    try:
        f_name = "score" + str(level) + '.txt'
        file = open(f_name, 'r')
        lines = file.readlines()
        file.close()
    except:                                         # 파일이 없을 경우 파일 생성
        name = input("명예의 전당에 등록할 이름을 입력하세요 (영문 세글자까지): ")
        user_full_name = name[:3] + ' ' + str(try_num) + ' ' + str(t_time) + '\n'
        f_name = "score" + str(level) + '.txt'
        file = open(f_name, 'w')
        file.write(user_full_name)
        file.close()
        return

    # 기록된 점수와 비교
    for index, full_score_line in enumerate(lines):
        name, score_try, score_time = full_score_line.split(' ')
        score_time_m = score_time[2:4]
        score_time_s = score_time[5:14]
        t_time_m = int(t_time[2:4])
        t_time_s = float(t_time[5:14])
        if try_num <= int(score_try):
            name = input("명예의 전당에 등록할 이름을 입력하세요 (영문 세글자까지): ")
            user_full_name = name[:3] + ' ' + str(try_num) + ' ' + str(t_time) + '\n'
            if try_num == int(score_try) and t_time_m <= int(score_time_m) and t_time_s < float(score_time_s):
                lines.insert(index, user_full_name)
                return lines                        # 수정된 점수 리스트를 반환
            lines.insert(index, user_full_name)
            return lines
    print("안타깝게도 순위권에 들지 못했습니다")

while True:
    start_number()
    if start_num == '1':
        correct_game_numbers, try_num, level = select_level()
        game_start(correct_game_numbers, try_num, level)
    elif start_num == 'q':
        print("게임을 종료합니다.")
        break
    else:
        print("1 또는 q 만 입력해주세요\n")


