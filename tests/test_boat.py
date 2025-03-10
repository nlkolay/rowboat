import pytest
from boat import Rowboat, Oar

@pytest.fixture
def test_boat():
    oars = [Oar(2.5, "carbon") for _ in range(4)]
    return Rowboat(oars, max_riders=4)

def test_basic_rowing(test_boat):
    test_boat.row(power=1.0, riders=2)
    assert 1.6 < test_boat.speed < 1.9  # Проверка диапазона скорости

def test_emergency_stop(test_boat):
    test_boat.row(1.0, 4)
    test_boat.stop()
    assert test_boat.speed == 0.0
    assert all(oar.angle == 0 for oar in test_boat.oars)

def test_steering(test_boat):
    test_boat.steer(45)
    test_boat.steer(90)
    assert test_boat.get_status()['direction'] == 135.0

def test_invalid_riders(test_boat):
    with pytest.raises(ValueError):
        test_boat.row(1.0, 5)
