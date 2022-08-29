from Color import *

cprint('Global Variables')

# 1단계
gv = 10

def printV1():
    print('1-1단계 gv :', gv)

printV1()
print('1-2단계 gv :', gv)

# 2단계
def printV2():
    lv = 20
    print('2-1단계 gv :', gv)
    print('2-2단계 lv :', lv)

printV2()
print('2-3단계 gv :', gv)
# print('2-4단계 lv :', lv)   # lv는 함수 내에서 사용된 로컬변수이므로

# 3단계
def printV3():
    # print('3-1단계 gv :', gv)
    gv = 30
    lv = 30
    print('3-2단계 gv :', gv)   # lv와 같은 로컬변수; global 'gv'와 다름
    print('3-3단계 lv :', lv)

printV3()
print('3-4단계 gv :', gv)   # global 'gv'
# print('3-5단계 lv :', lv)

# 4단계
def printV4(gv):
    # gv = 받은 값
    print('4-1단계 gv :', gv)
    gv = 40
    lv = 40
    print('4-2단계 gv :', gv)
    print('4-3단계 lv :', lv)

printV4(gv)
print('4-4단계 gv :', gv)

# 5단계
def printV5():
    lv = 50
    return lv

gv = printV5()
print('5단계 gv :', gv)

# 6단계
gv1 = 61
gv2 = 62

def printV6():
    global gv1
    gv1 = 601
    globals()['gv2'] = 602   # global에서 gv2를 찾아서 값을 바꿈
    gv2 = 700   # 로컬변수 gv2

printV6()
print('6-1단계 gv1 :', gv1)
print('6-2단계 gv2 :', gv2)

# 7단계
# gv1 = 700
if gv1 == 601:
    local_new = 300

print('7-1단계 local_new :', local_new)

i = 27632
for i in range(5):
    print(i)
print('7-2단계 i :', i)

print()
cprint('random module')
import random
list1 = ['a', 'b', 'c']
tuple1 = ('A', 'B', 'C')
set1 = {'1', '2', '3'}   # set는 정해진 index가 없으므로 choice 불가능
print(random.choice(list1))
print(random.choice(tuple1))
print(random.choice(list(set1)))
# print(random.choice(list1.extend(tuple1).extend(set1)))
list1.extend(tuple1)
list1.extend(set1)
print(list1)

# Random으로 순서를 재배열할 때 사용하는 trick (shuffle할 때 사용)
list2 = random.sample(list1, len(list1))
print(list2)

print()
cprint('time module')
import time
t1 = time.time()
t2 = time.ctime()
t3 = time.strftime('%Y/%m/%d %H:%M:%S')
print(t1, t2, t3)

print()
cprint('file')
s1 = 'We are the future'
s2 = '파이썬 공부하십니까?'

f1 = open('sample1.txt', 'wt')   # write text
f1.write(s1)
f1.write('\n')
f1.write(s2)
f1.close()

f2 = open('sample2.txt', 'wt', encoding='utf-8')
f2.write(s1)
f2.write('\n')
f2.write(s2)
f2.close()

f3 = open('../memo/day09.txt', 'rt', encoding='utf-8')
while True:
    readstr = f3.read(10)
    if readstr == '':
        break
    print(readstr, end='')
f3.close()

f4 = open('sample1.txt', 'rt')
while True:
    readstr = f4.read(10)
    if readstr == '':
        break
    print(readstr, end='')
f4.close()
print()

f5 = open('sample2.txt', 'rt', encoding='utf-8')
while True:
    readstr = f5.readline()
    if readstr == '':
        break
    print(readstr, end='')
f5.close()
print()

f6 = open('sample2.txt', 'rt', encoding='utf-8')
readstr = f6.readlines(18)
print(readstr)
f6.close()