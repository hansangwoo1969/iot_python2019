# glob모듈을 사용하여 C:\iot_bigdata\python_workspace\01_Jump_to_python\5_APP\6_exterior_function 디렉토리
# 파일의 확장자가 .py인 파일만 출력
import os, glob

print(os.getcwd())
os.chdir("C:\\iot_bigdata\\python_workspace\\01_Jump_to_python\\5_APP\\6_exterior_function")
print(os.getcwd())
# print(glob.glob("C:\\iot_bigdata\\python_workspace\\01_Jump_to_python\\5_APP\\6_exterior_function\\*"))
print(glob.glob("*.py"))


