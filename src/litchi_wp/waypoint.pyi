from typing import Union

from litchi_wp.action import Action as Action, ActionType as ActionType
from litchi_wp.altitude import Altitude as Altitude, AltitudeMode as AltitudeMode
from litchi_wp.enums import RotationDirection as RotationDirection
from litchi_wp.gimbal import Gimbal as Gimbal, GimbalMode as GimbalMode
from litchi_wp.photo import Photo as Photo
from litchi_wp.poi import Poi as Poi

class Waypoint:
    next_action_index: int
    lat: float
    lon: float
    altitude: float
    heading: float
    curvesize: float
    rotationdir: RotationDirection
    gimbal: Gimbal
    actions: list[Action]
    speed: float
    poi: Poi
    photo: Photo
    def __init__(self, lat: float, lon: float, alt: float, head: float = 180, curve: float = 0, rot: RotationDirection = RotationDirection.CW, speed: float = 0) -> None: ...
    def set_coordinates(self, lat: float, lon: float): ...
    def set_altitude(self, value: float, mode: AltitudeMode = AltitudeMode.AGL): ...
    def set_heading(self, value: float): ...
    def set_curvesize(self, value: float): ...
    def set_rotation_direction(self, value: RotationDirection = RotationDirection.CW): ...
    def set_gimbal(self, mode: GimbalMode, pitchangle: float = 0): ...
    def set_speed_ms(self, value: float): ...
    def set_speed_kmh(self, value: float): ...
    def set_poi(self, lat: float, lon: float, alt: float, alt_mode: AltitudeMode = AltitudeMode.MSL): ...
    def set_photo_interval_time(self, seconds: float): ...
    def set_photo_interval_distance(self, meters: float): ...
    def replace_action(self, index: int, action_type: ActionType, param: Union[int, float] = 0): ...
    def set_action(self, action_type: ActionType, param: Union[int, float] = 0) -> int: ...
    @staticmethod
    def get_header(line_break: str = '\n') -> str: ...
    def to_line(self, line_break: Union[str, bool, None] = '\n') -> str: ...
    @staticmethod
    def from_line(line: str) -> Waypoint: ...
    @staticmethod
    def from_file(filename: str) -> list['Waypoint']: ...
