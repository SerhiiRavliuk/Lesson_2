class Romb:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a
    @property
    def side_a(self) -> float:
        return self._side_a
    @side_a.setter
    def side_a(self, value: float):
        if value <= 0:
            raise ValueError("Side length must be greater than 0.")
        self._side_a = value
    @property
    def angle_a(self) -> float:
        return self._angle_a
    @angle_a.setter
    def angle_a(self, value: float):
        if value <= 0 or value >= 180:
            raise ValueError("Angle must be between 0 and 180 degrees.")
        self._angle_a = value
        self._angle_b = 180 - value
    @property
    def angle_b(self) -> float:
        return 180 - self._angle_a

    def __str__(self):
        return (f"Side A: {self.side_a}\n"
                f"Angle A: {self.angle_a}\n"
                f"Angle B: {self.angle_b}")


