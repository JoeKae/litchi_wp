from enum import Enum

class RegEx(Enum):
    VALID_LITCHI_WP_LINE: str
class RotationDirection(Enum):
    CW: int
    CCW: int

class GimbalMode(Enum):
    DISABLED: int
    FOCUS_POI: int
    INTERPOLATE: int

class AltitudeMode(Enum):
    MSL: int
    AGL: int

class ActionType(Enum):
    NO_ACTION: int
    STAY_FOR: int
    TAKE_PHOTO: int
    START_RECORDING: int
    STOP_RECORDING: int
    ROTATE_AIRCRAFT: int
    TILT_CAMERA: int
