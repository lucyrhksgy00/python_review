from Color import *

cprint('String Advanced')
print('1) find')
s1 = 'my name is messi'
print(s1.find('mes'))
print(s1.find('mesi'))   # 못 찾으면 -1
print('messi' in s1)

# 대소문자 관계없이 찾는 방법
print('MESSI'.lower() in s1.lower())

# 각 단어의 첫 글자를 대문자로
print(s1.title())

# lstrip, rstrip, strip
s3 = '          I am a Super Programmer!@@@@@@11111@@@@@11111'
s4 = s3.lstrip(' ')
print(s3)
print(s4)
s5 = s4.rstrip('@r1!')   # 각각을 다른 글자로 생각해야 함
                         # 오른쪽부터 문자열에 포함된 글자면 삭제
                         # 아닌 글자를 만날 때까지 지움
print(s5)

# 문자열 slicing
print(); print('String Slicing')
a = 'abcdefg'
print(a[0], a[1], a[3], a[5])
print(a[1:3])
print(a[3:])
print(a[3::2])
# 돌발퀴즈
print(a[::-1])   # 증감값이 음수면 무제한의 범위가 바뀜 (오른쪽, 왼쪽)

print()
cprint('집합객체 복사하기')
a = list(range(1,11))
print(a)
# b는 a[1]부터 끝까지 복사
b = a[1:]
print(b)

c = (1, 2, 3, 4, 5)   # 튜플
# d는 2, 4만 복사
d = c[1::2]
print(d)

# SET
e = {1, 2, 3, 4, 5}
# f = e[1]   # 오류, 인덱스가 존재하지 않음
f = list(e)
f = f[1:3]
f = set(f)
print(f)

print()
cprint('User Function')
print("Type 1")
def welcome():
    print('Welcome to my world in Europa')

basket = welcome()
print(basket)

print()
print("Type 2")
def printMessage1(message):
    print(message + " 같은 건 전송하지 마라")

printMessage1("우리의 고향")
# printMessage1()   # 변수를 무조건 받는 함수인데 안 주면 오류

def printMessage2(message="너 빈손일 줄 알았다"):
    print(message)
    if message != "너 빈손일 줄 알았다":
        print("웬일이냐")

printMessage2()
printMessage2("뭐라고?")

def printMessage3(message="침묵", i=5):
    for j in range(i):
        print(message)

printMessage3()
printMessage3("이거 출력해봐봐", 10)
printMessage3(500)   # 하나만 입력하면 앞의 인자로 들어간다.
printMessage3(i=3)

print()
print("Type 3")
import random
def getCritical(ratio):
    num = random.randint(0, 100)
    if num <= ratio:
        return "Critical"
    else:
        return "Normal"

isCritical = getCritical(99)
print(isCritical)

print()
print("Type 4")
def getPizzaPiece():
    i = random.randint(1, 8)
    j = random.randint(0, 8-i)
    k = 8 - i - j
    return i, j, k

james, john, mary = getPizzaPiece()
print("James {}, John {}, Mary {}".format(james, john, mary))

print()
print("Type 5")
# 숫자 입력을 받아 모두 더한 결과를 돌려주는 함수
def getAmount(*amt):
    result = 0
    for j in amt:
        result = result + j
    return result

today_sum = getAmount(100, 200, 300, 800, 2, 278, 2635235)
print("오늘의 총 소득은", today_sum, "$")