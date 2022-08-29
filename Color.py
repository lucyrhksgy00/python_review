BLACK   = '\033[90m'
RED     = '\033[91m'
GREEN   = '\033[92m'
YELLOW  = '\033[93m'
BLUE    = '\033[94m'
MAGENTA = '\033[95m'
CYAN    = '\033[96m'
WHITE   = '\033[97m'

REDBG = '\033[101m'
GREENBG = '\033[102m'

END = '\033[0m'

import random

def cprint(str):
    # print("***** " + str + " *****")
    # 256색 중 하나를 랜덤으로 선택하여
    # ***** str *****을 출력하는 컬러타이틀 함수 구현
    col = random.randint(0, 255)
    print('\033[38;5;{}m'.format(col)
          + "***** " + str + " *****" + END)

# cprint("ehsldkfhskdi") # 주석으로 놓지 않으면 다른 데서 import 했을 때 실행됨