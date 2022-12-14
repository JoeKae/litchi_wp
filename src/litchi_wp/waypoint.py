"""
Module for working with the litchi csv waypoints
"""
# pylint: disable=import-error,too-many-arguments,too-many-instance-attributes
import re
from litchi_wp.action import Action, ActionType
from litchi_wp.altitude import Altitude, AltitudeMode
from litchi_wp.enums import RotationDirection, RegEx
from litchi_wp.gimbal import Gimbal, GimbalMode
from litchi_wp.photo import Photo
from litchi_wp.poi import Poi


class Waypoint:
    """
    Class representing a litchi waypoint

    Attributes:
        lat (float): Latitude coordinate for the waypoint in WGS84 format
        lon (float): Longitude coordinate for the waypoint in WGS84 format
        altitude (Altitude): Altitude object
        heading (float): Heading in degrees
        curvesize (float): Curvesize (radius?) in meter
        rotationdir (RotationDirection):
            Direction of rotation ??(0=cw, 1=ccw)?? (always 0 from mission hub)
        gimbal (Gimbal): Gimbal settings
        actions (list[Action]): List of Action objects
        speed (float): Speed in meters per second
        poi (Poi): Poi object
        photo (Photo): Photo object
        next_action_index (int): The index of the next free action slot (max 14)

        Raises:
            ValueError: If [lat, lon, alt, head, curve, speed] cannot be float
                        or rot is no valid RotationDirection

    """
    next_action_index = 0

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
        self.lat = float(lat)
        self.lon = float(lon)
        self.altitude = Altitude(value=alt)
        self.heading = float(head)
        self.curvesize = float(curve)
        self.rotationdir = RotationDirection(rot)
        self.gimbal = Gimbal()
        self.actions = [Action() for i in range(0, 15)]
        self.speed = float(speed)
        self.poi = Poi()
        self.photo = Photo()

    def set_coordinates(self, lat: float, lon: float):
        """
        Setter for coordinates

        Args:
            lat (float): Latitude coordinate for the waypoint in WGS84 format
            lon (float): Longitude coordinate for the waypoint in WGS84 format

        Raises:
            ValueError: If lat cannot be float or lon cannot be float

        """
        self.lat = float(lat)
        self.lon = float(lon)

    def set_altitude(self, value: float, mode: AltitudeMode = AltitudeMode.AGL):
        """
        Setter for altitude

        Args:
            value (float): The height in meters
            mode (AltitudeMode): The altitude mode (MSL or AGL)

        Raises:
            ValueError: If value cannot be float or mode is no valid AltitudeMode

        """
        self.altitude.set_value(float(value))
        self.altitude.set_mode(AltitudeMode(mode))

    def set_heading(self, value: float):
        """
        Setter for heading

        Args:
            value (float): The heading in degrees (0 = north, 180 = south)

        Raises:
            ValueError: If value cannot be float

        """
        self.heading = float(value)

    def set_curvesize(self, value: float):
        """
        Setter for curve size

        Args:
            value (float): The curve radius in meters

        Raises:
            ValueError: If value cannot be float

        """
        self.curvesize = abs(float(value))

    def set_rotation_direction(self, value: RotationDirection = RotationDirection.CW):
        """
        Setter for the rotation direction

        Args:
            value (RotationDirection): Clockwise or Counterclockwise rotation

        Raises:
            ValueError: If value is not a valid RotationDirection

        """
        self.rotationdir = RotationDirection(value)

    def set_gimbal(self, mode: GimbalMode, pitchangle: float = 0):
        """
        Setter for gimbal mode

        Args:
            mode (GimbalMode): The mode setting for the gimbal
            pitchangle (float): The angle for the gimbal (only for interpolate mode)

        Raises:
            ValueError: If mode is no valid GimbalMode. Or mode is GimbalMode.Interpolate and
                        (pitchangle cannot be float or pitchangle < -90 or pitchangle > 30)

        """
        match GimbalMode(mode):
            case GimbalMode.DISABLED:
                self.gimbal.set_mode(GimbalMode.DISABLED)
            case GimbalMode.FOCUS_POI:
                self.gimbal.set_focus_poi()
            case GimbalMode.INTERPOLATE:
                self.gimbal.set_interpolate(pitchangle)

    def set_speed_ms(self, value: float):
        """
        Setter for speed in meters per second

        Args:
            value (float): The speed in meters per second

        Raises:
            ValueError: If value cannot be float

        """
        self.speed = float(value)

    def set_speed_kmh(self, value: float):
        """
        Setter for speed in kilometers per hour

        Args:
            value (float): The speed in kilometers per hour

        Raises:
            ValueError: If value cannot be float

        """
        self.speed = float(value) / 3.6

    def set_poi(
            self,
            lat: float,
            lon: float,
            alt: float,
            alt_mode: AltitudeMode = AltitudeMode.MSL
    ):
        """
        Setter for point of interest
        Args:
            lat (float): Latitude coordinate for the waypoint in WGS84 format
            lon (float): Longitude coordinate for the waypoint in WGS84 format
            alt (float): The altitude in meters
            alt_mode (AltitudeMode): The altitudemode, MSL or AGL

        Raises:
            ValueError: If [lat, lon, alt] cannot be float or alt_mode is no valid AltitudeMode

        """
        self.poi.set_coordinates(float(lat), float(lon))
        self.poi.set_altitude(float(alt))
        self.poi.set_altitude_mode(AltitudeMode(alt_mode))

    def set_photo_interval_time(self, seconds: float):
        """
        Setter for photo time interval

        Args:
            seconds (float): The time in seconds between each photo

        Raises:
            ValueError: If seconds cannot be float

        """
        self.photo.set_time_interval(float(seconds))

    def set_photo_interval_distance(self, meters: float):
        """
        Setter for photo distance interval

        Args:
            meters (float): The distance in meters between each photo

        Raises:
            ValueError: If meters cannot be float

        """
        self.photo.set_distance_interval(float(meters))

    def replace_action(self, index: int, action_type: ActionType, param: int | float = 0):
        """
        Replaces actions at index

        Args:
            index (int): Action slot (0, ... ,14)
            action_type (ActionType): The type of the action
            param (int | float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
                - Take Photo (set to 0)
                - Start Recording (set to 0)
                - Stop Recording (set to 0)

        Raises:
            IndexError: If index < 0 or index > 14
            ValueError: If index cannot be int or param cannot be float
                        or action_type is not valid ActionType

        """
        if int(index) > 14 or int(index) < 0:
            raise IndexError(f"Index {index} is out of bounds (0 ... 14)")
        match ActionType(action_type):
            case ActionType.NO_ACTION:
                self.actions[index].delete()
            case ActionType.ROTATE_AIRCRAFT:
                self.actions[index].set_rotate(param)
            case ActionType.STAY_FOR:
                self.actions[index].set_stay_for(int(param))
            case ActionType.TILT_CAMERA:
                self.actions[index].set_tilt_cam(param)
            case ActionType.TAKE_PHOTO:
                self.actions[index].set_take_photo()
            case ActionType.START_RECORDING:
                self.actions[index].set_start_rec()
            case ActionType.STOP_RECORDING:
                self.actions[index].set_stop_rec()

    def set_action(self, action_type: ActionType, param: int | float = 0) -> int:
        """
        Setter for actions

        Args:
            action_type (ActionType): The type of the action
            param (int | float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
                - Take Photo (set to 0)
                - Start Recording (set to 0)
                - Stop Recording (set to 0)

        Returns:
            The index of the action or -1 if no action slots are available

        Raises:
            ValueError: If action_type is no valid ActionType or param cannot be float

        """
        ret = -1
        if self.next_action_index <= 14:
            self.replace_action(
                index=self.next_action_index,
                action_type=ActionType(action_type),
                param=float(param)
            )
            ret = self.next_action_index
            self.next_action_index += 1
        return ret

    @staticmethod
    def get_header(line_break='\n') -> str:
        """
        Getter for the waypoint file header

        Args:
            line_break (str | bool | None): Linebreak character, disable with None or False

        Returns:
            The header as a string

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

    def to_line(self, line_break: str | bool | None = '\n') -> str:
        """
        Transforms the waypoint to a line in litchi csv format

        Args:
            line_break (str | bool | None): Linebreak character, disable with None or False

        Returns:
            The serialized waypoint in litchi csv format

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
        line += str(self.poi.altitude.value) + ','
        line += str(self.poi.altitude.mode.value) + ','
        line += str(self.photo.time_interval) + ','
        line += str(self.photo.distance_interval)
        if line_break:
            if line_break is not True:
                line += line_break
        return line

    @staticmethod
    def from_line(line: str) -> 'Waypoint':
        """
        Parses a line from a litchi waypoint csv file and returns an instance of the Waypoint

        Args:
            line (str): The litchi waypoints csv line

        Returns:
            The Waypoint as an instance

        Raises:
            ValueError: If line does not match regex filter

        """
        match = re.search(RegEx.VALID_LITCHI_WP_LINE.value, line)
        if match:
            rows = match.group().split(',')

            def get_float(index: int):
                return float(rows[index])

            def get_int(index: int):
                return int(get_float(index))

            waypoint = Waypoint(
                lat=get_float(0),
                lon=get_float(1),
                alt=get_float(2)
            )
            waypoint.set_heading(get_float(3))
            waypoint.set_curvesize(get_float(4))
            waypoint.set_rotation_direction(RotationDirection(get_int(5)))
            waypoint.set_gimbal(
                mode=GimbalMode(get_int(6)),
                pitchangle=get_float(7)
            )
            action_index = 0
            for i in range(8, 8 + 30, 2):
                waypoint.replace_action(
                    index=action_index,
                    action_type=ActionType(get_int(i)),
                    param=get_float(i + 1)
                )
                action_index += 1
            waypoint.set_altitude(
                get_float(2),
                mode=AltitudeMode(get_int(38))
            )
            waypoint.set_speed_ms(get_float(39))
            waypoint.set_poi(
                lat=get_float(40),
                lon=get_float(41),
                alt=get_float(42),
                alt_mode=AltitudeMode(get_int(43))
            )
            waypoint.photo.time_interval = get_float(44)
            waypoint.photo.distance_interval = get_float(45)
            return waypoint
        raise ValueError('invalid_input')

    @staticmethod
    def from_file(filename: str) -> list['Waypoint']:
        """
        Creates a list of Waypoints from a litchi waypoint csv file.
        Prints out any lines that did not match the regular expression.
        Format: {line_number}: {line}

        Args:
            filename (str): The path + filename of the file to be parsed

        Returns:
            The list of parsed Waypoints

        """
        with open(filename, encoding='utf-8', mode='r') as file:
            file_content = file.read()
        rows = file_content.split('\n')
        wp_list = []
        no_ignored_lines = True
        for row in rows:
            try:
                wp_list.append(
                    Waypoint.from_line(row)
                )
            except ValueError:
                if no_ignored_lines:
                    no_ignored_lines = False
                    print('Ignored lines:')
                print(f"{rows.index(row)}: {row}")
        return wp_list
