# pylint: skip-file
from unittest import TestCase

from litchi_wp.enums import GimbalMode
from litchi_wp.gimbal import Gimbal


class TestGimbal(TestCase):
    def test_set_focus_poi(self):
        gimbal = Gimbal()
        gimbal.set_focus_poi()
        self.assertEqual(GimbalMode.FOCUS_POI, gimbal.mode)

    def test_set_interpolate(self):
        angles = list(range(-90, 20))
        angles.extend([-10.5, 2.4, "10.1", "abc"])
        for angle in angles:
            gimbal = Gimbal()
            try:
                float(angle)
                gimbal.set_interpolate(angle)
                self.assertEqual(float(angle), gimbal.pitchangle)
                self.assertEqual(GimbalMode.INTERPOLATE, gimbal.mode)
            except ValueError:
                self.assertRaises(ValueError, gimbal.set_interpolate, pitchangle=angle)

    def test_set_mode(self):
        modes = [
            "abc",
            "0",
            0,
            -1,
            GimbalMode.FOCUS_POI,
            GimbalMode.INTERPOLATE,
            GimbalMode.DISABLED
        ]
        for mode in modes:
            gimbal = Gimbal()
            try:
                GimbalMode(mode)
                gimbal.set_mode(mode)
                self.assertEqual(GimbalMode(mode), gimbal.mode)
            except ValueError:
                self.assertRaises(ValueError, gimbal.set_mode, mode=mode)

    def test_set_pitchangle(self):
        angles = list(range(-90, 20))
        angles.extend([-10.5, 2.4, "10.1", "abc"])
        for angle in angles:
            gimbal = Gimbal()
            try:
                float(angle)
                gimbal.set_pitchangle(angle)
                self.assertEqual(float(angle), gimbal.pitchangle)
            except ValueError:
                self.assertRaises(ValueError, gimbal.set_pitchangle, pitchangle=angle)
