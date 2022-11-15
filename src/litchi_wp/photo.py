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

        Parameters:
            time_interval (float): The interval between photos in seconds, disable with -1.0
            distance_interval (float): The interval between photos in meters, disable with -1.0
        """
        self.time_interval = time_interval
        self.distance_interval = distance_interval

    def set_time_interval(self, interval: float):
        """
        Setter for time based interval

        Parameters:
            interval (float): The interval between photos in seconds, disable with -1.0
        """
        self.time_interval = interval
        self.distance_interval = 0

    def set_distance_interval(self, interval: float):
        """
        Setter for distance based interval

        Parameters:
            interval (float): The interval between photos in seconds, disable with -1.0
        """
        self.distance_interval = interval
        self.time_interval = 0
