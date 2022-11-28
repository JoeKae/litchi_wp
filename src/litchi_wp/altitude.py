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
        Args:
            value (float): The height in meters
            mode (AltitudeMode): The altitude mode (MSL or AGL)

        Raises:
            ValueError: If mode is no valid AltitudeMode or value cannot be float

        """
        self.value = float(value)
        self.mode = AltitudeMode(mode)

    def set_mode(self, mode: AltitudeMode):
        """
        Setter for Altitudemode

        Args:
            mode (AltitudeMode): The enum of Altitudemode

        Raises:
            ValueError: If mode is no valid AltitudeMode

        """
        self.mode = AltitudeMode(mode)

    def set_value(self, value: float):
        """
        Setter for value

        Args:
            value (float): The height in meters

        Raises:
            ValueError: If value cannot be float

        """
        self.value = float(value)
