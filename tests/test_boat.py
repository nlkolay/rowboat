import pytest
from rowboat.boat import Rowboat, Oar, Environment

@pytest.fixture
def test_boat():
    oars = [Oar(2.5, "carbon") for _ in range(4)]
    return Rowboat(oars, max_riders=4)

# TC-F-01
def test_initial_state(test_boat):
    status = test_boat.get_status()
    assert status['speed'] == 0.0
    assert status['direction'] == 0.0
    assert status['oars_angles'] == [0, 0, 0, 0]
    assert status['environment']['wind_speed'] == 0.0
    assert status['environment']['current_speed'] == 0.0

# TC-F-02
def test_single_rider(test_boat):
    test_boat.row(power=0.5, riders=1)
    status = test_boat.get_status()
    assert 0.44 < status['speed'] < 0.46
    assert status['direction'] == 0.0

# TC-F-03
def test_max_riders(test_boat):
    test_boat.row(power=1.0, riders=4)
    status = test_boat.get_status()
    assert 2.85 < status['speed'] < 2.87
    assert status['direction'] == 0.0

# TC-F-04
def test_turn_45_degrees(test_boat):
    test_boat.steer(45)
    status = test_boat.get_status()
    assert status['direction'] == 45.0

# TC-I-01
def test_wind_assist(test_boat):
    env = Environment(wind_speed=5.0, wind_direction=0,
                     current_speed=0.0, current_direction=0)
    test_boat.set_environment(env)
    test_boat.row(power=0.5, riders=2)
    status = test_boat.get_status()
    assert 0.82 < status['speed'] < 0.84
    assert -1 < status['direction'] < 1

# TC-I-02
def test_wind_resistance(test_boat):
    env = Environment(wind_speed=5.0, wind_direction=180,
                     current_speed=0.0, current_direction=0)
    test_boat.set_environment(env)
    test_boat.row(power=0.5, riders=2)
    status = test_boat.get_status()
    assert 1.82 < status['speed'] < 1.84
    assert 17 < status['direction'] < 19
