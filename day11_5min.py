"""
    Day11 5min Challenge
    2022. 8. 9
"""
"""
    1. 문자열을 2개 입력받는다(s1, s2).
    2. 공통으로 존재하는 문자를 찾는다.(set)
    3. "첫 번째 문자열의 길이 : ***, 두 번째 문자열의 길이 : ***"
       "공통으로 존재하는 문자 개수 : ***"를 출력한다.
    4. 첫 번째 문자열과 두 번째 문자열을 출력하되
       공통인 문자만 색을 입혀 출력한다.
"""
s1 = input("첫 번째 문자열을 입력하세요 : ")
s2 = input("두 번째 문자열을 입력하세요 : ")

# 글자 쪼개기 : 방법1   또는 바로 set(s1) => 중복되는 글자는 무시됨
s1_lst = []
s2_lst = []
for c in s1:
    s1_lst.append(c)
for c in s2:
    s2_lst.append(c)
print(s1_lst)
print(s2_lst)

# set으로 변환
s1_set = set(s1_lst)
s2_set = set(s2_lst)
res_set = s1_set.intersection(s2_set)
res_lst = list(res_set)
if ' ' in res_lst:
    res_lst.remove(' ')

print("첫 번째 문자열의 길이 : {}, 두 번째 문자열의 길이 : {}".format(len(s1), len(s2)))
print("공통으로 존재하는 문자 개수 : {}".format(len(res_lst)))

for c in s1:
    if c in res_lst:
        print(RED + c + END, end='')
    else:
        print(c, end='')
print()
for c in s2:
    if c in res_lst:
        print(GREEN + c + END, end='')
    else:
        print(c, end='')