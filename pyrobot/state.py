from pyrobot.model.robot import Robot
from pyrobot.model.table import Table


class State:
    def __init__(self):
        self.table = Table(5, 5)
        self.robot = Robot()
