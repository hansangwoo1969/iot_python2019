# os모듈을 사용하여 다음과 같이 동작하도록 코드 작성
# C:\iot_bigdata\python_workspace\01_Jump_to_python\5_APP\6_exterior_function
import os

# C:\iot_bigdata\python_workspace\01_Jump_to_python\5_APP\6_exterior_function 로 이동
os.chdir("C:\\iot_bigdata\\python_workspace\\01_Jump_to_python\\5_APP\\6_exterior_function")
# print(os.getcwd())

# dir명령을 실행하고 그 결과를 변수에 담는다
f = os.popen("dir")

# dir 명령의 결과를 출력
print(f.read())