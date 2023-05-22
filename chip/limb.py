class Limb():
    """ An abstract class that represents a limb.

    Attributes:
        name (str): The name of the limb.

    Example:
        >>> from limb import Limb
        >>> limb = Limb()
        >>> print(limb)

    """

    name = ""

    def __init__(self, name:str="Limb"):
        self.name = name
       
    def __str__(self):
        return self.name

    def wiggle(self, times_to_wiggle:int=2):
        """ Wiggle the limb, using the times_to_wiggle parameter to determine how many times to wiggle.

        Args:
            times_to_wiggle (int, optional): _description_. Defaults to 2.
        """
        pass