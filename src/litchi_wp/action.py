"""
Module for litchi waypoint actions
"""
# pylint: disable=import-error
from litchi_wp.enums import ActionType


class Action:
    """
    Class respresenting a litchi waypoint action

    Attributes:
        type (ActionType): The type of the action
        param (int | float): The parameter of the action. Depends on the actiontype

    """

    def __init__(
            self,
            actiontype: ActionType = ActionType.NO_ACTION,
            param: int | float = 0
    ):
        """
        Constructor

        Args:
            actiontype (ActionType): The type of the action
            param (float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
                - Take Photo (set to 0)
                - Start Recording (set to 0)
                - Stop Recording (set to 0)

        Raises:
            ValueError: If actiontype is no valid ActionType or param cannot be float

        """
        self.type: ActionType = ActionType(actiontype)
        self.param = float(param)

    def set_type(self, actiontype: ActionType):
        """
        Setter for the type of the action

        Args:
            actiontype (Actiontype): The type of the action

        Raises:
            ValueError: If actiontype is no valid ActionType

        """
        self.type = ActionType(actiontype)

    def set_param(self, param: int | float):
        """
        Setter for the action parameter

        Args:
            param (int | float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)

        Raises:
            ValueError: If param cannot be float

        """
        self.param = float(param)

    def delete(self):
        """
        Clear action
        """
        self.type = ActionType.NO_ACTION
        self.param = 0

    def set_stay_for(self, msec: int):
        """
        Setter for 'Stay For' action

        Args:
            msec (int): Time to stay in milliseconds

        Raises:
            ValueError: If msec cannot be int or msec < 0 or msec > 32000

        """
        if int(msec) < 0 or int(msec) > 32000:
            raise ValueError('allowed range is 0 to 32000')
        self.type = ActionType.STAY_FOR
        self.param = int(msec)

    def set_take_photo(self):
        """
        Setter for 'Take Photo' action
        """
        self.type = ActionType.TAKE_PHOTO
        self.param = 0

    def set_start_rec(self):
        """
        Setter for 'Start Recording' action
        """
        self.type = ActionType.START_RECORDING
        self.param = 0

    def set_stop_rec(self):
        """
        Setter for 'Stop Recording' action
        """
        self.type = ActionType.STOP_RECORDING
        self.param = 0

    def set_rotate(self, deg: int | float):
        """
        Setter for 'Rotate Aircraft' action

        Args:
            deg (int | float): Rotation in degrees

        Raises:
            ValueError: If deg cannot be float or deg < 0 or deg > 359

        """
        if float(deg) < 0 or float(deg) > 359:
            raise ValueError('allowed range is 0 to 359')
        self.type = ActionType.ROTATE_AIRCRAFT
        self.param = float(deg)

    def set_tilt_cam(self, deg: int | float):
        """
        Setter for 'Tilt Camera' action

        Args:
            deg (int | float): Tiltangle in degrees

        Raises:
            ValueError: If deg cannot be float or deg < -90 or deg > 30

        """
        if float(deg) < -90 or float(deg) > 30:
            raise ValueError('allowed range is -90 to 30')
        self.type = ActionType.TILT_CAMERA
        self.param = float(deg)
