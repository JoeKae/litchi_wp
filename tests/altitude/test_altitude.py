# pylint: skip-file
from unittest import TestCase

from litchi_wp.altitude import Altitude
from litchi_wp.enums import AltitudeMode


class TestAltitude(TestCase):
    def test_set_mode(self):
        modes = [AltitudeMode.AGL, AltitudeMode.MSL, 0, "0", -1, 0.4]
        for mode in modes:
            altitude = Altitude()
            try:
                AltitudeMode(mode)
                altitude.set_mode(mode)
                self.assertEqual(AltitudeMode(mode), altitude.mode)
            except ValueError:
                self.assertRaises(ValueError, altitude.set_mode, mode=mode)
    def test_set_value(self):
        alts = list(range(-300, 300))
        alts.extend([-10.35, 25.4, "19.3", "abc"])
        for alt in alts:
            altitude = Altitude()
            try:
                float(alt)
                altitude.set_value(alt)
                self.assertEqual(float(alt), altitude.value)
            except ValueError:
                self.assertRaises(ValueError, altitude.set_value, value=alt)
