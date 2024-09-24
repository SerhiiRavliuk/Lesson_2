from Lesson_16.homework_part_2.figure import Figure

class Rectangle(Figure):
    __rectangle_side_a: int
    __rectangle_side_b: int

    def __init__(self, rectangle_side_a: int, rectangle_side_b: int):
        self.__rectangle_side_a = rectangle_side_a
        self.__rectangle_side_b = rectangle_side_b

    def calculation_perimetr(self):
        return (self.__rectangle_side_a * 2) + (self.__rectangle_side_b * 2)

    def calculation_square(self):
        return self.__rectangle_side_a * self.__rectangle_side_b