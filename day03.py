from Color import *

print(RED + "Day03. Operator" + END)
print('(1)산술연산자')
a = 'My name'
b = 'is None'
print(a + ' ' + b)
c = 'I\'ll be '
d = 100
print(c + str(d))

print('(2)비교연산자')
a = 30
b = 20
c = a > b
print(c, type(c)) # bool: True/False
print('10 == 20 :', 10 == 20)

print('(3)논리연산자')
a = -30 # 온도
b = 1 # 내복 착용 여부

c = a < -10 and b == 0 # 영하 10도 이하이고 내복이 없고
d = a < -10 or b == 0 # 영하 10도 이하거나 내복이 없거나; 로직을 잘못짜면 내복이 있어도 지급

print(c, d)

e = True ^ False ^ False # True, False 달라서 True
# False ^ False부터 계산하고 싶으면 괄호
print(e)

# String.format
print('{}은 또 하나의 {}함수 {}입니다.'.format('이것', 'print', '사용법'))
print('숫자도 되는지 해보죠 {}'.format(10))
print('되네요. 괄호보다 입력이 더 많을 때에는 {}'.format('되네', '궁금')) # '궁금'은 무시
# print('괄호보다 입력이 더 적을 때에는 {} {}'.format(10))

print("#" * 40)
print('이름:{name} 주소:{addr}'.format(name = 'Unknown', addr = 'None'))
print("#" * 40)
print('이름:{1} 주소:{0}'.format('Unknown', 'None')) # format 순서대로 0, 1이어서 0에 Unknown, 1에 None 대입

# if Statement
print()
print(RED + "Day03. If statement" + END)
print('*** a = 1 ***')
a = 1 # a = 0일 때 아무것도 출력하지 않음
if a > 0:
    print('a는 positive')
if a == 1:
    print('a는 1')
if not a != 1:
    print('a는 1이 아닌게 아님')

a = -100
if a > 0:
    print('a는 positive2')
      # print('a는 positive3') # 오류 : 파이썬은 들여쓰기 (indent)가 매우 중요
   # print('a는 positive4') # 윗 줄보다 들여쓰기 레벨이 높아도 안됨
print('a는 positive5') # if랑 동급; 아무데도 소속되어 있지 않기 때문에 항상 프린트 됨

# if a < 0: print('a는 positive6') # if문 줄에 실행문을 넣으면
#           print('a는 positive7') # 아래 줄은 들여쓰기를 맞춰도 X
if a < 0: print('a는 positive8'); print('a는 positive9') # 됨!

# if a = 2: # 파이썬은 할당자를 조건문에 넣을 수 없음
#     print('a는 2')

isRainy = True

if isRainy:
    print('우산 가져가')
else:
    print('우산 두고가')

c = 60
if c > 50: # 범위 잘 설정할 것!
    print('c는 big positive')
elif c > 0:
    print('c는 positive')
elif c == 0:
    print('c는 zero')
else:
    print('c는 negative')