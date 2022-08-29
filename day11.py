from Color import *

cprint("String Method")

s1 = 'my name is John'
print(s1)
print("'name' is at", s1.find('name'))   # 3
print("'Name' is at", s1.find('Name'))   # -1

# 'name'이 s1에 있는지 없는지를 bool 타입으로 반환
print("'name' is in s1??", 'name' in s1)

# 대소문자 관계없이 찾고 싶은 경우
print("'Name' is in s1??", 'Name'.lower() in s1.lower())

# 각 단어의 첫 글자만 대문자로
s2 = s1.title()
print("s1.title() :", s2, "why's".title())
s3 = "my name is John. your name is jack".capitalize()
print(s3)

# Quiz
# s3를 가지고 "My name is John. Your name is jack"을 만들어보시오.
ss1, ss2 = s3.split(". ")
print(ss1)
print(ss2)
print(ss1.capitalize() + ". " + ss2.capitalize())

# split 했을 시 몇 개의 결과가 나오는지 모를 때
def capitalize_text(text):
    ss = text.split(". ")   # list 형태로 ss에 split된 모든 text들이 저장됨
    result = ""
    for i in range(0,len(ss)):   # 길이가 len(ss)
        result = result + ss[i].capitalize()
        if i != len(ss)-1:   # 마지막 text가 아니라면 (마지막 text는 이미 마침표가 붙어있음)
            result = result + ". "   # result 끝에 마침표를 넣어라
    return result

stest = "abcee. ddddd. eeeee. fhejwoeijfldkjf. slkjeofih."
stest2 = capitalize_text(stest)
print(stest2)

print()
cprint("lstrip, rstrip, strip")
s4 = '              I am a progamer@@@@@11111111111@@@@@@@@@@@@@@@@@@1111111'
print(s4)
s5 = s4.lstrip(' ')
print(s5)

# 문자열에 있는 문자면 삭제, 문자열에 없는 문자를 만날 때까지
s6 = s5.rstrip('1r@')
print(s6)

print()
cprint("First Class")

class House:
    pass

house1 = House()
house2 = House()
print(house1 == house2)
print(type(house1) == type(house2))
print(type(house1))