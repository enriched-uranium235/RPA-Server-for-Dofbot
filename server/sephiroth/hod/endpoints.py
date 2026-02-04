from fastapi import APIRouter, status, Depends
from netzach.dtos import DofbotDto
from tiphareth.urls import API_DOFBOT_CONTROLLER, API_DOFBOT_CONTROLLER_SET_NEWTRAL
from yesod.dofbot import DofbotModel
from binah.config import Config
from markuth.dofbot_controller import DofBotController

router = APIRouter()

def get_config() -> Config:
    from kether.main import config_manager
    return config_manager.get_config()

@router.post(API_DOFBOT_CONTROLLER)
def control_dofbot(
    dofbot: DofbotDto,
    dofbot_controller: DofBotController = Depends(DofBotController),
    config: Config = Depends(get_config)
):
    dofbot_control_params = DofbotModel(
        servo1=dofbot.servo1,
        servo2=dofbot.servo2,
        servo3=dofbot.servo3,
        servo4=dofbot.servo4,
        servo5=dofbot.servo5,
        servo6=dofbot.servo6
    )

    dofbot_controller.control_dofbot(dofbot_control_params, config)
    return {status.HTTP_200_OK: "DOFBOT controlled successfully"}


@router.get(API_DOFBOT_CONTROLLER_SET_NEWTRAL)
def set_newtral_position(
    dofbot_controller: DofBotController = Depends(DofBotController),
    config: Config = Depends(get_config)
):
    dofbot_controller.set_newtral_position(config)
    return {status.HTTP_200_OK: "DOFBOT set to newtral position successfully"}