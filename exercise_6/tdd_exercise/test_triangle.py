from pytest import raises
from triangle import Triangle


def test_valid_init():
    triangle = Triangle(base=5, height=2)
    assert triangle.base == 5 and triangle.height == 2


def test_negative_base_fails():
    with raises(ValueError):
        Triangle(base=-1, height=2)


def test_negative_height_fails():
    with raises(ValueError):
        Triangle(base=1, height=-2)


def test_invalid_type_str_init_fails():
    with raises(ValueError):
        Triangle(base="1", height=1)


def test_invalid_type_bool_init_fails():
    with raises(ValueError):
        Triangle(base=1, height=True)


def test_zero_base_fail():
    with raises(ValueError):
        Triangle(base=0, height=1)
