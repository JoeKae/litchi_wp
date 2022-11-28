"""
Module for litchi waypoint photo settings
"""


class Photo:
    """
    Class representing litchi waypoint photo settings

    Attributes:
        time_interval (float): The interval between photos in seconds
        distance_interval (float): The interval between photos in meters

    """

    def __init__(self, time_interval: float = -1.0, distance_interval: float = -1.0):
        """
        Constructor

        Args:
            time_interval (float): The interval between photos in seconds, disable with -1.0
            distance_interval (float): The interval between photos in meters, disable with -1.0

        Raises:
            ValueError: If time_interval cannot be float or distance_interval cannot be float

        """
        self.time_interval = float(time_interval)
        self.distance_interval = float(distance_interval)

    def set_time_interval(self, interval: float):
        """
        Setter for time based interval

        Args:
            interval (float): The interval between photos in seconds, disable with -1.0

        Raises:
            ValueError: If interval cannot be float

        """
        self.time_interval = float(interval)
        self.distance_interval = float(0)

    def set_distance_interval(self, interval: float):
        """
        Setter for distance based interval

        Args:
            interval (float): The interval between photos in seconds, disable with -1.0

        Raises:
            ValueError: If interval cannot be float

        """
        self.distance_interval = float(interval)
        self.time_interval = float(0)
