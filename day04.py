"""
    Day04 - Control Statement
    Version : 1.0
    Created : 2022. 7. 21
    Updated : 2022. 7. 21
"""
from Color import *
print(RED + 'while' + END)
print('노가다')
print('1번 출력')
print('2번 출력')
print('3번 출력')
print('4번 출력')
print('5번 출력')
print('6번 출력')
print('7번 출력')
print('8번 출력')
print('9번 출력')
print('10번 출력')
print()

print('자동화')
i = 1
while i < 11:
    print('{}번 출력'.format(i))
    i = i + 1   # i += 1; 이 조건을 적지 않으면 i는 계속 1이어서 '1번 출력'이 무한 반복됨

i = 0
# while True:   # 무한 루프
#     print(i)
#     i = i + 1

# while True:   # 무한 루프
#     num = input("1에서부터 10까지의 숫자를 넣어봐라 : ")
#     if num.isdecimal() and int(num) >= 1 and int(num) <= 10:   # .isdecimal() : num이 숫자같이 생겼는지 확인하는 True/False
#         print('입력에 성공하셨습니다.')
#         break   # 제대로 입력했을 시 루프 탈출!
#     else:
#         print('너 지금 뭐하냐!!!! {} 입력했네?'.format(num))

print()
print(GREEN + 'for' + END)
print('[String]')
for s in "이걸한글자씩처리한다는말인가요":   # 문자열을 집합으로 인정
    print(s)

print()
print('[List]')
for l in ['first', 'second', 'rameon']:
    print(l)

print()
print('[Tuple]')
v4 = ('Spring', 'Summer', 'Fall', 'Winter')
for t in v4:
    print(t)   # 질서정연하게 출력됨

print()
print('[Set]')
v4 = {'Spring', 'Summer', 'Fall', 'Winter'}
for s in v4:
    print(s)   # 순서를 보장하지 않음; shuffle 기능으로 이용 가능

print()
v4 = {'Spring', 'Summer', 'Fall', 'Winter', 'Spring'}
for s in v4:
    print(s)   # 중복 제거 (overwrite)

print()
print('[Range]')
for i in range(1, 11):   # range, 11은 미포함
    print('{}번 출력'.format(i))

print()
print('[Dictionary]')
person = {'name':'Jungfrau', 'addr':'none'}
for pe in person:
    print('#1', pe)   # key인 'name'과 'addr'만 출력
    print('#1', person[pe], person.get(pe))   # 각 key들의 value들을 출력

for key, value in person.items():
    print('#2', key, value)