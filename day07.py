# import Color
# Color.cprint("13. enumerate, zip")
from Color import *

cprint("13. enumerate, zip")
student = ['A', 'B', 'C', 'D']
print(enumerate(student))   # 저장 정보 알려줌
student_e = list(enumerate(student))
print(student_e)

for s1, s2 in enumerate(student):
    print(s1, s2)

student_s = [30, 20, 100, 0]
print(zip(student, student_s))
print(list(zip(student, student_s)))

for s1, s2 in zip(student, student_s):
    print(s1, s2)

print()
cprint('Method of List')
list_a = [1, 2, 3]
print('#1', list_a)
# list_a[3] = 4   # 불가; index out of range
list_a.append(4)
print('#2', list_a)
list_a.append("abcde")   # list는 잡식성
print('#3', list_a)
print('#4', list_a[2] * list_a[4])   # 숫자 * 문자열 = 문자열 숫자만큼 반복됨

# 번외편
house = []   # 일반적으로 파이썬은 초기화가 불필요하나, 메서드를 사용하기 위해서는 빈 것이라도 만들어줘야 함
house.append("John")
print(house)

list_a.insert(2, 65555)
print('#5', list_a)   # 원래 2번 자리에 있던 element부터 뒤로 한 칸씩 밀림

a = [4, 5, 6, 7, 8]
b = (4444, 5555)
c = {123, 456, 789}
list_a.extend(a)
print('#6', list_a)
list_a.extend(b)
print('#7', list_a)
list_a.extend(c)
print('#8', list_a)

basket = list_a.pop()   # 제일 뒤에 있는 element를 꺼냄; list에서 없앰
dish = list_a.pop(0)   # 제일 앞에 있는 element를 꺼냄; list에서 없앰
print('#9', basket, dish)   # '789'와 '1' 출력
print('#9', list_a)   # '789'와 '1'을 제외하고 출력

g = list_a.index(4444)
print('4444는 {}번 인덱스에 존재함'.format(g))
# g2 = list_a.index(4444, 11)   # 인덱스 11번부터 찾으라고 지시 => 못 찾으면 ValueError
h = list_a.remove(8)   # remove는 리턴값이 없음 (None); h에 저장하는 것은 무의미
print('삭제 결과는 :', h)
# list_a.remove(9876)   # 지울게 없으면 ValueError
print('#10', list_a)

list_a.clear()
print('#11', list_a)

print()
print()
cprint('Set Method')
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a.intersection(b)   # 교집합
d = a.union(b)   # 합집합
e = a.difference(b)   # 차집합
print(c, d, e, sep = '|')

print()
cprint('Dictionary Method')
dic = {
        1:'one',
        'subject':['sci', 'kor'],
        '숫자':1234
      }   # 이 괄호는 줄 위치 상관 없음

print(dic[1])
print(dic.get(1))

# print(dic[8])   # 없는 key 찾으면 KeyError
print(dic.get(8))   # 없는 key 찾으면 'None'
print(dic.get(8, '그런값없어임마'))   # '8'을 못 찾았을 시 '그런값없어임마'로 대체
print(dic.get(8, dic.get(1)))   # 함수로도 대체 가능
print(dic.get(8, cprint("Are You Crazy")))   # 출력 후 cprint의 리턴 값이 없으니 'None' 출력