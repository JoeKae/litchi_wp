"""
Module for litchi waypoint POIs
"""
from litchi_wp.altitude import Altitude
# pylint: disable=import-error
from litchi_wp.enums import AltitudeMode


class Poi:
    """
    Class representing a litchi waypoint POI

    Attributes:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        altitude (AltitudeMode): The altitude in meters

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

        Args:
            lat (float): Latitude coordinate for the waypoint in WGS84 format
            lon (float): Longitude coordinate for the waypoint in WGS84 format
            altitude (float): The altitude in meters
            altitude_mode (AltitudeMode): The altitudemode, MSL or AGL

        Raises:
            ValueError: If lat cannot be float or lon cannot be float or altitude
                        cannot be float or altitude_mode is no valid AltitudeMode

        """
        self.lat = float(lat)
        self.lon = float(lon)
        self.altitude: Altitude = Altitude(value=float(altitude), mode=AltitudeMode(altitude_mode))

    def set_coordinates(self, lat: float, lon: float):
        """
        Setter for coordinates

        Args:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format

        Raises:
            ValueError: If lat cannot be float or lon cannot be float or altitude

        """
        self.lat = float(lat)
        self.lon = float(lon)

    def set_altitude(self, altitude: float):
        """
        Setter for altitude

        Args:
        altitude (float): The altitude in meters

        Raises:
            ValueError: If altitude cannot be float or altitude

        """
        self.altitude.set_value(float(altitude))

    def set_altitude_mode(self, altitude_mode: AltitudeMode):
        """
        Setter for the altitude mode

        Args:
            altitude_mode (AltitudeMode): The altitudemode (MSL or AGL)

        Raises:
            ValueError: If altitude_mode is no valid AltitudeMode

        """
        self.altitude.set_mode(AltitudeMode(altitude_mode))
