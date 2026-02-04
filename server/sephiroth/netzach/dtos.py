from pydantic import BaseModel

class DofbotDto(BaseModel):
    servo1: int
    servo2: int
    servo3: int
    servo4: int
    servo5: int
    servo6: int

    def validate(self):
        if not (0 <= self.servo1 <= 180):
            raise ValueError("servo1 must be between 0 and 180")
        if not (0 <= self.servo2 <= 180):
            raise ValueError("servo2 must be between 0 and 180")
        if not (0 <= self.servo3 <= 180):
            raise ValueError("servo3 must be between 0 and 180")
        if not (0 <= self.servo4 <= 180):
            raise ValueError("servo4 must be between 0 and 180")
        if not (0 <= self.servo5 <= 180):
            raise ValueError("servo5 must be between 0 and 180")
        if not (0 <= self.servo6 <= 180):
            raise ValueError("servo6 must be between 0 and 180")