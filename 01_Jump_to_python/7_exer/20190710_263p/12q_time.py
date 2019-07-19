# time모듈을 사용하여 현재날짜와 시간을 다음과 같은 형식으로 출력  2018/04/03 17:20:32

import time

print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))