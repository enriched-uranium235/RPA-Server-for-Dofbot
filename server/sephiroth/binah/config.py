from pydantic import BaseModel


class Config(BaseModel):
    min_servo1: int = 0
    max_servo1: int = 180
    min_servo2: int = 0
    max_servo2: int = 180
    min_servo3: int = 0
    max_servo3: int = 180
    min_servo4: int = 0
    max_servo4: int = 180
    min_servo5: int = 0
    max_servo5: int = 180
    min_servo6: int = 0
    max_servo6: int = 180
    dofbot_ip: str = "127.0.0.1"
    dofbot_port: int = 6000
    dofbot_app_connect_button_coodinate: tuple[int, int] = (0, 0)
    dofbot_check_network_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_ip_input_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_port_input_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_connect_submit_button_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_use_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo1_scroll_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo2_scroll_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo3_scroll_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo4_scroll_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo5_scroll_coodinate: tuple[int, int] = (0, 0)
    dofbot_app_servo6_scroll_coodinate: tuple[int, int] = (0, 0)
