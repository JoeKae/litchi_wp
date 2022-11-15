"""
Module for litchi waypoint POIs
"""
# pylint: disable=import-error
from litchi_wp.enums import AltitudeMode


class Poi:
    """
    Class representing a litchi waypoint POI

    Attributes:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        altitude (float): The altitude in meters
        altitude_mode (int): The altitudemode
    """

    def __init__(
            self,
            lat: float = 0,
            lon: float = 0,
            altitude: float = 0,
            altitude_mode: AltitudeMode = AltitudeMode.MSL
    ):
        """
        Constructor

        Parameters:
            lat (float): Latitude coordinate for the waypoint in WGS84 format
            lon (float): Longitude coordinate for the waypoint in WGS84 format
            altitude (float): The altitude in meters
            altitude_mode (AltitudeMode): The altitudemode, MSL or AGL
        """
        self.lat = lat
        self.lon = lon
        self.altitude = altitude
        self.altitude_mode = altitude_mode

    def set_coordinates(self, lat: float, lon: float):
        """
        Setter for coordinates

        Parameters:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        """
        self.lat = lat
        self.lon = lon

    def set_altitude(self, altitude: float):
        """
        Setter for altitude

        Parameters:
        altitude (float): The altitude in meters
        """
        self.altitude = altitude

    def set_altitude_mode(self, altitude_mode: AltitudeMode):
        """
        Setter for the altitude mode

        Parameters:
            altitude_mode (AltitudeMode): The altitudemode (MSL or AGL)
        """
        self.altitude_mode = altitude_mode
