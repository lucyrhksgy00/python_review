print('aaaaa')

RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

print(GREEN + '1.print' + END)

#1. 화면에 Hello + 본인이름을 출력하시오.
print('Hello ***')
print('Hello ' + '***')
print('Hello ' + '***', end = '') # 다음 줄로 내려가지 않음
print() # 출력 하지 않고 한 줄 내리고 싶을 때

#2. Mary's cosmetics
print('Mary\'s cosmetics')
print("Mary's cosmetics") # "를 먼저 쓰면 '가 그대로 출력됨
print('aaa"') # '를 먼저 쓰면 "가 문자로 출력됨

#3.
print('신씨가 "도둑이야"라고 소리쳤다.')

#4. a = 'first' b = 'second'일 때 first second
a = 'first'
b = 'second'
print(a, b) # 쉼표로 연결
print(a, b, a, a, a) # 쉼표로 무제한 연결 가능
print(a+b, b, a, a, a) # +와 ,의 차이
print(a, b, sep = '|', end = '!!!!!') # 다음 줄과 사이의 공백 없어짐
print(a, b, sep = '') # space 없애고 싶을 때
print(a, b, sep = '***') # replace space with ***
print(a, b, sep = '|') # 데이터 구분자 (separator)로 사용
print(a, b, sep = '|', end = '!!!!!\n') # !!!!!찍고 다음 줄로 내림

print(RED + '2.input' + END)
print("*" * 40)
# a = input()
# print(a * 10) # a를 10번 반복
# b = input("값을 입력하세요 : ")
# print(b)
# a = input("영어점수와 국사점수를 쉼표로 구분하여 입력해 : ") # 10과 8 모두 a로 들어감
# print(a)

# a, b = input("영어점수와 국사점수를 쉼표로 구분하여 입력해 : ").split(',')
# print('영어점수:', a) # 10 숫자가 아닌 문자로 읽음
# print('국사점수:', b) # 8 숫자가 아닌 문자로 읽음
# print('영어 + 국사점수:', int(a) + int(b)) # a+b를 할 시 문자끼리 더한 걸로 생각해 108로 붙힘

# 영어, 수학, 과학 점수를 입력받아 합계와 평균을 출력하시오.
e, m, s = input("영어, 수학, 과학 점수를 공백으로 구분하여 입력해 : ").split(' ')
e = int(e)
m = int(m)
s = int(s)
tot = e + m + s
avg = round(tot/3, 1) # 소숫점 첫번째자리까지 남기고 반올림
print("귀하의 총점은 무려 " + str(tot) + "점입니다.") # 숫자를 다시 문자로 바꿔줘야 더할 수 있음
print("귀하의 평균은 아쉽게도 " + str(avg) + "점입니다.")