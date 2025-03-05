import pytest  
from rowboat.boat import Oar, RowBoat  

@pytest.fixture  
def boat():  
    return RowBoat(Oar(2.0), Oar(2.0))  

def test_forward_movement(boat):  
    boat.oar_left.angle = 90  
    boat.oar_right.angle = 90  
    boat.update_movement()  
    assert boat.speed > 0, "Лодка не движется вперед"  

def test_left_turn(boat):  
    boat.oar_left.angle = 0  
    boat.oar_right.angle = 90  
    initial_dir = boat.direction  
    boat.update_movement()  
    assert boat.direction < initial_dir, "Лодка не поворачивает влево"  

def test_stop(boat):  
    boat.oar_left.angle = 0  
    boat.oar_right.angle = 0  
    boat.update_movement()  
    assert boat.speed == 0, "Лодка не останавливается"  
