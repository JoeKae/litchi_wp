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

        """
        self.mode = mode
        self.pitchangle = pitchangle

    def set_focus_poi(self):
        """
        Setter for focus poi mode
        """
        self.set_mode(GimbalMode.FOCUS_POI)

    def set_interpolate(self, pitchangle: float):
        """
        Setter for interpolate mode
        """
        self.set_mode(GimbalMode.INTERPOLATE)
        self.set_pitchangle(pitchangle)

    def set_mode(self, mode: GimbalMode):
        """
        Setter for mode

        Args:
            mode (GimbalMode): The mode for the gimbal (disabled, focus poi or interpolate)

        """
        self.mode = mode

    def set_pitchangle(self, pitchangle: float):
        """
        Setter for pitchangle

        Args:
            pitchangle (float): The gimbal angle in degrees

        """
        self.pitchangle = pitchangle
