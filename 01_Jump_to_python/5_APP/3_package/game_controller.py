import sys
sys.path.append('./new_pkg')
#import game.sound.echo
#game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# 만약에 sound, play패키지 안에 모두 echo모듈이 있고 아래와 같이 동일한 함수가 있다면
# '모듈.함수()' 로 구별하여 호출해야 한다.
# from game.play.echo import echo_test
# from game.sound.echo import echo_test
# echo_test()
#
# from game.sound import *
# echo.echo_test()
# wave.wave_test()

from game.graphic.render import render_test
render_test()
