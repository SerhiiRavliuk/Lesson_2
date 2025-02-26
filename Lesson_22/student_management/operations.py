from database import Session
from models import Student, Course

session = Session()


def add_student(name, course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        course = Course(title=course_title)
        session.add(course)

    student = Student(name=name)
    student.courses.append(course)

    session.add(student)
    session.commit()


def get_students_by_course(course_title):
    course = session.query(Course).filter_by(title=course_title).first()
    if course:
        return [student.name for student in course.students]
    return []


def get_courses_by_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        return [course.title for course in student.courses]
    return []


def update_student(student_name, new_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        student.name = new_name
        session.commit()


def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        session.delete(student)
        session.commit()

