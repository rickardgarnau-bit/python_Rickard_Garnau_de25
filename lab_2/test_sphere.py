from pytest import raises
from sphere import Sphere
import math


# Test that a sphere can be initialized with a valid radius
def test_valid_init():
    sphere = Sphere(radius=8)
    assert sphere.radius == 8


# Test that initializing a sphere with a negative radius raises ValueError
def test_negative_radius_fail():
    with raises(ValueError):
        Sphere(radius=-1)


# Test that initializing a sphere with a string raises TypeError
def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Sphere(radius="8")


# Test that initializing a sphere with a boolean raises TypeError
def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Sphere(radius=True)


# Test that setting the radius to a valid number works correctly
def test_set_radius_valid():
    sphere = Sphere(radius=4)
    sphere.radius = 5
    assert sphere.radius == 5


# Test that setting the radius to a negative value raises ValueError
def test_set_radius_invalid_value():
    sphere = Sphere(radius=4)
    with raises(ValueError):
        sphere.radius = -2


# Test that setting the radius to an invalid type raises TypeError
def test_set_radius_invalid_type():
    sphere = Sphere(radius=4)
    with raises(TypeError):
        sphere.radius = "a"


def test_float_radius():
    sphere = Sphere(radius=5.5)
    assert math.isclose(sphere.volume, (4 / 3) * math.pi * 5.5**3)
    assert math.isclose(sphere.surface_area, 4 * math.pi * 5.5**2)


# Test volume method directly
def test_volume_method():
    sphere = Sphere(radius=3)
    assert math.isclose(sphere.volume, (4 / 3) * math.pi * 27)


# Test surface_area method directly
def test_surface_area_method():
    sphere = Sphere(radius=2)
    assert math.isclose(sphere.surface_area, 4 * math.pi * 4)


# Test circumference method
def test_circumference_method():
    sphere = Sphere(radius=1.5)
    assert math.isclose(sphere.circumference, 2 * math.pi * 1.5)


""" sources: https://www.w3resource.com/python-exercises/math/python-math-exercise-6.php
and cube.py as a template"""
