import pyautogui as pag

from yesod.dofbot import DofbotModel
from binah.config import Config


CURRENT_SERVO1 = 90
CURRENT_SERVO2 = 90
CURRENT_SERVO3 = 90
CURRENT_SERVO4 = 90
CURRENT_SERVO5 = 90
CURRENT_SERVO6 = 180


class DofBotController:
    def is_valid_coordinate(self, coordinate: list) -> bool:
        """
        座標が有効か（0より大きい値が設定されているか）チェックする
        """
        return coordinate[0] > 0 and coordinate[1] > 0

    def set_newtral_position(self, config: Config):
        """
        Sets the DOFBOT to a neutral position.
        """
        global CURRENT_SERVO1, CURRENT_SERVO2, CURRENT_SERVO3, CURRENT_SERVO4, CURRENT_SERVO5, CURRENT_SERVO6
        if self.is_valid_coordinate(config.dofbot_app_servo1_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo1_scroll_coodinate[0], config.dofbot_app_servo1_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO1-90) * 125)
            CURRENT_SERVO1 = 90
        else:
            print("Warning: Servo1 scroll coordinate is not set. Skipping servo1 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo2_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo2_scroll_coodinate[0], config.dofbot_app_servo2_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO2-90) * 125)
            CURRENT_SERVO2 = 90
        else:
            print("Warning: Servo2 scroll coordinate is not set. Skipping servo2 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo3_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo3_scroll_coodinate[0], config.dofbot_app_servo3_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO3-90) * 125)
            CURRENT_SERVO3 = 90
        else:
            print("Warning: Servo3 scroll coordinate is not set. Skipping servo3 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo4_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo4_scroll_coodinate[0], config.dofbot_app_servo4_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO4-90) * 125)
            CURRENT_SERVO4 = 90
        else:
            print("Warning: Servo4 scroll coordinate is not set. Skipping servo4 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo5_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo5_scroll_coodinate[0], config.dofbot_app_servo5_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO5-90) * 125)
            CURRENT_SERVO5 = 90
        else:
            print("Warning: Servo5 scroll coordinate is not set. Skipping servo5 control.")
        pag.sleep(0.1)

        if self.is_valid_coordinate(config.dofbot_app_servo6_scroll_coodinate):
            pag.moveTo(config.dofbot_app_servo6_scroll_coodinate[0], config.dofbot_app_servo6_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO6-180) * 125)
            CURRENT_SERVO6 = 180
        else:
            print("Warning: Servo6 scroll coordinate is not set. Skipping servo6 control.")

    def control_dofbot(self, dofbot: DofbotModel, config: Config) -> None:
        """
        Controls the DOFBOT by sending commands to the robot.
        """
        global CURRENT_SERVO1, CURRENT_SERVO2, CURRENT_SERVO3, CURRENT_SERVO4, CURRENT_SERVO5, CURRENT_SERVO6
        if dofbot.servo1 < config.min_servo1 or dofbot.servo1 > config.max_servo1:
            print(f"servo1 must be between {config.min_servo1} and {config.max_servo1}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo1_scroll_coodinate):
            print("Warning: Servo1 scroll coordinate is not set. Skipping servo1 control.")
        else:
            pag.moveTo(config.dofbot_app_servo1_scroll_coodinate[0], config.dofbot_app_servo1_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO1 - dofbot.servo1) * 125)
            CURRENT_SERVO1 = dofbot.servo1
        pag.sleep(0.1)
        if dofbot.servo2 < config.min_servo2 or dofbot.servo2 > config.max_servo2:
            print(f"servo2 must be between {config.min_servo2} and {config.max_servo2}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo2_scroll_coodinate):
            print("Warning: Servo2 scroll coordinate is not set. Skipping servo2 control.")
        else:
            pag.moveTo(config.dofbot_app_servo2_scroll_coodinate[0], config.dofbot_app_servo2_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO2 - dofbot.servo2) * 125)
            CURRENT_SERVO2 = dofbot.servo2
        pag.sleep(0.1)
        if dofbot.servo3 < config.min_servo3 or dofbot.servo3 > config.max_servo3:
            print(f"servo3 must be between {config.min_servo3} and {config.max_servo3}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo3_scroll_coodinate):
            print("Warning: Servo3 scroll coordinate is not set. Skipping servo3 control.")
        else:
            pag.moveTo(config.dofbot_app_servo3_scroll_coodinate[0], config.dofbot_app_servo3_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO3 - dofbot.servo3) * 125)
            CURRENT_SERVO3 = dofbot.servo3
        pag.sleep(0.1)
        if dofbot.servo4 < config.min_servo4 or dofbot.servo4 > config.max_servo4:
            print(f"servo4 must be between {config.min_servo4} and {config.max_servo4}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo4_scroll_coodinate):
            print("Warning: Servo4 scroll coordinate is not set. Skipping servo4 control.")
        else:
            pag.moveTo(config.dofbot_app_servo4_scroll_coodinate[0], config.dofbot_app_servo4_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO4 - dofbot.servo4) * 125)
            CURRENT_SERVO4 = dofbot.servo4
        pag.sleep(0.1)
        if dofbot.servo5 < config.min_servo5 or dofbot.servo5 > config.max_servo5:
            print(f"servo5 must be between {config.min_servo5} and {config.max_servo5}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo5_scroll_coodinate):
            print("Warning: Servo5 scroll coordinate is not set. Skipping servo5 control.")
        else:
            pag.moveTo(config.dofbot_app_servo5_scroll_coodinate[0], config.dofbot_app_servo5_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO5 - dofbot.servo5) * 125)
            CURRENT_SERVO5 = dofbot.servo5
        pag.sleep(0.1)
        if dofbot.servo6 < config.min_servo6 or dofbot.servo6 > config.max_servo6:
            print(f"servo6 must be between {config.min_servo6} and {config.max_servo6}")
        elif not self.is_valid_coordinate(config.dofbot_app_servo6_scroll_coodinate):
            print("Warning: Servo6 scroll coordinate is not set. Skipping servo6 control.")
        else:
            pag.moveTo(config.dofbot_app_servo6_scroll_coodinate[0], config.dofbot_app_servo6_scroll_coodinate[1])
            pag.sleep(0.1)
            pag.scroll((CURRENT_SERVO6 - dofbot.servo6) * 125)
            CURRENT_SERVO6 = dofbot.servo6