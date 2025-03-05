class RowBoat:  
    def __init__(self, oar_left: Oar, oar_right: Oar):  
        self.oar_left = oar_left  
        self.oar_right = oar_right  
        self.speed = 0.0  # м/с  
        self.direction = 0.0  # Угол направления (0-360°)  

    def update_movement(self):  
        """Обновляет скорость и направление на основе гребков."""  
        force_left = self.oar_left.row(self.oar_left.angle)  
        force_right = self.oar_right.row(self.oar_right.angle)  
        self.speed = (force_left + force_right) / 2  
        self.direction += (force_right - force_left) * 0.1  
