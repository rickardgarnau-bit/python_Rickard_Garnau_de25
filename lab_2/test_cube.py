from pytest import raises
from cube import Cube

def test_valid_init():
    cube = Cube(side=8)
    assert cube.side 8