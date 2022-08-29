"""
    1. '이름을 입력하세요 : '를 출력하고 입력을 받는다.
    2. '최대 숫자를 입력하세요 : '를 출력하고 입력을 받는다.
    3. 1부터 입력한 수 사이의 임의의 수를 만든다.
    4. 숫자 입력을 받아 임의의 수와 같은지 맞추는 게임을 한다.
        정답은 몇일까요? 를 출력하고 입력을 받는다.
        임의의 수와 입력한 수가 동일할 때까지 계속한다.
        5번까지 못 맞추면 종료한다.
    5. 한 번에 정답을 맞추면 '***님 대단하십니다'
        세 번 이내에 맞추면 '***님 우수한 성적이십니다'
        다섯 번 이내에 맞추면 '***님 좀 심하십니다'
        다섯 번까지도 못 맞추면 '정답은 *입니다. ***님 진짜 너무하십니다'
"""
from Color import *
print(RED + "Test Your Luck" + END)

# 1
name = input('이름을 입력하세요 : ')

# 2
while True:
    num = input('최대 숫자를 입력하세요 : ')
    if num.isdecimal():   # 무조건 숫자를 입력해야함
        break

# 3
import random   # 랜덤 숫자 뽑기
rand_int = random.randint(1, int(num))   # randint 함수: input을 2개를 받아 2개 사이에 있는 숫자 하나를 임의로 출력함
# print(rand_int)   # type int, for debugging

# 4
count = 1
while True:   # 1) 정답을 맞춘다. 2) 5번 chance를 날린다.
    ans = input('정답은 무엇일까요? : ')   # type string
    if str(rand_int) == ans:
        break

    # if int(ans) == rand_int:
    #     print('{} 정답!'.format(int(ans)))
    # ans가 isdecimal인지 한번 더 확인해야함

    print("와 개노답. 완전 틀렸어요.")
    count = count + 1
    if count > 5:
        break

# 5
if count == 1:
    print("{}님 대단하십니다.".format(name))
elif count <= 3:
    print("{}님 우수한 성적이십니다.".format(name))
elif count <= 5:
    print("{}님 좀 심하십니다.".format(name))
else:
    print("정답은 {}입니다. {}님 진짜 너무하십니다.".format(rand_int, name))

print(GREEN + "세계적 대히트 게임 종료" + END)