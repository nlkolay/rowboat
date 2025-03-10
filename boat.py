from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Environment:
    """Класс для хранения параметров окружающей среды"""
    wind_speed: float  # Скорость ветра в м/с (0-20)
    wind_direction: float  # Направление ветра в градусах (0-359)
    current_speed: float  # Скорость течения в м/с (0-5)
    current_direction: float  # Направление течения в градусах (0-359)

class Oar:
    """Класс весла с управлением углом погружения"""
    def __init__(self, length: float, material: str):
        """
        Инициализация весла
        :param length: длина в метрах (1.5-3.0)
        :param material: материал изготовления
        """
        self.length = length
        self.material = material
        self.angle = 0  # Угол погружения (0-90°)

    def set_angle(self, degrees: int):
        """
        Установка угла погружения весла
        :param degrees: угол в градусах (0-90)
        """
        if 0 <= degrees <= 90:
            self.angle = degrees
        else:
            raise ValueError("Угол весла должен быть между 0 и 90 градусами")

class Rowboat:
    """Класс вёсельной лодки с учетом окружающей среды"""
    MAX_SPEED = 5.0  # Максимальная скорость в узлах
    
    def __init__(self, oars: List[Oar], max_riders: int):
        """
        Инициализация лодки
        :param oars: список весел
        :param max_riders: максимальное количество гребцов
        """
        self.oars = oars
        self.max_riders = max_riders
        self._speed = 0.0  # Текущая скорость в узлах
        self._direction = 0.0  # Направление движения (0-359°)
        self.environment = Environment(0.0, 0.0, 0.0, 0.0)  # Окружающая среда

    def set_environment(self, env: Environment):
        """Установка параметров окружающей среды"""
        self.environment = env

    def _calculate_environmental_impact(self) -> Tuple[float, float]:
        """
        Расчет влияния окружающей среды на движение лодки
        Возвращает кортеж (влияние на скорость, коррекция направления)
        """
        # Влияние ветра
        wind_factor = 0.2  # Коэффициент влияния ветра
        wind_impact = self.environment.wind_speed * wind_factor
        wind_angle_diff = (self._direction - self.environment.wind_direction) % 360
        
        # Влияние течения
        current_factor = 1.0  # Коэффициент влияния течения
        current_impact = self.environment.current_speed * current_factor
        current_angle_diff = (self._direction - self.environment.current_direction) % 360
        
        # Суммарное влияние на скорость
        total_speed_impact = (
            wind_impact * (1 - abs(wind_angle_diff - 180)/180) +
            current_impact * (1 - abs(current_angle_diff - 180)/180)
        )
        
        # Коррекция направления
        direction_shift = (
            (wind_angle_diff * wind_impact + 
             current_angle_diff * current_impact) / 
            (wind_impact + current_impact + 1e-9)
        ) * 0.1  # Коэффициент сглаживания
        
        return total_speed_impact, direction_shift

    def row(self, power: float, riders: int):
        """
        Гребля с заданной мощностью и количеством гребцов
        :param power: мощность гребка (0.0-1.0)
        :param riders: количество гребцов (1-max_riders)
        """
        if riders < 1 or riders > self.max_riders:
            raise ValueError(f"Количество гребцов должно быть от 1 до {self.max_riders}")
            
        if power < 0 or power > 1:
            raise ValueError("Мощность гребка должна быть между 0.0 и 1.0")
            
        # Базовый расчет скорости
        base_speed = power * riders / (1 + 0.1 * riders)
        
        # Учет влияния окружения
        env_impact, dir_shift = self._calculate_environmental_impact()
        
        # Обновление состояния
        self._speed = min(base_speed + env_impact, self.MAX_SPEED)
        self._direction = (self._direction + dir_shift) % 360

    def steer(self, degrees: float):
        """Изменение направления лодки"""
        self._direction = (self._direction + degrees) % 360

    def stop(self):
        """Остановка лодки"""

        self._speed = 0.0
        for oar in self.oars:
            oar.set_angle(0)

    def get_status(self) -> dict:
        """Получение текущего состояния лодки"""
        return {
            'speed': round(self._speed, 2),
            'direction': round(self._direction, 2),
            'oars_angles': [oar.angle for oar in self.oars],
            'environment': {
                'wind_speed': self.environment.wind_speed,
                'wind_direction': self.environment.wind_direction,
                'current_speed': self.environment.current_speed,
                'current_direction': self.environment.current_direction
            }
        }
