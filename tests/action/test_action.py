# pylint: skip-file
from unittest import TestCase

from litchi_wp.action import Action
from litchi_wp.enums import ActionType


class TestAction(TestCase):
    def test_set_type(self):
        types = [
            ActionType.NO_ACTION,
            ActionType.TAKE_PHOTO,
            ActionType.STAY_FOR,
            ActionType.ROTATE_AIRCRAFT,
            ActionType.TILT_CAMERA,
            ActionType.START_RECORDING,
            ActionType.STOP_RECORDING,
            "abc",
            -1,
            0,
            4.1
        ]
        for t in types:
            action = Action()
            try:
                ActionType(t)
                action.set_type(t)
                self.assertEqual(ActionType(t), action.type)
            except ValueError:
                self.assertRaises(ValueError, action.set_type, actiontype=t)

    def test_set_param(self):
        types = [
            ActionType.NO_ACTION,
            ActionType.TAKE_PHOTO,
            ActionType.STAY_FOR,
            ActionType.ROTATE_AIRCRAFT,
            ActionType.TILT_CAMERA,
            ActionType.START_RECORDING,
            ActionType.STOP_RECORDING,
            ]
        params = list(range(-3000, 3000))
        params.extend([10.4, "9.3", "abc"])
        for param in params:
            for t in types:
                action = Action()
                action.set_type(t)
                try:
                    float(param)
                    action.set_param(param)
                    self.assertEqual(float(param), action.param)
                except ValueError:
                    self.assertRaises(ValueError, action.set_param, param=param)

    def test_delete(self):
        action = Action()
        action.delete()
        self.assertEqual(ActionType.NO_ACTION, action.type)

    def test_set_stay_for(self):
        msecs = list(range(-33000, 33000))
        msecs.extend(["abc", 10.1, "99.3"])
        for ms in msecs:
            action = Action()
            try:
                if int(ms) < 0 or int(ms) > 32000:
                    raise ValueError
                action.set_stay_for(ms)
                self.assertEqual(ActionType.STAY_FOR, action.type)
                self.assertEqual(int(ms), action.param)
            except ValueError:
                self.assertRaises(ValueError, action.set_stay_for, msec=ms)

    def test_set_take_photo(self):
        action = Action()
        action.set_take_photo()
        self.assertEqual(ActionType.TAKE_PHOTO, action.type)

    def test_set_start_rec(self):
        action = Action()
        action.set_start_rec()
        self.assertEqual(ActionType.START_RECORDING, action.type)

    def test_set_stop_rec(self):
        action = Action()
        action.set_stop_rec()
        self.assertEqual(ActionType.STOP_RECORDING, action.type)

    def test_set_rotate(self):
        degrees = list(range(-1000, 1000))
        degrees.extend([float(i/100) for i in range(-100000, 100000)])
        degrees.extend(["10", "-50.4", "abc"])
        for degree in degrees:
            action = Action()
            try:
                if float(degree) < 0 or float(degree) > 359:
                    raise ValueError
                action.set_rotate(degree)
                self.assertEqual(ActionType.ROTATE_AIRCRAFT, action.type)
                self.assertEqual(float(degree), action.param)
            except ValueError:
                self.assertRaises(ValueError, action.set_rotate, deg=degree)

    def test_set_tilt_cam(self):
        degrees = list(range(-1000, 1000))
        degrees.extend([float(i / 100) for i in range(-100000, 100000)])
        degrees.extend(["10", "-50.4", "abc"])
        for degree in degrees:
            action = Action()
            try:
                if float(degree) < -90 or float(degree) > 30:
                    raise ValueError
                action.set_tilt_cam(degree)
                self.assertEqual(ActionType.TILT_CAMERA, action.type)
                self.assertEqual(float(degree), action.param)
            except ValueError:
                self.assertRaises(ValueError, action.set_tilt_cam, deg=degree)
