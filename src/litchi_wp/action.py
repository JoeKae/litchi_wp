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
        param (int): The parameter of the action. Depends on the actiontype
    """

    def __init__(
            self,
            actiontype: ActionType = ActionType.NO_ACTION,
            param: int = 0
    ):
        """
        Constructor

        Parameters:
            actiontype (ActionType): The type of the action
            param (float): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
                - Take Photo (set to 0)
                - Start Recording (set to 0)
                - Stop Recording (set to 0)
        """
        self.type: ActionType = actiontype
        self.param = param

    def set_type(self, actiontype: ActionType):
        """
        Setter for the type of the action

        Parameters:
            actiontype (Actiontype): The type of the action
        """
        self.type = actiontype.value

    def set_param(self, param: int):
        """
        Setter for the action parameter

        Parameters:
            param (int): The parameter of the action. Depends on the actiontype

                - Stay For (time in milliseconds),
                - Rotate Aircraft (angle in degrees),
                - Tilt Camera (angle in degrees)
        """
        self.param = param

    def delete(self):
        """
        Clear action
        """
        self.type = ActionType.NO_ACTION
        self.param = 0

    def set_stay_for(self, msec: int):
        """
        Setter for 'Stay For' action

        Parameters:
            msec (int): Time to stay in milliseconds
        """
        self.type = ActionType.STAY_FOR
        self.param = msec

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

    def set_rotate(self, deg: int):
        """
        Setter for 'Rotate Aircraft' action

        Parameters:
            deg (int): Rotation in degrees
        """
        self.type = ActionType.ROTATE_AIRCRAFT
        self.param = deg

    def set_tilt_cam(self, deg: int):
        """
        Setter for 'Tilt Camera' action

        Parameters:
            deg (int): Tiltangle in degrees
        """
        self.type = ActionType.TILT_CAMERA
        self.param = deg
