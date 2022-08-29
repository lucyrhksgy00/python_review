import myclasses as mc
from Color import *

cprint('Class Exercise')
# docstring Test
print(mc.House.__doc__)

print("init class var :", mc.House.house_count)
myhouse = mc.House()
print(myhouse.name)
print("made 1 class var :", myhouse.house_count)
print("class var(no instance) :", mc.House.house_count)
yourhouse = mc.House("Your House")
yourhouse.welcome()
print("yourhouse.house_count :", yourhouse.house_count)
print("myhouse.house_count :", myhouse.house_count)
myhouse.house_count = 500   # house_count가 self.house_count로 변경
print("yourhouse.house_count :", yourhouse.house_count)
print("myhouse.house_count :", myhouse.house_count)
hishouse = mc.House()
print("yourhouse.house_count :", yourhouse.house_count)
print("myhouse.house_count :", myhouse.house_count)
print("hishouse.house_count :", hishouse.house_count)
# yourhouse = 100
# print(yourhouse.name)   # 100으로 할당한 순간 객체는 그냥 변수가 됨

# instance variable
print(hishouse.__dict__)
print(myhouse.__dict__)
hishouse.room = 100
print(hishouse.room)
print(hishouse.__dict__)

# special test
hishouse.data_process("pppp")
hishouse.data_process(1000)
hishouse.data_process([1,2,3,4])

myvill = mc.Villa()

# class test
apart1 = mc.Apart()
apart2 = mc.Apart()
print('apart1의 방 개수 :', apart1.getRoom())
apart1.setRoom(99)
print('리모델링 후 apart1의 방 개수 :', apart1.getRoom())
apart1.addFurniture("Sofa")
apart1.addFurniture("TV")
apart1.addFurniture("Bed")
apart1.showFurniture()
apart2.showFurniture()

list_a = [apart1, apart2]
print(type(list_a[0]))

print()
cprint('Exception')
try:
    a = int(input('나누어지는 수를 입력하세요 : '))
    if a >= 10000:
        raise Exception("너 지금 나랑 장난하냐")
    b = int(input('나눌 수를 입력하세요 : '))
    c = a / b
    print('{} / {} = {}'.format(a, b, c))
except ZeroDivisionError as e:
    print('0으로 나눌려고 하냐??')
    print(e)
except ValueError as e:
    print('정수만 된다니까 이게 확')
    print(e)
except Exception as e:
    print('오류났어')
    print(e)
else:
    print('오류 안나고 정상 수행되었습니다 짝짝짝!!!')
finally:
    print('오류나든 안나든 니가 특별히 잘한 것은 없다')

def alwaysAngry():
    raise mc.MyException("호출하기만 해봐라")

# cf) Java
#     함수의 선언부에 throws Exception

try:
    alwaysAngry()
except Exception as e:
    print('예외가 발생하였습니다.....')
    print(e)