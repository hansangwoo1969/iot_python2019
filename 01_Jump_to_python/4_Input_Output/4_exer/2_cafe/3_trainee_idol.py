# "연습생.txt" 파일의 이름을 읽어와 리스트로 만든다.

def show_candidate(candidate_list):    # 현재 연습생 리스트 출력
    print("=== trainee===")
    for candidate in candidate_list:
        print(candidate, end='')


def make_idol(candidate_list):    # 이름 앞 뒤로 문구추가한 메시지 작성 "신예 아이돌 유라 인기 급상승
    print("\n=== candidate ===")
    for candidate in candidate_list:
        print("신예 아이돌 %s 인기 급상승" % candidate)

def make_world_star(candidate_list):  # 이름을 활용해 문구추가한 메시지 출력
    print("===  idol       ===")
    for candidate in candidate_list:
        print("아이돌 %s 월드스타 등극" % candidate)

with open("연습생.txt", 'r', encoding='UTF-8') as f:
    trainee_list=[]
    while True:
        trainee = f.readline()
        if not trainee: break
        trainee_list.append(trainee)

show_candidate(trainee_list)
make_idol(trainee_list)
make_world_star(trainee_list)

