from pydantic import BaseModel

class DofbotModel(BaseModel):
    servo1: int
    servo2: int
    servo3: int
    servo4: int
    servo5: int
    servo6: int