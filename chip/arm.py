from servo import Servo
from time import sleep
from limb import Limb

class Arm(Limb):
    """Represents an arm with a hand.
    """

    arm = Servo()
    hand = Servo()

    def __init__(self, arm_pin:int=0, hand_pin:int=1, name:str="Arm"):
        """_summary_

        Args:
            arm_pin (int, optional): _description_. Defaults to 0.
            hand_pin (int, optional): _description_. Defaults to 1.
            name (str, optional): _description_. Defaults to "Arm".

        Example:
            >>> from arm import Arm
            >>> arm = Arm()
            >>> arm.wave(2)
            
        """
        self.name = name
        self.arm = Servo(arm_pin)
        self.hand = Servo(hand_pin)

    def wave(self, times_to_wave:int=2):
        """ Wave the hand, using the times_to_wave parameter to determine how many times to wave.

        Args:
            times_to_wave (int, optional): _description_. Defaults to 2.
        """
        
        for i in range(times_to_wave):
            self.hand.value(-50)
            sleep(0.5)
            self.hand.value(50)
            sleep(0.5)