from Lesson_16.homework_part_2.figure import Figure
from Lesson_16.homework_part_2.rectangle import Rectangle
from Lesson_16.homework_part_2.square import Square
from Lesson_16.homework_part_2.triangle import Triangle

square_f : Square = Square(4)
rectangle: Rectangle = Rectangle(10,5)
triangle : Triangle = Triangle (5,6,7,3)

figures_list : list[Figure] = [square_f,rectangle,triangle]

list_tuple_perimetr_and_square : list[tuple[int, object]] = [(figure.calculation_perimetr(),figure.calculation_square()) for figure in figures_list]

for item in list_tuple_perimetr_and_square:
    print(item[0],item[1])