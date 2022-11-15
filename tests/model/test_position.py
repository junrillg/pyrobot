import pytest

from pyrobot.model.position import Direction


@pytest.mark.parametrize(
    "current_facing, want",
    [
        [Direction.EAST, Direction.NORTH],
        [Direction.NORTH, Direction.WEST],
        [Direction.WEST, Direction.SOUTH],
        [Direction.SOUTH, Direction.EAST],
    ],
)
def test_to_left(current_facing: Direction, want: Direction):
    got = current_facing.get_left()

    assert got == want


@pytest.mark.parametrize(
    "current_facing, want",
    [
        [Direction.EAST, Direction.SOUTH],
        [Direction.SOUTH, Direction.WEST],
        [Direction.WEST, Direction.NORTH],
        [Direction.NORTH, Direction.EAST],
    ],
)
def test_to_right(current_facing: Direction, want: Direction):
    got = current_facing.get_right()

    assert got == want
