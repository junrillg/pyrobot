from dataclasses import dataclass
from typing import Optional

from pyrobot.model.exception import RobotHasNotBeenPlacedError
from pyrobot.model.position import Position


@dataclass
class Robot:
    position: Optional[Position]

    def __init__(self):
        self.position = None

    def has_been_placed(self) -> bool:
        return self.position is not None

    def turn_left(self) -> None:
        if not self.has_been_placed():
            raise RobotHasNotBeenPlacedError

        self.position.facing = self.position.facing.get_left()

    def turn_right(self) -> None:
        if not self.has_been_placed():
            raise RobotHasNotBeenPlacedError

        self.position.facing = self.position.facing.get_right()

    def report(self) -> str:
        if not self.has_been_placed():
            raise RobotHasNotBeenPlacedError

        return repr(self.position)
