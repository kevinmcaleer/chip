from leg import Leg
from arm import Arm
from servo import Servo

class Chip():
    """_summary_
    """

    left_arm = Arm()
    right_arm = Arm()
    left_leg = Leg()
    right_leg = Leg()
    neck = Servo()

    def __init__(self):
        self.name = "Chip"
        
    def clap(self):
        # TODO: Implement this
        pass

    def stand(self):
        # TODO: Implement this
        pass

    def sit(self):
        # TODO: Implement this
        pass