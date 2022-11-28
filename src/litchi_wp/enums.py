"""
Module to bundle all enum classes
"""
from enum import Enum


# pylint: disable=anomalous-backslash-in-string
class RegEx(Enum):
    """
    Enum class for all regular expressions strings
    """
    VALID_LITCHI_WP_LINE = (
            '^[-]?\d+(\.\d+)?,'  # latitude
            + '[-]?\d+(\.\d+)?,'  # longitude
            + '\d+(\.\d+)?,'  # altitude(m)
            + '[-]?\d+(\.\d+)?,'  # heading(deg)
            + '[-]?\d+(\.\d+)?,'  # curvesize(m)
            + '[0-1]+,'  # rotationdir
            + '([-1]|[0-2]),'  # gimbalmode
            + '[-]?\d+(\.\d+)?,'  # gimbalpitchangle
            + '((-1|[0-5]),[-]?\d+(\.\d+)?,){15}'  # actiontype, actionparam 1-15
            + '[0-1],'  # altitudemode
            + '\d+(\.\d+)?,'  # speed(m/s)
            + '[-]?\d+(\.\d+)?,'  # poi_latitude
            + '[-]?\d+(\.\d+)?,'  # poi_longitude
            + '\d+(\.\d+)?,'  # poi_altitude(m)
            + '[-]?[0-1],'  # poi_altitudemode
            + '((-1|\d+)(\.\d+)?),'  # photo_timeinterval
            + '((-1|\d+)(\.\d+)?)'  # photo_distinterval
    )


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
