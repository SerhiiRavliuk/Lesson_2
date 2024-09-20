from Lesson_16_2.figure import Figure
from typing import override

class Triangle(Figure):
    __triangle_side_a: int
    __triangle_side_b: int
    __triangle_side_c: int
    __heigh : int

    def __init__(self, triangle_side_a, triangle_side_b, triangle_side_c, heigh):
        self.__triangle_side_a = triangle_side_a
        self.__triangle_side_b = triangle_side_b
        self.__triangle_side_c = triangle_side_c
        self.__heigh = heigh

    @override
    def calculation_perimetr(self):
        return self.__triangle_side_a + self.__triangle_side_b + self.__triangle_side_c
    @override
    def calculation_square(self) -> float:
        return 0.5 * self.__triangle_side_a * self.__heigh