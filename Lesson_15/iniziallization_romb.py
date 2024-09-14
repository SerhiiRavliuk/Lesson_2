from Lesson_15.romb import Romb

romb = Romb(5, 50)
print(romb)

try:
    romb.side_a = -10
except ValueError as e:
    print(e)

try:
    romb.angle_a = 190
except ValueError as e:
    print(e)

romb.angle_a = 60
print(romb)