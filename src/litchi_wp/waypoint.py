"""
Module for working with the litchi csv waypoints
"""
# pylint: disable=import-error,too-many-arguments,too-many-instance-attributes
from litchi_wp.action import Action, ActionType
from litchi_wp.altitude import Altitude, AltitudeMode
from litchi_wp.enums import RotationDirection
from litchi_wp.gimbal import Gimbal, GimbalMode
from litchi_wp.photo import Photo
from litchi_wp.poi import Poi


class Waypoint:
    """
    Class representing a litchi waypoint

    Attributes:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        altitude (float): Altitude in meters
        heading (float): Heading in degrees
        curvesize (float): Curvesize (radius?) in meter
        rotationdir (RotationDirection):
            Direction of rotation ??(0=cw, 1=ccw)?? (always 0 from mission hub)
        gimbal (Gimbal): Gimbal settings
        actions (list[Action]): List of Action objects
        speed (float): Speed in meters per second
        poi (Poi): Poi object
        photo (Photo): Photo object
    """

    def __init__(
            self,
            lat: float,
            lon: float,
            alt: float,
            head: float = 180,
            curve: float = 0,
            rot: RotationDirection = RotationDirection.CW,
            speed: float = 0,
    ):
        self.lat = lat
        self.lon = lon
        self.altitude = Altitude(value=alt)
        self.heading = head
        self.curvesize = curve
        self.rotationdir = rot
        self.gimbal = Gimbal()
        self.actions = [Action() for i in range(0, 15)]
        self.speed = speed
        self.poi = Poi()
        self.photo = Photo()

    def set_coordinates(self, lat: float, lon: float):
        """
        Setter for coordinates

        Parameters:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        """
        self.lat = lat
        self.lon = lon

    def set_altitude(self, value: float, mode: AltitudeMode = AltitudeMode.AGL):
        """
        Setter for altitude

        Parameters:
            value (float): The height in meters
            mode (AltitudeMode): The altitude mode (MSL or AGL)
        """
        self.altitude.set_value(value)
        self.altitude.set_mode(mode)

    def set_heading(self, value: float):
        """
        Setter for heading

        Parameters:
            value (float): The heading in degrees (0 = north, 180 = south)
        """
        self.heading = value

    def set_curvesize(self, value: float):
        """
        Setter for curve size

        Parameters:
            value (float): The curve radius in meters
        """
        self.curvesize = value

    def set_rotation_direction(self, value: RotationDirection = RotationDirection.CW):
        """
        Setter for the rotation direction

        Parameters:
            value (RotationDirection): Clockwise or Counterclockwise rotation
        """
        self.rotationdir = value

    def set_gimbal(self, mode: GimbalMode, pitchangle: float = 0):
        """
        Setter for gimbal mode

        Parameters:
            mode (GimbalMode): The mode setting for the gimbal
            pitchangle (float): The angle for the gimbal (only for interpolate mode)
        """
        match mode:
            case GimbalMode.DISABLED:
                self.gimbal.set_mode(GimbalMode.DISABLED)
            case GimbalMode.FOCUS_POI:
                self.gimbal.set_focus_poi()
            case GimbalMode.INTERPOLATE:
                self.gimbal.set_interpolate(pitchangle)

    def set_speed_ms(self, value: float):
        """
        Setter for speed in meters per second

        Parameters:
            value (float): The speed in meters per second
        """
        self.speed = value

    def set_speed_kmh(self, value: float):
        """
        Setter for speed in kilometers per hour

        Parameters:
            value (float): The speed in kilometers per hour
        """
        self.speed = value / 3.6

    def set_poi(
            self,
            lat: float,
            lon: float,
            alt: float,
            alt_mode: AltitudeMode = AltitudeMode.MSL
    ):
        """
        Setter for point of interest

        Parameters:
            lat (float): Latitude coordinate for the waypoint in WGS84 format
            lon (float): Longitude coordinate for the waypoint in WGS84 format
            alt (float): The altitude in meters
            alt_mode (AltitudeMode): The altitudemode, MSL or AGL
        """
        self.poi.set_coordinates(lat, lon)
        self.poi.set_altitude(alt)
        self.poi.set_altitude_mode(alt_mode)

    def set_photo_interval_time(self, seconds: float):
        """
        Setter for photo time interval

        Parameters:
            seconds (float): The time in seconds between each photo
        """
        self.photo.set_time_interval(seconds)

    def set_photo_interval_distance(self, meters: float):
        """
        Setter for photo distance interval

        Parameters:
            meters (float): The distance in meters between each photo
        """
        self.photo.set_distance_interval(meters)

    def set_action(self, index: int, actiontype: ActionType, param: int = 0):
        """
        Setter for actions

        Parameters:
            index (int): Action slot (0, ... ,14)
            actiontype (ActionType): The type of the action
            param (float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
                - Take Photo (set to 0)
                - Start Recording (set to 0)
                - Stop Recording (set to 0)
        """
        if index > 14 or index < 0:
            return
        match actiontype:
            case ActionType.NO_ACTION:
                self.actions[index].delete()
            case ActionType.ROTATE_AIRCRAFT:
                self.actions[index].set_rotate(param)
            case ActionType.STAY_FOR:
                self.actions[index].set_stay_for(param)
            case ActionType.TILT_CAMERA:
                self.actions[index].set_tilt_cam(param)
            case ActionType.TAKE_PHOTO:
                self.actions[index].set_take_photo()
            case ActionType.START_RECORDING:
                self.actions[index].set_start_rec()
            case ActionType.STOP_RECORDING:
                self.actions[index].set_stop_rec()

    @staticmethod
    def get_header(line_break='\n'):
        """
        Getter for the waypoint file header
        """
        ret = 'latitude,longitude,altitude(m),heading(deg),' \
              'curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,' \
              'actiontype1,actionparam1,actiontype2,actionparam2,' \
              'actiontype3,actionparam3,actiontype4,actionparam4,' \
              'actiontype5,actionparam5,actiontype6,actionparam6,' \
              'actiontype7,actionparam7,actiontype8,actionparam8,' \
              'actiontype9,actionparam9,actiontype10,actionparam10,' \
              'actiontype11,actionparam11,actiontype12,' \
              'actionparam12,actiontype13,actionparam13,actiontype14,' \
              'actionparam14,actiontype15,actionparam15,' \
              'altitudemode,speed(m/s),poi_latitude,' \
              'poi_longitude,poi_altitude(m),poi_altitudemode,' \
              'photo_timeinterval,photo_distinterval'
        if line_break:
            ret += line_break
        return ret

    def to_line(self, line_break='\n'):
        """
        Transforms the waypoint to a line in litchi csv format
        """
        line = ''
        line += str(self.lat) + ','
        line += str(self.lon) + ','
        line += str(self.altitude.value) + ','
        line += str(self.heading) + ','
        line += str(self.curvesize) + ','
        line += str(self.rotationdir.value) + ','
        line += str(self.gimbal.mode.value) + ','
        line += str(self.gimbal.pitchangle) + ','
        for i in range(0, 15):
            line += str(self.actions[i].type.value) + ','
            line += str(self.actions[i].param) + ','
        line += str(self.altitude.mode.value) + ','
        line += str(self.speed) + ','
        line += str(self.poi.lat) + ','
        line += str(self.poi.lon) + ','
        line += str(self.poi.altitude) + ','
        line += str(self.poi.altitude_mode.value) + ','
        line += str(self.photo.time_interval) + ','
        line += str(self.photo.distance_interval)
        if line_break:
            line += line_break
        return line
