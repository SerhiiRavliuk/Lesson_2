from models import Base
from database import engine
from operations import add_student, get_students_by_course, update_student, delete_student

Base.metadata.create_all(engine)

add_student("Петренко Петро", "Математика")
add_student("Шевченко Тарас", "Фізика")
add_student("Сидоренко Марія", "Хімія")
add_student("Коваленко Олександр", "Біологія")
add_student("Гончаренко Олена", "Інформатика")

students_in_math = get_students_by_course("Математика")
print("Студенти на курсі Математика:", students_in_math)

update_student("Петренко Петро", "Петренко Петро Іванович")

delete_student("Петренко Петро Іванович")
