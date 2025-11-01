from pytest import raises
from cube import Cube
import math


# Test that a cube can be initialized with a valid side
def test_valid_init():
    cube = Cube(side=8)
    assert cube.side == 8


# Test that initializing a cube with a negative side raises ValueError
def test_negative_side_fail():
    with raises(ValueError):
        Cube(side=-1)


# Test that initializing a cube with a string raises TypeError
def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Cube(side="8")


# Test that initializing a cube with a boolean raises TypeError
def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Cube(side=True)


# Test that setting the side to a valid number works correctly
def test_set_side_valid():
    cube = Cube(side=4)
    cube.side = 5
    assert cube.side == 5


# Test that setting the side to a negative value raises ValueError
def test_set_side_invalid_value():
    cube = Cube(side=4)
    with raises(ValueError):
        cube.side = -2


# Test that setting the side to an invalid type raises TypeError
def test_set_side_invalid_type():
    cube = Cube(side=4)
    with raises(TypeError):
        cube.side = "a"


# Test that float sides work correctly and calculations are accurate
def test_float_side():
    cube = Cube(side=2.5)
    assert math.isclose(cube.volume, 2.5**3)
    assert math.isclose(cube.surface_area, 6 * 2.5**2)


# Test volume method directly
def test_volume_method():
    cube = Cube(side=3)
    assert math.isclose(cube.volume, 27)


# Test surface_area method directly
def test_surface_area_method():
    cube = Cube(side=2)
    assert math.isclose(cube.surface_area, 24)


# Test perimeter method
def test_perimeter_method():
    cube = Cube(side=1.5)
    assert math.isclose(cube.perimeter, 18)


""" sources: http://pythonfiddle.com/python-program-to-write-a-cube-class/
https://github.com/Db-Lau/python_code_along_DE25/tree/main/exercises/tdd_exercise"""
