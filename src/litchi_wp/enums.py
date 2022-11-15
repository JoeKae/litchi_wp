"""
Module to bundle all enum classes
"""
from enum import Enum


class RotationDirection(Enum):
    """
    Enum class for rotation direction
    """
    CW = 0
    CCW = 1


class GimbalMode(Enum):
    """
    Enum class for Gimbalmode
    """
    DISABLED = 0
    FOCUS_POI = 1
    INTERPOLATE = 2


class AltitudeMode(Enum):
    """
    Enum class for Altitudemode
    """
    MSL = 0
    AGL = 1


class ActionType(Enum):
    """
    Enum class for action types
    """
    NO_ACTION = -1
    STAY_FOR = 0
    TAKE_PHOTO = 1
    START_RECORDING = 2
    STOP_RECORDING = 3
    ROTATE_AIRCRAFT = 4
    TILT_CAMERA = 5
