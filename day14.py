from Color import *

cprint("List")
alist = [1, 2, 3, 4, 5]
print(alist)
print(len(alist))

blist = [1, 2, [3, 4], 5]
print(len(blist))

blist.append(6)   # 맨 뒤에 6을 추가
print("#1", blist)
blist.insert(1, 7)   # 1번 인덱스 자리에 7을 추가
print("#2", blist)
blist.insert(6, 10)   # 6번 인덱스 자리에 10을 추가; 16 이나 106으로 인덱스를 설정해도 제일 위치에 10 추가
print("#3", blist)
# 맨 뒤의 값을 ppp에 저정하고 삭제
ppp = blist.pop()
print("#4", ppp, blist)
# 맨 앞의 값을 qqq에 저장하고 삭제
qqq = blist.pop(0)
print("#5", qqq, blist)

# list Challenge 1
clist = [100, 200, 300, 400, 500]
# result = [500, 400, 300, 200, 100]
result = clist[::-1]   # Day05 참고; 배열을 역순으로 복제; start:stop:step
print(result)

# list Challenge 2
list1 = ['M', 'na', 'i', 'Ke']
list2 = ['y', 'me', 's', 'lly']
# result = ['My', 'name', 'is', 'Kelly']

# solution1
result = []
for i in range(0, len(list1)):
    result.append(list1[i] + list2[i])
print("Q2(s1) :", result)

# solution2
result = []
for i, j in zip(list1, list2):   # Day07 참고
    result.append(i + j)
print("Q2(s2) :", result)

# solution3
result = [i+j for i, j in zip(list1, list2)]
print("Q2(s3) :", result)

# list Challenge 3
list3 = [1, 2, 3, 4, 5]
# result = [1, 4, 9, 16, 25]
result = [i**2 for i in list3]   # **은 제곱 표현할 때 사용
print("Q3 :", result)

# list Challenge 4
list4 = ['Hello', 'Make']
list5 = ['Bye', 'Sleep']
# result = ['Hello Bye', 'Hello Sleep', 'Make Bye', 'Make Sleep']
result = [i+' '+j for i in list4 for j in list5]   # 이중 for문 사용
print("Q4 :", result)

# list Challenge 5
list6 = [10, 20, 30, 40]
list7 = [100, 200, 300, 400]
"""
result
10 400
20 300
30 200
40 100
"""
print("Q5 :")
for i, j in zip(list6, list7[::-1]):
    print(i, j)

# list Challenge 6
list8 = [5, 10, 15, 20, 25, 30, 35, 40]
# 20을 200으로 변경 : list8[3] = 200
list8[list8.index(20)] = 200
print('Q6 :', list8)
print()

cprint("Stack")
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack :", stack)
stack.pop()
stack.pop()
print("Stack after pop 2 times :", stack)

class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print()

# queue
#1. List로 구현
cprint("Queue")
queue1 = []
queue1.append(1)
queue1.append(2)
queue1.append(3)
print("My Queue :", queue1)
queue1.pop(0)
queue1.pop(0)
print("My Queue after pop 2 times :", queue1)

#2. Queue 클래스로 구현
import queue
import time
size = 100000

q1 = queue.Queue()
time1 = time.time()
for i in range(size):
    q1.put(i)
for i in range(size):
    q1.get(i)
time2 = time.time()

q2 = []
time3 = time.time()
for i in range(size):
    q2.append(i)
for i in range(size):
    q2.pop(0)
time4 = time.time()

print(time.ctime())
print("Queue(class) :", time2 - time1)
print("Queue(mine) :", time4 - time3)