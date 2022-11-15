import hypothesis.strategies as st
import pytest

from copy import deepcopy
from hypothesis import given
from pyrobot.model.exception import InvalidPositionError
from pyrobot.model.position import DIRECTIONS, Direction, Position
from pyrobot.model.robot import Robot
from pyrobot.model.table import Table


class TABLE_SIZE:
    """The size of the table used for testing"""

    X = 5
    Y = 5


@pytest.fixture(scope="module", autouse=True)
def table() -> Table:
    return Table(5, 5)


@pytest.mark.parametrize(
    "x, y, want",
    [
        [0, 0, True],
        [4, 0, True],
        [0, 4, True],
        [2, 2, True],
        [-1, 0, False],
        [0, -1, False],
        [0, 5, False],
        [5, 0, False],
    ],
)
def test_is_valid_position__returns_expected_result(x, y, want, table):
    position = Position(x, y, ...)

    got = table.is_valid_position(position)

    assert got == want


@given(
    x=st.integers(0, TABLE_SIZE.X - 1),
    y=st.integers(0, TABLE_SIZE.Y - 1),
    direction=st.sampled_from(DIRECTIONS),
)
def test_place__sets_the_correct_position_for_the_robot(table: Table, x: int, y: int, direction: Direction):
    robot = Robot()

    table.place(robot, x, y, direction)

    assert robot.position.x == x
    assert robot.position.y == y
    assert robot.position.facing == direction


def test_place__raises_exception_when_position_is_invalid(table):
    robot = Robot()
    x, y, facing = -1, 3, Direction.SOUTH

    with pytest.raises(InvalidPositionError):
        table.place(robot, x, y, facing)


@pytest.mark.parametrize(
    "current_position, new_position",
    [
        [Position(0, 0, Direction.EAST), Position(1, 0, Direction.EAST)],
        [Position(0, 0, Direction.NORTH), Position(0, 1, Direction.NORTH)],
        [Position(4, 0, Direction.WEST), Position(3, 0, Direction.WEST)],
        [Position(4, 0, Direction.NORTH), Position(4, 1, Direction.NORTH)],
        [Position(0, 4, Direction.EAST), Position(1, 4, Direction.EAST)],
        [Position(0, 4, Direction.SOUTH), Position(0, 3, Direction.SOUTH)],
        [Position(4, 4, Direction.WEST), Position(3, 4, Direction.WEST)],
        [Position(4, 4, Direction.SOUTH), Position(4, 3, Direction.SOUTH)],
    ],
)
def test_move_forward__moves_the_robot_in_its_facing_direction(current_position, new_position, table):
    robot = Robot()
    robot.position = current_position

    table.move_forward(robot)

    assert robot.position == new_position


@pytest.mark.parametrize(
    "current_position",
    [
        Position(0, 0, Direction.WEST),
        Position(0, 0, Direction.SOUTH),
        Position(4, 0, Direction.EAST),
        Position(4, 0, Direction.SOUTH),
        Position(0, 4, Direction.WEST),
        Position(0, 4, Direction.NORTH),
        Position(4, 4, Direction.EAST),
        Position(4, 4, Direction.NORTH),
    ],
)
def test_move_forward__raises_exception_when_the_next_position_is_off_the_table(current_position, table):
    robot = Robot()
    robot.position = deepcopy(current_position)

    with pytest.raises(InvalidPositionError):
        table.move_forward(robot)

    assert robot.position == current_position
