from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def calculation_perimetr(self):
        ...

    @abstractmethod
    def calculation_square(self):
        ...