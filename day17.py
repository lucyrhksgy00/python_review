import numpy as np
from Color import *

cprint('7) unique')
rd = np.random.randint(1, 10, (3, 4))
print(rd)
number, count = np.unique(rd, return_counts=True)
print('unique한 값은', number)
print('unique한 값의 개수는', count)

# zip으로 number와 count를 묶는 방법 (day07)
print(list(zip(number, count)))

number = np.unique(rd)
print('unique한 값은', number)   # default는 return_counts=False

print()
cprint('8) concatenate')
na1 = np.random.randint(10, size=(2,3))
na2 = np.random.randint(10, size=(3,2))
na3 = np.random.randint(10, size=(3,3))
print(na1)
print(na2)
print(na3)
print('8-1) 세로 결합')
c_con = np.concatenate((na1, na3))
print(c_con)
print('8-2) 가로 결합')
r_con = np.concatenate((na2, na3), axis=1)
print(r_con)

print()
cprint('9) split')
r = np.arange(11,20)
print(r)
array1 = np.split(r, [5])   # 인덱스 5는 새 그룹의 시작점
print(array1)
array2 = np.split(r, [2, 4, 6, 8])
print(array2)
print(list(array2[2]))

print()
cprint('10) sort')
r1 = np.random.randint(10, size=(3,3))
print(r1)
print('가로 정렬')
r1.sort()
print(r1)
print('세로 정렬')
r1.sort(axis=0)
print(r1)

"""
Quiz 5
1부터 20까지의 랜덤 숫자를 갖는 5 x 5 행렬을 만드시고
최소값과 최대값을 sort를 사용하여 구하시오.
"""
print()
cprint('Quiz 5')
na = np.random.randint(1, 21, size=(5,5))
print(na)
na.sort()
na.sort(axis=0)
print(na)
print('최소값:', na[0][0], '최대값:', na[4][4])

print('\n')
cprint('NUMPY 연산')
print('1) basic')
na = np.array([1,2,3])
print('na :', na)
print('na * 3 =>', na * 3)
nb = np.array([4,5,6])
print('nb :', nb)
print('na * nb =>', na * nb)

print()
print('2) compare')
print('na == 2 =>', na == 2)
print('nb > 4 =>', nb > 4)
print('na*4 > nb =>', na*4 > nb)
print([1,2,3] > [4,5,6])

print()
print('3) filter')
print('na[na==2] =>', na[na==2])
print('nb[nb>4] =>', nb[nb>4])
nf = [True, False, True, False, True]
na3 = np.array([1, 2, 3, 2, 2])
print('na3[nf] =>', na3[nf])

"""
Quiz 6
1부터 20까지의 행렬을 만들고
3의 배수만 남기시오.
"""
print()
cprint('Quiz 6')
na = np.arange(1,21)
print(na)
print(na[na % 3 == 0])

"""
Quiz 7
리스트 2개가 있다.
ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 0, 3, 4, 0]
같은 인덱스에 같은 값이 존재하는 것들만 남기시오.
"""
print()
cprint('Quiz 7')
ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 0, 3, 4, 0]
ar1 = np.array(ls1)
ar2 = np.array(ls2)
ar3 = ar1[ar1 == ar2]
print(ar3)
q7 = list(ar3)
print(q7)

print()
cprint('4) broadcasting')
na = np.array(range(12)).reshape(3, 4)
print('na :\n', na)

# 모든 데이터에 1 더하기
print('na + 1 :\n', na + 1)

# 모든 행에 na1 더하기
na1 = np.array(range(4))
print('na1 :\n', na1)
print('na + na1 :\n', na + na1)

# 모든 열에 na2 더하기
na2 = np.array([[1000], [2000], [3000]])
print('na2 :\n', na2)
print('na + na2 :\n', na + na2)

print()
cprint('5) NUMPY functions')
na = np.random.randint(10, size=(2,3))
print(na)

# min, max, argmin, argmax
print('min, max :', na.min(), na.max())
print('argmin, argmax :', na.argmin(), na.argmax())

# sum
print('sum(na) :', np.sum(na))
print('sum(na, axis=0) :', np.sum(na, axis=0))   # 세로 합계
print('sum(na, axis=0) :', np.sum(na, axis=1))   # 가로 합계

# mean, median, var, std
print('mean(na) :', np.mean(na))
print('median(na) :', np.median(na))
print('var(na) :', np.var(na))
print('std(na) :', np.std(na))

# *** ndarray의 타입 바꾸기
print(); cprint('astype')
na = np.array(['1','2','3'])
nb = na.astype(dtype=int)
nc = na.astype(dtype=float)
nd = nc.astype(dtype='<U3')   # 숫자는 글자 수
print(na)
print(nb)
print(nc)
print(nd)

"""
Quiz 8
1부터 20까지 랜덤숫자를 가지는 5 x 5 행렬(ndarray)를 만드시고
최소값과 최대값은 숫자(min), 숫자(max)로 출력하시오.
"""
# 랜덤 ndarray 만들기
print(); cprint('Quiz 8')
nd = np.random.randint(1, 21, size=(5,5))
print(nd)

# 최소, 최대값 구하기
minv = nd.min()
maxv = nd.max()
print(f'최소값 : {minv}, 최대값 : {maxv}')

# ndaary 타입을 문자열로 바꾸기
nd_r = nd.astype(dtype='<U10')
nd_r = nd_r.reshape(25)   # reshape 하면 nd_r[][] 할 필요 없음
print(nd_r)

# 각 원소를 최소, 최대값과 비교하기
for i in range(len(nd_r)):
    if nd_r[i] == str(minv):
        nd_r[i] = nd_r[i] + '(min)'
    if nd_r[i] == str(maxv):
        nd_r[i] = nd_r[i] + '(max)'

# 출력하기
print(nd_r)
Q8 = nd_r.reshape(nd.shape)
print(Q8)