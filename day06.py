from Color import *

cprint("Built-in Functions")

def printExp(str):
    print(str + ' => ', eval(str))

# printExp Test
printExp("100 * 4000")

print('1. eval')
printExp("eval('1+1')")

print('2. format')
printExp('format(34567, ",")')   # ''안에 "" 넣는거 복습!
printExp('format(34567, "_")')

printExp('format("꽥꽥꽥꽥꽥", "비<20")')   # 20자리로 좌측정렬하고 빈 부분은 '비'로 채움
printExp('format(1234, "0>15")')   # 15자리로 우측정렬하고 빈 부분은 0으로 채움
printExp('format(1234, "0>+15")')   # 부호 한자리 넣어줌
printExp('format(1234, "<10")')   # 채울 문자를 생략하면 공백

print('3. str, int, float')
print('str() : ' + str(47) + '명이 출석 중')
print('float(10) :', float(10))
print('int(10.9) :', int(10.9))

print('4. divmod()')
printExp('divmod(10,3)')
a = divmod(10, 3)
print(a)
# a[1] = 5   # tuple은 수정 불가
b = list(a)
b[1] = 5
b = tuple(b)
print(b)

print('5. min(), max()')
c = [1, 2, 3, 4, 5]
print(min(c))   # 숫자 1
print(min(1, 2, 3, 4, 5))
print(min("1", "2", "3"))   # 문자 '1'
print(min(c) == min("1"))
# a = min(1, "1")   # 숫자와 문자는 크기 비교 불가

print('6. abs(), pow(), sum()')
printExp('abs(-50.5)')
printExp('pow(10, -1)')
printExp('pow(10, 1.5)')
# printExp('sum(1, 2, 3, 4, 5)')
printExp('sum([1, 2, 3, 4, 5], start = 1000)')

a = max([10, 1000, 10000], [100, 100, 100])
print(a)   # 첫번째 값들만 비교; 같으면 다음 값 비교
b = max(["a", "a1", "A", "9"])
print(b)

print('7. round()')
printExp('round(234.2, -3)')
printExp('round(2.675, 1)')
printExp('round(2.975, 2)')
printExp('round(2.685, 2)')
printExp('round(2.675, 2)')   # 소수 셋째자리 정도부터는 5는 올림일 수도 내림일 수도 있음
printExp('round(2.665, 2)')
printExp('round(2.655, 2)')

print('8. print()')
print('String1', 'String2', sep = "|")

print('9. input()')
# a, b = input('변수를 공백으로 구분해서 입력하세요 :').split(" ")
# print(a, b)

print('10. len()')   # 문자열만 len() 씌울 수 있음!
printExp('len("abcde")')   # 문자의 개수
printExp('len(["abcde"])')

print('11. range()')
printExp('list(range(10))')   # range(10)은 우리에게 인식되는 값이 아니라 list로 눈에 보이게 만들어야 함
printExp('list(range(1, 100, 2))')
printExp('list(range(0, 15, -5))')

print('12. sorted()')
student = ['A학생', 'B학생', '12345']
s1 = sorted(student, reverse = False)
print(s1)
s2 = sorted(student, reverse = True)
print(s2)