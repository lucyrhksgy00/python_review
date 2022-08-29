from Color import *

# 1. break
print(RED + '1. break' + END)
# 1~9까지 출력하는 예제
n = 1
while True:
    print(n)
    if n == 9:
        break
    n += 1

# 2. continue
print()
print(GREEN + '2. continue' + END)
print('1부터 9중에 3의 배수만 빼고 출력')
n = 1
while True:
    if n == 10:
        break
    elif n % 3 == 0:
        n += 1   # 이 부분이 없으면 무한 루프; n = 3일 때 계속 제일 위로 올라가서 이 부분에서 다시 걸림
        continue
    print(n)
    n += 1

print()
print(RED + '3. list' + END)
list_simple = [1, 2, 3]
print(list_simple[0])   # 첫번째 것
list_complex = [['AA', 'BB', 'CC'], ['DD', 'EE', 'FF']]
print(list_complex[1][1])   # EE를 의미
print(list_complex[1])   # 두번째 그룹 전체 출력
print(list_simple[1:])   # [1:3]과 동일

print()
print(RED + '4. Color' + END)
print(YELLOW + 'yellow' + END)
print(MAGENTA + 'magenta' + END)
print(CYAN + REDBG + 'AAAAAAAA' + END)
print(GREENBG + '        ' + END)

print()
# for문을 사용해서 8색으로 AAAA글자를 출력하시오.
for num in range(90, 98):
    print('\033[' + str(num) + 'm' + 'AAAA' + '\033[0m', end = '')

# 개선 방법
print()
for num in range(90, 98):
    print('\033[{}m'.format(num) + 'AAAA' + '\033[0m', end = '')

# 강사님 방법 1
print()
for n in range(8):
    print('\033[9{}m'.format(n) + 'AAAA' + '\033[0m', end = '')

# 강사님 방법 2
print()
for n in range(8):
    print('\033[9{}m'.format(n) + 'AAAA', end = '')
print('\033[0m')

# 강사님 방법 2
for n in range(8):
    print('\033[10{}m'.format(n) + '    ', end = '')
print('\033[0m')

# for문을 사용해서 배경색을 256색으로 ' '를 출력하시오.
for col in range(256):
    print('\033[48;5;{}m'.format(col) + ' ', end = '')
    # 16색마다 줄바꿈을 한다.
    if col % 16 == 15:   # 0부터 시작했기 때문에 15일 때 내려가야 함
        print(END)

# True Color
print()
for n in range(256):
    print('\033[48;2;{};{};{}m'.format(n, 0, 0) + ' ', end = '')
    if n % 64 == 63:
        print(END)

print()
for n in range(256):
    print('\033[48;2;{};{};{}m'.format(n, n, 0) + ' ', end = '')
    if n % 64 == 63:
        print(END)

print()
for n in range(256):
    print('\033[48;2;{};{};{}m'.format(n, n, n) + ' ', end = '')
    if n % 64 == 63:
        print(END)

print()
import random
for n in range(256):
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    print('\033[48;2;{};{};{}m'.format(c1, c2, c3) + ' ', end = '')
    if n % 64 == 63:
        print(END)