class Oar:  
    def __init__(self, length: float):  
        self.length = length  
        self.angle = 0  # Угол весла относительно лодки (0-360°)  

    def row(self, angle: int) -> float:  
        """Возвращает силу гребка в зависимости от угла."""  
        self.angle = angle  
        return self.length * abs(90 - angle) / 90  # Упрощенная модель  
