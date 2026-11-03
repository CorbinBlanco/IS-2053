
class Car:
    def __init__(self, __year_model, __make):
        self.__year_model = __year_model
        self.__make = __make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed
