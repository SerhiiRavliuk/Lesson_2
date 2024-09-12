from Lesson_14.student import Student

student_Serhii_Ravliuk = Student('Serhii', 'Ravliuk', 30, 84.5)

print(student_Serhii_Ravliuk)

# Змінюємо середній бал студента
student_Serhii_Ravliuk.change_average_score(90.0)

# Виводимо оновлену інформацію про студента
print(student_Serhii_Ravliuk)

