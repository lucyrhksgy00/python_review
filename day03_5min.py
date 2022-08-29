"""
    Day3 5 min Challenge
"""
from Color import *
# 0. Intro
print('\033[95m' + "양음0 판독기!!!" + END) # 색 입력은 항상 END로 끝내야함

# 1. 사용자로부터 숫자 입력을 하나 받는다 (소수점 가능).
num = input(RED + "숫자를 입력하시오 (소수점 가능) : " + END)
num = float(num)
# 또는, num = float(input(RED + "숫자를 입력하시오 (소수점 가능) : " + END))

# 2. 입력한 숫자가 양수, 0, 음수에 따라 메시지를 출력한다.
if num > 0:
    print("숫자는 " + GREEN + "양수 " + END + "입니다.")
elif num == 0:
    print("숫자는 0입니다.")
else:
    print(RED + str(num) + END + " 은/는 음수입니다.")