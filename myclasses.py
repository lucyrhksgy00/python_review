class House:
    """My House Class : Useless"""   # DocString (클래스 설명문)
    house_count = 0   # 클래스 변수 (모든 인스턴스가 공유하는 변수)

    def __init__(self, name="My Palace"):   # 새로운 인스턴스가 만들어질 때 무조건 호출되는 함수
        print("Instance OK")
        self.name = name   # 인스턴스 변수
        House.house_count += 1

    def welcome(self):   # House 클래스의 새로운 메서드
        print("Welcome to my house")

    def data_process(self, data):   # House 클래스의 새로운 메서드
        print(type(data))

class Villa(House):   # House 클래스 전체를 인수
    pass

class Apart:
    def __init__(self):
        print("새로운 아파트가 생성되었습니다.")
        self.room = 3
        self.furniture = []

    def setRoom(self, i):
        self.room = i

    def getRoom(self):
        return self.room

    def addFurniture(self, str):
        # self.furniture에 str 추가
        self.furniture.append(str)

    def showFurniture(self):
        print(self.furniture)

class MyException(Exception):
    # log를 기록한다.
    # 예외 시스템으로 전송한다.
    pass