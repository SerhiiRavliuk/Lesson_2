from Lesson_16_2.figure import Figure

class Square(Figure):
    __square_side : int
    def __init__(self,square_side):
        self.__square_side = square_side

    def calculation_perimetr(self):
        return self.__square_side * 4

    def calculation_square(self):
        return self.__square_side ** 2