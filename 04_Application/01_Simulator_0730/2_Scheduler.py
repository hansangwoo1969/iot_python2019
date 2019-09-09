import threading
import time
import ctypes

g_Balcony_Window = False
g_AI_Mode = False
schedule_cycle = 5

def terminate_ai_mode():
    """Terminates a python thread from another thread. 다른 스레드로부터 파이썬 스레드를 종료
    :param thread: a threading. Thread instance
    """
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # ""if  it returns a number greater than one, you're  in  trouble,
        # and you should call it again with exc=NULL to revert the effect.
        # 1보다 큰수는 문제가 있다, 효과를 되돌리려면 'exc=NULL'로 다시 호출할 것. """
        ctypes.pythonapi.PyThreadState_SetAsyncExec(ai_scheduler.ident,  None)
        raise SyntaxError("PyThreadState_SetAsyncExc  failed")


def update_scheduler():       # 인공지능 쓰레드 작동되는 코드,,,
    while True:
        time.sleep(schedule_cycle)

        print(f"스케쥴러 작동..  {schedule_cycle}초 주기")

while True:
    print("메뉴를 선택하세요 ")
    print("1. 장비상태 조회")
    print("2. 인공지능 모드 변경")
    print("3. 종료")

    menu_num = int(input("메뉴 입력: "))
    if (menu_num ==  1):
        print("발코니(베란다) 창문: ", end="")
        if g_Balcony_Window==True: print("열림")
        else: print("닫힘")
    elif(menu_num ==2):
        print("인공지능 모드: ", end="")
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode==True:
            ai_scheduler = threading.Thread(target=update_scheduler) # target=update_sheduler()이 아님에 주의
            ai_scheduler.daemon=True     # 부모가 종료되면 즉시끝나게 하기 위해 True, start이전에 사용
            # 데몬 쓰레드:백그라운드에서 실행되는 쓰레드로 메인 쓰레드가 종료되면 즉시 종료되는 쓰레드
            # 데몬 쓰레드가 아니면 해당 서브쓰레드는 메인 쓰레드가 종료할 지라도 자신의 작업이 끝날 때까지 계속 실행
            #  Thread 객체의 daemon 속성을 True로 설정한 후 start() 하면, 해당 서브쓰레드는 데몬 쓰레드가 되고
            #  메인 쓰레드가 곧바로 종료되면 바로 데몬 쓰레드를 종료하게 된다.
            #
            #  daemon 속성은 디폴트로 False 이므로 별도로 지정하지 않으면 메인 쓰레드가 종료되어도
            #  서브쓰레드는 끝까지 작업을 수행한다.

            ai_scheduler.start()
            print("작동 완료!")
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass

            print("정지 완료!")
    else: break






