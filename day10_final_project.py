"""
    Day10 Final Project
    2022. 8. 5. Fri
"""
"""
    1. 보물상자에서 랜덤으로 5개의 무기 중 하나를 획득한다.
    2. 길을 가다가 늑대, 산적, 드래곤 중 하나를 랜덤으로 만난다.
    3. 무기를 가지고 둘 중 하나의 에너지가 0이 될 때까지 싸운다.
       사용자는 공격, 회복 중 선택을 하고, 몬스터는 공격만 한다.
    4. 승리 또는 패배에 따라 메시지를 출력한다.
"""
from Color import *
import time

# 1.1 Opening
print('*' * 29)
cprint('운명의 데스티니 게임')
print('*' * 29)

# 1.2 보물상자를 발견했다는 메시지를 출력하고
# 사용자가 아무 키나 입력하기를 기다린다. (print, input)
print('당신은 길을 가다가 ' + YELLOW + '[보물상자]' + END + '를 발견하였습니다.')
time.sleep(1)   # 1초 쉬고 다음 줄 출력
input('Press Any Key ... to continue')

# 1.3 보물상자에서 랜덤으로 무기 1개를 획득한다.
#     각 무기는 ['무기이름', 최소공격력, 최대공격력]
#     random, list, if
myimage = '╰(*°▽°*)╯ '
monimage = ['ʕ•ﻌ•ʔ ♡  ', '◕‿◕✿      ', '(❁´▽`❁)    ']

import random as rd
weapons = [['휴지',1,3], ['목검',3,5],
           ['대검',5,10], ['대포',1,50], ['에픽검',50,100]]   # 이중 배열
sel = rd.randint(0, 4)
my_weapon = weapons[sel]
print(my_weapon)

if sel == 0:
    print('당신은 ' + '[{}({}-{})]'.format(my_weapon[0], my_weapon[1], my_weapon[2]) + '을(를) 획득하였습니다.')
elif sel == 1:
    print('당신은 ' + GREEN + '[{}({}-{})]'.format(my_weapon[0], my_weapon[1], my_weapon[2]) + END + '을(를) 획득하였습니다.')
elif sel == 2:
    print('당신은 ' + BLUE + '[{}({}-{})]'.format(my_weapon[0], my_weapon[1], my_weapon[2]) + END + '을(를) 획득하였습니다.')
elif sel == 3:
    print('당신은 ' + YELLOW + '[{}({}-{})]'.format(my_weapon[0], my_weapon[1], my_weapon[2]) + END + '을(를) 획득하였습니다.')
elif sel == 4:
    print('당신은 ' + MAGENTA + '[{}({}-{})]'.format(my_weapon[0], my_weapon[1], my_weapon[2]) + END + '을(를) 획득하였습니다.')

# 2.1 길을 가다가 랜덤으로 몬스터를 만난다.
monsters = [['늑대',1,3],['산적',5,10],['드래곤',1,100]]
sel = rd.randint(0, 2)
my_mon = monsters[sel]
if sel == 0:
    print('당신은 길을 가다가 ' + my_mon[0] + '를 만났습니다.')
elif sel == 1:
    print('당신은 길을 가다가 ' + GREEN + my_mon[0] + END + '을 만났습니다.')
elif sel == 2:
    print(REDBG + '당신은 길을 가다가' + END + ' ' + RED + my_mon[0] + END + '을 만났습니다.')

# 3.1 초기 양쪽의 에너지는 100
my_energy = 100
mon_energy = 100

# 데미지를 계산하는 함수
def cal_damage(mina=0, maxa=0, cri=50):
    # return 10
    damage = rd.randint(mina, maxa)
    if rd.randint(1,100) <= cri:
        damage = damage * 1.5
        print(RED + 'Critical Hit!!!' + END)
    return int(damage)   # * 1.5를 했을 때 소수로 나올 수 있기 때문

# 현재의 에너지 상태를 출력하는 함수
def print_energy(mye, mone):
    # print('공사중')
    print('당신의 에너지 : {}, 몬스터의 에너지 : {}'.format(mye, mone))
    print(myimage + ' ' * 11 + monimage[sel])
    if mye < 30:
        print(REDBG + ' ' * int(mye / 5) + END, end='')
    else:
        print(GREENBG + ' ' * int(mye / 5) + END, end='')
    print(' ' * (21-int(mye/5)), end='')   # 내 에너지와 몬스터 에너지 칸 사이에 1칸의 공백이 항상 있어야 하기 때문에 21
    if mone < 30:
        print(REDBG + ' ' * int(mye / 5) + END, end='')
    else:
        print(GREENBG + ' ' * int(mone/5) + END, end = '')
    print()

# 3.2 무한루프로 전투를 한다. 둘 중 하나의 에너지가 0 이하가 되면 끝난다.
while True:
    # 3.3 사용자는 공격(1) 또는 회복(2)를 선택한다.
    while True:
        user_input = input('행동을 선택하십시오(1.공격, 2.회복) : ')
        if user_input in ['1','2']:
            break
        print('잘못 입력하셨습니다.')

    # 3.4 공격을 선택했다면 최소, 최대 공격력 사이로 공격을 한다.
    if user_input == '1':
        # 데미지를 계산한다.
        damage = cal_damage(my_weapon[1], my_weapon[2], 30)
        print('당신이 공격하여 몬스터는 {}의 데미지를 입었습니다.'.format(damage))
        # 몬스터 에너지에서 데미지를 뺀다.
        mon_energy = mon_energy - damage
        # 현재 상태를 출력한다.
        print_energy(my_energy, mon_energy)
        # 몬스터 에너지가 0 이하가 되면 루프를 탈출한다.
        if mon_energy <= 0:
            break
    # 3.5 회복을 선택했다면 0부터 30사이로 회복을 한다.
    elif user_input == '2':
        # 회복량을 계산한다.
        heal = rd.randint(0, 30)
        print('회복을 선택하여 {}의 에너지가 회복되었습니다.'.format(heal))
        # 에너지를 회복시킨다.
        my_energy = my_energy + heal
        if my_energy >= 100:
            my_energy = 100
        # 현재 상태를 출력한다.
        print_energy(my_energy, mon_energy)

    time.sleep(1)

    # 3.6 몬스터가 최소, 최대 공격력 사이로 공격을 한다.
    damage = cal_damage(my_mon[1], my_mon[2], 20)
    print('{}의 공격으로 {}의 피해를 입었습니다.'.format(my_mon[0], damage))
    # 내 에너지에서 데미지를 뺀다.
    my_energy = my_energy - damage
    print_energy(my_energy, mon_energy)
    if my_energy <= 0:
        break

# 4. 결과를 출력한다.
print('-' * 60)
if my_energy > 0:   # 승리
    print('당신은 몬스터에게 승리하였습니다.')
    print('몬스터는 당신에게 자신보다 강한 자가 2323명 더 있다고 합니다.')
else:   # 패배
    print('당신은 몬스터에게 패배하였습니다.')
    print('몬스터는 당신의 명품 가방을 가져갔습니다.')
    print('##$%#@#$%%#$#%#')

# 5. Ending
print('*' * 29)
cprint('전설의 레전드 게임 종료')
print('*' * 29)