print('작업1')

try:
    f = open('나없는 파일', 'r')
except:
    print(""" '나없는 파일'이 없습니다.
    파일을 준비하고 다시 수행하십시오.
    """)

print('작업2')
print("정상종료")
