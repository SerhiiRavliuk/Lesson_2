from abc import ABC

class Employee(ABC):

    def __init__(self, name, salary):
        self.name: str = name
        self.salary: int = salary

class Manager(Employee):

    def __init__(self,name:str,salary:int,department:str):
        super().__init__(name,salary)
        self.department = department

class TestEngineer(Employee):
    programming_language : str

class TeamLead(Manager, TestEngineer):

    team_size : int
    
    def __init__(self, name: str, salary: int, department: str, team_size:int):
        super().__init__(name, salary, department)
        self.team_size = team_size

        