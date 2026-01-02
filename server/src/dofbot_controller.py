import pyautogui as pag

from models.dofbot import DofbotControl
from models.config import Config


class DofBotController:
    def __init__(self):
        self.servo1 = 90
        self.servo2 = 90
        self.servo3 = 90
        self.servo4 = 90
        self.servo5 = 90
        self.servo6 = 180

    def is_valid_coordinate(self, coordinate: list) -> bool:
        """
        座標が有効か（0より大きい値が設定されているか）チェックする
        """
        return coordinate[0] > 0 and coordinate[1] > 0

    def set_newtral_position(self, config: Config):
        """
        Sets the DOFBOT to a neutral position.
        """
        if self.is_valid_coordinate(config.dofbot_app_servo1_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo1_scroll_coodinate[0], config.dofbot_app_servo1_scroll_coodinate[1])
            pag.scroll(90-self.servo1)
            self.servo1 = 90
        else:
            print("Warning: Servo1 scroll coordinate is not set. Skipping servo1 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo2_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo2_scroll_coodinate[0], config.dofbot_app_servo2_scroll_coodinate[1])
            pag.scroll(90-self.servo2)
            self.servo2 = 90
        else:
            print("Warning: Servo2 scroll coordinate is not set. Skipping servo2 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo3_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo3_scroll_coodinate[0], config.dofbot_app_servo3_scroll_coodinate[1])
            pag.scroll(90-self.servo3)
            self.servo3 = 90
        else:
            print("Warning: Servo3 scroll coordinate is not set. Skipping servo3 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo4_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo4_scroll_coodinate[0], config.dofbot_app_servo4_scroll_coodinate[1])
            pag.scroll(90-self.servo4)
            self.servo4 = 90
        else:
            print("Warning: Servo4 scroll coordinate is not set. Skipping servo4 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo5_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo5_scroll_coodinate[0], config.dofbot_app_servo5_scroll_coodinate[1])
            pag.scroll(90-self.servo5)
            self.servo5 = 90
        else:
            print("Warning: Servo5 scroll coordinate is not set. Skipping servo5 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo6_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo6_scroll_coodinate[0], config.dofbot_app_servo6_scroll_coodinate[1])
            pag.scroll(180-self.servo6)
            self.servo6 = 180
        else:
            print("Warning: Servo6 scroll coordinate is not set. Skipping servo6 control.")

    def control_dofbot(self, dofbot: DofbotControl, config: Config) -> None:
        """
        Controls the DOFBOT by sending commands to the robot.
        """
        if dofbot.servo1 < config.min_servo1 or dofbot.servo1 > config.max_servo1:
            print(f"servo1 must be between {config.min_servo1} and {config.max_servo1}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo1_scroll_coodinate):
            print("Warning: Servo1 scroll coordinate is not set. Skipping servo1 control.")
        else:
            pag.moveTo(config.dofbot_app_servo1_scroll_coodinate[0], config.dofbot_app_servo1_scroll_coodinate[1])
            pag.scroll(dofbot.servo1 - self.servo1)
            self.servo1 = dofbot.servo1
        pag.sleep(0.1)
        if dofbot.servo2 < config.min_servo2 or dofbot.servo2 > config.max_servo2:
            print(f"servo2 must be between {config.min_servo2} and {config.max_servo2}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo2_scroll_coodinate):
            print("Warning: Servo2 scroll coordinate is not set. Skipping servo2 control.")
        else:
            pag.moveTo(config.dofbot_app_servo2_scroll_coodinate[0], config.dofbot_app_servo2_scroll_coodinate[1])
            pag.scroll(dofbot.servo2 - self.servo2)
            self.servo2 = dofbot.servo2
        pag.sleep(0.1)
        if dofbot.servo3 < config.min_servo3 or dofbot.servo3 > config.max_servo3:
            print(f"servo3 must be between {config.min_servo3} and {config.max_servo3}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo3_scroll_coodinate):
            print("Warning: Servo3 scroll coordinate is not set. Skipping servo3 control.")
        else:
            pag.moveTo(config.dofbot_app_servo3_scroll_coodinate[0], config.dofbot_app_servo3_scroll_coodinate[1])
            pag.scroll(dofbot.servo3 - self.servo3)
            self.servo3 = dofbot.servo3
        pag.sleep(0.1)
        if dofbot.servo4 < config.min_servo4 or dofbot.servo4 > config.max_servo4:
            print(f"servo4 must be between {config.min_servo4} and {config.max_servo4}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo4_scroll_coodinate):
            print("Warning: Servo4 scroll coordinate is not set. Skipping servo4 control.")
        else:
            pag.moveTo(config.dofbot_app_servo4_scroll_coodinate[0], config.dofbot_app_servo4_scroll_coodinate[1])
            pag.scroll(dofbot.servo4 - self.servo4)
            self.servo4 = dofbot.servo4
        pag.sleep(0.1)
        if dofbot.servo5 < config.min_servo5 or dofbot.servo5 > config.max_servo5:
            print(f"servo5 must be between {config.min_servo5} and {config.max_servo5}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo5_scroll_coodinate):
            print("Warning: Servo5 scroll coordinate is not set. Skipping servo5 control.")
        else:
            pag.moveTo(config.dofbot_app_servo5_scroll_coodinate[0], config.dofbot_app_servo5_scroll_coodinate[1])
            pag.scroll(dofbot.servo5 - self.servo5)
            self.servo5 = dofbot.servo5
        pag.sleep(0.1)
        if dofbot.servo6 < config.min_servo6 or dofbot.servo6 > config.max_servo6:
            print(f"servo6 must be between {config.min_servo6} and {config.max_servo6}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo6_scroll_coodinate):
            print("Warning: Servo6 scroll coordinate is not set. Skipping servo6 control.")
        else:
            pag.moveTo(config.dofbot_app_servo6_scroll_coodinate[0], config.dofbot_app_servo6_scroll_coodinate[1])
            pag.scroll(dofbot.servo6 - self.servo6)
            self.servo6 = dofbot.servo6
