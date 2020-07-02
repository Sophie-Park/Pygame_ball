# class Unit :
#     def __init__(self):
#         print("Unit 생성자")


# class Flyable :
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__()


# # 드랍쉽
# dropship = FlyableUnit()

# >>>> 결과값 : Unit 생성자 # Flyable 은 상속되지 않음을 알 수 있음.

# # super를 사용할 시에는, 다중상속을 할때 처음 상속받는 것만 상속가능.


class Unit :
    def __init__(self):
        print("Unit 생성자")


class Flyable :
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
        
dropship = FlyableUnit()

# >>> 결과값 : 

# Unit 생성자
# Flyable 생성자

# >> 따라서, 다중 상속을 원하는 경우에는 super 를 사용하는 것이 아닌 상속을 따로따로 해주는 것이 좋음.