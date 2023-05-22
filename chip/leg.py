from servo import Servo
from limb import Limb

class Leg(Limb):
    """ Represents a robot leg with all the servos that make it up.

    Attributes:
        upper_leg (Servo): The upper leg servo.
        thigh (Servo): The thigh servo.
        knee (Servo): The knee servo.
        shin (Servo): The shin servo.
        ankle (Servo): The ankle servo.
        hip (Servo): The hip servo.

    Args:
        Limb (_type_): The parent class.
    """
    
    def __init__(self):
        """ Initializes the leg with all the servos that make it up.
        """
        self.name = "Leg"
        self.upper_leg = Servo()
        self.thigh = Servo()
        self.knee = Servo()
        self.shin = Servo()
        self.ankle = Servo()
        self.hip = Servo()
