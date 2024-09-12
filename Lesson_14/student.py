class Student:
    def __init__(self, first_name: str, last_name: str, age: int, average_score: float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def change_average_score(self, new_score: float):
        self.average_score = new_score

    def __str__(self):
        return (f'Student: {self.first_name} {self.last_name}, Age: {self.age}, '
                f'Average Score: {self.average_score}')

