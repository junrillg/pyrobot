import re

from pyrobot import controller
from pyrobot.model.exception import InvalidPositionError, RobotHasNotBeenPlacedError
from pyrobot.model.position import Direction


def start_program() -> None:
    controller.start_new_session()

    while True:
        try:
            user_input = input("Please enter a command: ")
            user_input = user_input.strip().upper()
            if user_input == "LEFT":
                controller.turn_left()
            elif user_input == "RIGHT":
                controller.turn_right()
            elif user_input == "MOVE":
                controller.move()
            elif matches := re.match(r"PLACE (?P<x>\d),(?P<y>\d),(?P<facing>\w+)", user_input):
                input_dict = matches.groupdict()

                x = int(input_dict["x"])
                y = int(input_dict["y"])
                facing = Direction[input_dict["facing"]]

                controller.place(x, y, facing)
            elif user_input == "REPORT":
                print(controller.report())
            else:
                print("I didn't understand that! Could you please try again?")
        except (InvalidPositionError, RobotHasNotBeenPlacedError):
            print("Ignored the command since it is an invalid move")
        except KeyboardInterrupt:
            print("\nSee you later")
            return
        except Exception as e:
            print(f"Unknown error: {e}")
