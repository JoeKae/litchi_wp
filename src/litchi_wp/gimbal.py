"""
Module for litchi waypoint gimbal settings
"""
# pylint: disable=import-error
from litchi_wp.enums import GimbalMode


class Gimbal:
    """
    Class representing litchi waypoint gimbal settings

    Attributes:
            mode (GimbalMode): The mode for the gimbal setting
            pitchangle (int): The gimbal angle in degrees

    """

    def __init__(self, mode: GimbalMode = GimbalMode.DISABLED, pitchangle: float = 0):
        """
        Constructor

        Args:
            mode (GimbalMode): The mode for the gimbal (disabled, focus poi or interpolate)
            pitchangle (float): The gimbal angle in degrees

        Raises:
            ValueError: If mode is no valid GimbalMode or pitchangle cannot be float

        """
        self.mode = GimbalMode(mode)
        self.pitchangle = float(pitchangle)

    def set_focus_poi(self):
        """
        Setter for focus poi mode
        """
        self.set_mode(GimbalMode.FOCUS_POI)

    def set_interpolate(self, pitchangle: float):
        """
        Setter for interpolate mode

        Raises:
            ValueError: If pitchangle cannot be float

        """
        self.set_mode(GimbalMode.INTERPOLATE)
        self.set_pitchangle(pitchangle)

    def set_mode(self, mode: GimbalMode):
        """
        Setter for mode

        Args:
            mode (GimbalMode): The mode for the gimbal (disabled, focus poi or interpolate)

        Raises:
            ValueError: If mode is no valid GimbalMode

        """
        self.mode = GimbalMode(mode)

    def set_pitchangle(self, pitchangle: float):
        """
        Setter for pitchangle

        Args:
            pitchangle (float): The gimbal angle in degrees

        Raises:
            ValueError: If pitchangle cannot be float or pitchangle < -90 or pitchangle > 30

        """
        if float(pitchangle) < -90 or float(pitchangle) > 30:
            raise ValueError('allowed range is -90 to 30')
        self.pitchangle = float(pitchangle)
