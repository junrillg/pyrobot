from copy import deepcopy
import hypothesis.strategies as st

from hypothesis import given
from pyrobot.model.position import DIRECTIONS, Direction, Position
from pyrobot.model.robot import Robot

# NOTE: The actual logic of how turning works are tested as part of
# `test_position.py`. These tests only verify when turning the robot maintains
# its location i.e. (x, y) coordinates.


@given(st.integers(), st.integers(), st.sampled_from(DIRECTIONS))
def test_turn_left__only_changes_facing_direction(x: int, y: int, direction: Direction):
    robot = Robot()
    original_position = Position(x, y, direction)
    robot.position = deepcopy(original_position)

    robot.turn_left()

    assert robot.position.x == original_position.x
    assert robot.position.y == original_position.y
    assert robot.position.facing != original_position.facing


@given(st.integers(), st.integers(), st.sampled_from(DIRECTIONS))
def test_turn_right__only_changes_facing_direction(x: int, y: int, direction: Direction):
    robot = Robot()
    original_position = Position(x, y, direction)
    robot.position = deepcopy(original_position)

    robot.turn_right()

    assert robot.position.x == original_position.x
    assert robot.position.y == original_position.y
    assert robot.position.facing != original_position.facing
