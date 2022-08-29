"""
    Day07 Challenge
    Calculator for Engineering
"""
"""
    1. 무한루프로 사용자에게 수식을 입력받는다.
    2. 수식 대신 'X'를 입력하면 종료한다.
    3. 수식을 계산해서 수식과 결과를 출력한다.
       결과는 총 40칸으로 오른쪽 정렬한다.
    4. 사용자가 수식을 계속해서 입력하면 기존의 수식들을 출력하고
       기존 결과에 추가된 수식을 계산한 결과를 출력한다.
    5. 수식 대신 'C'를 입력하면 0을 출력하고 수식들을 다 비운다.
"""
from Color import *

# 0. 타이틀을 출력한다.
cprint("Calculator for Engineering")

isFirst = True   # isFirst 대신 res = ""를 사용하는 방법도 있음
exp_list = []

# 1. 코드
while True:
    exp = input('수식을 입력하십시오 (종료는 X, 초기화는 C) : ')

    # X를 입력하면 종료한다. C를 입력하면 초기화된다.
    if exp == 'X':
        break
    elif exp == 'C':
        exp_list.clear()
        isFirst = True
        print('-' * 40)
        print(format(0, '>40'))
        continue   # 노트 확인하기!!!!!

    # 수식을 계산한다.
    if isFirst == True:
        res = eval(exp)   # day06.txt 참고!!!
        isFirst = False
    else:
        res = eval(str(res) + " " + exp)

    # 수식을 저장한다.
    exp_list.append(exp)

    # 수식을 출력한다.
    # print(exp_list)
    for e1, e2 in enumerate(exp_list):
        if e1 == len(exp_list) - 1:   # 맨 마지막 수식이면
            print(RED + format('[' + e2 + ']', '>40') + END)
        else:
            print(GREEN + format('[' + e2 + ']', '>40') + END)

    # 결과를 출력한다.
    # 우측정렬하고 40자리
    print(YELLOW + '-' * 40 + END)
    print(format(res, ">40"))
    print()