from os import system
from sys import stdout
from random import randrange
from datetime import datetime
from time import time, gmtime, strftime, sleep
from getpass import getuser
from msvcrt import kbhit

def rotation(speed:float):
    load = ['/', '-', '\\', '|', '-']
    for i in load:
        stdout.write('\b')
        stdout.write(i)
        stdout.flush()
        sleep(speed)
    return

def random_color() -> int:
    if randrange(1,4) == randrange(1,4):
        random = randrange(randrange(1,4),randrange(4,10))
    elif randrange(randrange(1,4),randrange(4,10)) > randrange(randrange(1,4),randrange(4,10)):
        random = randrange(randrange(randrange(1,2),randrange(2,4)),randrange(4,randrange(5,10)))
    else:
        random = randrange(randrange(randrange(1,3),4),randrange(4,randrange(5,10)))
    if random == randrange(3,5):
        random = random_color()
    return random

def title_bar() -> str:
    print("""
              _                 _    _            ______  _____    ___ 
             | |               | |  | |           | ___ \|  _  |  |_  |
  ___  _ __  | |_   ___  _ __  | |_ | |__    ___  | |_/ /| | | |    | |
 / _ \| '_ \ | __| / _ \| '__| | __|| '_ \  / _ \ | ___ \| | | |    | |
|  __/| | | || |_ |  __/| |    | |_ | | | ||  __/ | |_/ /\ \_/ //\__/ /
 \___||_| |_| \__| \___||_|     \__||_| |_| \___| \____/  \___/ \____/""")
    print("""
     ██ ██    ██ ███████ ████████     ██████   ██████      ██ ████████ 
     ██ ██    ██ ██         ██        ██   ██ ██    ██     ██    ██    
     ██ ██    ██ ███████    ██        ██   ██ ██    ██     ██    ██    
██   ██ ██    ██      ██    ██        ██   ██ ██    ██     ██    ██    
 █████   ██████  ███████    ██        ██████   ██████      ██    ██   """)

run = time()
title_bar()
default_color = random_color()
system(f'color {abs(default_color-random_color()) if default_color == 4 or default_color == random_color() else default_color}')
while 1:
    check = True
    stdout.write("엔터를 눌러 입력 시작 ")
    while(check):
        # print('w')
        check = not kbhit()
        rotation(0.05)
    input()
    bojkr = input(f"help or BOJ문제 번호|{getuser()}|:")
    if bojkr == 'help':
        print("time : 지금 시간이 나옵니다.")
        print("timer : 문제번호를 입력하고 지난 시간과\nboj오프너를 실행하고 지난 시간을 출력해줍니다")
        print("exit : 프로그램을 종료합니다.")
        print("color : 색상을 변경합니다.")
        print("start: 시간을 '초기화' 하고 타이머를 시작합니다.(타이머는 문제 번호 입력시 자동 시작 됩니다.)")
        print("title: 처음에 나오는 크레딧을 출력합니다.")
        print("※ 이 프로그램은 상단 타이틀 바 우클릭 -> 속성 -> 글꼴 에 있는 [NSinSum]글꼴을 지원합니다.")
    elif bojkr == 'time': print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    elif bojkr == 'timer' :
        try:elapsed_time = time() - start
        except: elapsed_time = 0
        elapsed_time = strftime("%H:%M:%S",gmtime(elapsed_time))
        R_elapsed_time = time() - run
        R_elapsed_time = strftime("%H:%M:%S", gmtime(R_elapsed_time))
        print(f"문제를 푸신지 {elapsed_time}의 시간이 지났으며")
        print(f"이 프로그램을 실행한지 {R_elapsed_time}의 시간이 지났습니다")
    elif bojkr == 'start':
        start = time()
    elif bojkr == 'title': title_bar()
    elif bojkr == 'exit': break
    elif bojkr == "color":
        print("""
색 특성은 두 자리의 16진수로 지정됩니다. 첫째 자리는
배경색에 해당하고 둘째 자리는 전경색에 해당합니다. 각 자리는
다음 값이 될 수 있습니다. 또한 한자리만 입력할 경우에는 글자색만 변경됩니다.
※ 본 설정은 새로운 문제 입력시 랜덤으로 초기화 됩니다.

    0 = 검은색       8 = 회색
    1 = 파란색        9 = 연한 파란색
    2 = 녹색       A = 연한 녹색
    3 = 청록색        B = 연한 청록색
    4 = 빨간색         C = 연한 빨간색""")
        system(f'color {input(" 위의 안내에 따라 16진수를 입력해주세요: ")}')
    elif bojkr == '':
        pass
    else:
        start = time()
        system(f"start \"\" https://boj.kr/{bojkr}")
        system(f'color {random_color()}')
    
    print('='*20+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    if randrange(randrange(0,50), 100) == 100:print("그거 아세요? 당신은 럭키가이 입니다!")
    if randrange(randrange(0,50), 100) == 51:print("그거 아세요? 색상은 랜덤 이랍니다!")
    if randrange(randrange(0,50), 100) == 10:print("그거 아세요? 그거 아세요?는 랜덤 이스터에그 랍니다!")
