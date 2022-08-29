import numpy as np
from Color import *

# 1. 행렬의 생성 1
cprint('1-1) 1차원 행렬')
a1 = np.array([1,2,3])
print(a1, type(a1), a1 * 3)

l1 = [1, 2, 3]
print(l1, type(l1), l1 * 3)

cprint('1-2) 2차원 행렬')
a2 = np.array([[1,2,3],[4,5,np.NaN]])
# NaN : 미정의 숫자 (NaN을 소수점이 있는 큰 수로 생각하기 때문에 소수점(.)이 붙음)
print(a2)

cprint('1-3) 행렬의 차원과 모양 확인')
print('차원 :', a1.ndim, a2.ndim)
print('모양 :', a1.shape, a2.shape)   # 1차원의 모양 잘 기억하기!
print()

cprint('1-4) 행렬의 모양 변경')
na = np.array(range(10))
print(na, '길이 :', len(na))
nb = na.reshape(2, 5)
print('reshape 적용완료!')
print(nb)
print()

cprint('2) 행렬 데이터의 선택')
a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3)

# 1) 데이터의 선택
print()
print('a3[1] :\n', a3[1])
print('a3[1][0] :', a3[1][0])
print('a3[1][0][2] :', a3[1][0][2])

# 2) []의 생략이 가능
print('a3[1,0,2] :', a3[1,0,2])

# 3) 범위로 선택 가능
print('a3[1:,:,:2] :]\n', a3[1:,:,:2])
# 1로 시작해서 무한까지 (1번만 존재하니 1번만 선택)
# 무제한 처음부터 무제한 끝까지 선택
# 무제한 처음부터 1까지 (0, 1 선택)
print('a3[1:,:,1:] :\n', a3[1:,:,1:])
print('a3[1:,:,:1] :\n', a3[1:,:,:1])

# 4) 데이터 수정
a1 = np.array(range(5))
a1[2] = 0
print(a1)

# 5) 브로드캐스팅 수정
cprint('2-5) 브로드캐스팅 수정')
a1 = np.array(range(5))
print(a1)
# a1[1::2] = 0
a1[3:] = 0
print(a1)

# 3. 행렬의 생성 2
print()
cprint('3. 행렬의 생성 2')
print('3-1) zeros')
zero = np.zeros((2,3))
print(zero)
print()
print('3-2) ones')
ones = np.ones((4,3), dtype=int)
print(ones)

"""
Quiz 1
numpy를 사용하여 5개의 1로 이루어진 정수 타입의 1차원 행렬을 만드시오
q1 = [1 1 1 1 1]
"""
print()
print("----- Quiz 1 -----")
# q1 = np.ones((1,5), dtype=int)[0]
# q1 = np.ones((5,), dtype=int)
q1 = np.ones(5, dtype=int)
print(q1)

"""
Quiz 2
10개의 1로 만들어진 정수 데이터 타입의 벡터에서
마지막 5개는 5로 바꾸시오.
q2 = [1 1 1 1 1 5 5 5 5 5]
"""
print('----- Quiz 2 -----')
q2 = np.ones(10, dtype=int)
q2[5:] = 5
print(q2)

# 4. arange 만들기
print()
cprint('4. arange')
ar1 = np.array(range(10))
print(ar1)
ar2 = np.arange(10)
print(ar2)
ar3 = np.arange(5, 10, 2)
print(ar3)

# 5. linspace, logspace
print()
cprint('5. linspace, logspace')
e51 = np.linspace(0, 100, 5, dtype=int)
print(e51)   # 0 앞에 space가 있는 이유는 가장 큰 자릿수를 가진 100을 따르기 때문
e52 = np.logspace(0, 2, 5)   # 0, 2는 각각 10의 0제곱 1, 10의 2제곱 100을 의미
print(e52)

"""
Quiz 3
numpy를 사용하여 1에서 10까지의 홀수 데이터를 갖는 벡터를 만드시오.
q3 = [1 3 5 7 9]
"""
print()
print('----- Quiz 3 -----')
q3 = np.arange(1, 10, 2)
# q3 = np.linspace(1, 9, 5, dtype=int)
print(q3)

"""
Quiz 4
0부터 8까지의 값을 갖는 3x3 행렬을 만드시오.
"""
print('----- Quiz 4 -----')
q4 = np.arange(9).reshape(3,3)
print(q4)

# 6. Numpy Random
cprint('numpy.random')
print('1) seed')
np.random.seed(1)
result1 = np.random.randint(low=10, high=100, size=10)
np.random.seed(1)
result2 = np.random.randint(low=10, high=100, size=10)
np.random.seed(None)   # seed 무효화
result3 = np.random.randint(low=10, high=100, size=10)
np.random.seed(4294967295)   # seed는 2의 32제곱 - 1까지
result4 = np.random.randint(low=10, high=100, size=10)
print(result1)
print(result2)
print(result3)
print(result4)

print()
print('2) rand')
rd = np.random.rand(10)
print(rd)

print()
print('3) randn')
rd = np.random.randn(100)
print(rd)

print()
print('4) randint')
np.random.seed(None)
rd = np.random.randint(5, 10, (2,3))
print(rd)
print()
rd = np.random.randint(5, size=(4,3))   # 0부터 5까지
print(rd)

print()
print('5) shuffle')
rd = np.random.randint(1, 10, (3,4))
print(rd)
np.random.shuffle(rd)
print(rd)

# 전체를 섞는 방법
print()
print('전체 섞기')
rd = np.random.randint(1, 10, (3,4))
print(rd)

# 1차원으로 변경
rd_1 = rd.reshape(rd.size)
print('1차원으로 변경 :', rd_1)
# shuffle
np.random.shuffle(rd_1)
print('after shuffle :', rd_1)
# 원래 차원으로 복귀
result = rd_1.reshape(rd.shape)
print('final')
print(result)

# choice
print()
print('6) choice')
c = np.random.choice(5, 10, p=[0.3, 0.3, 0.4, 0, 0])
# 0부터 4까지의 수 중에서 10개를 정해진 확률에 따라 선택
print(c)

d = np.random.choice(['normal', 'magic', 'legend'], 100, p=[0.8, 0.199, 0.001])
print(d)