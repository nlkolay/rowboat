class Oar:
    def __init__(self, length: float, material: str):
        self.length = length  # Длина весла в метрах
        self.material = material  # Материал изготовления
        self.angle = 0  # Угол погружения 0-90°

    def set_angle(self, degrees: int):
        if 0 <= degrees <= 90:
            self.angle = degrees
        else:
            raise ValueError("Недопустимый угол весла")

class Rowboat:
    def __init__(self, oars: list[Oar], max_riders: int):
        self.oars = oars
        self.max_riders = max_riders
        self._speed = 0.0  # Текущая скорость в узлах
        self._direction = 0.0  # Направление в градусах (0-359)
        
    @property
    def speed(self):
        return self._speed
        
    def row(self, power: float, riders: int):
        if riders < 1 or riders > self.max_riders:
            raise ValueError("Недопустимое количество гребцов")
        
        # Расчет скорости: базовая формула V = P * n / (1 + k*n)
        # где P - мощность гребка, n - количество гребцов
        base_speed = power * riders / (1 + 0.1 * riders)
        self._speed = min(base_speed, 5.0)  # Максимум 5 узлов

    def steer(self, degrees: float):
        self._direction = (self._direction + degrees) % 360
        
    def stop(self):
        self._speed = 0.0
        for oar in self.oars:
            oar.set_angle(0)

    def get_status(self) -> dict:
        return {
            'speed': round(self._speed, 2),
            'direction': round(self._direction, 2),
            'oars_angles': [oar.angle for oar in self.oars]
        }
