"""
Module for litchi waypoint altitude settings
"""
# pylint: disable=import-error
from litchi_wp.enums import AltitudeMode


class Altitude:
    """
    Class representing litchi waypoint altitude settings

    Attributes:
        value (float): The height in meters
        mode (AltitudeMode): The altitude mode
    """

    def __init__(self, value: float = -1.0, mode: AltitudeMode = AltitudeMode.AGL):
        """
        Constructor

        value (float): The height in meters
        mode (AltitudeMode): The altitude mode (MSL or AGL)
        """
        self.value = value
        self.mode = mode

    def set_mode(self, mode: AltitudeMode):
        """
        Setter for Altitudemode

        Parameters:
            mode (AltitudeMode): The enum of Altitudemode
        """
        self.mode = mode

    def set_value(self, value: float):
        """
        Setter for value

        Parameters:
            value (float): The height in meters
        """
        self.value = value
