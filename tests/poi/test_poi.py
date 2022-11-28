# pylint: skip-file
from unittest import TestCase

from litchi_wp.enums import AltitudeMode
from litchi_wp.poi import Poi


class TestPoi(TestCase):
    lat_tests_valid = [0, 50.188110, -16.972741, "50.118110"]
    lat_tests_invalid = ["abc"]

    lon_tests_valid = [0, 8.042336, -96.328125, "8.042336"]
    lon_tests_invalid = ["abc"]

    alt_tests_valid = [0, 0.8, 50.53, 100, -5, -5.4, "10"]
    alt_tests_invalid = ["abc"]

    alt_mode_tests_valid = [AltitudeMode.MSL, AltitudeMode.AGL]
    alt_mode_tests_invalid = [0, "123"]
    def test_set_coordinates(self):
        for lat in self.lat_tests_valid + self.lat_tests_invalid:
            for lon in self.lon_tests_valid + self.lon_tests_invalid:
                poi = Poi()
                try:
                    float(lat)
                    float(lon)
                    poi.set_coordinates(
                        lat=lat,
                        lon=lon
                    )
                    self.assertEqual(float(lat), poi.lat)
                    self.assertEqual(float(lon), poi.lon)
                except ValueError:
                    self.assertRaises(
                        ValueError,
                        poi.set_coordinates,
                        lat=lat,
                        lon=lon
                    )

    def test_set_altitude(self):
        poi = Poi()
        for alt in self.alt_tests_valid + self.alt_tests_invalid:
            poi = Poi()
            try:
                float(alt)
                poi.set_altitude(
                    altitude=alt
                )
                self.assertEqual(float(alt), poi.altitude.value)
            except ValueError:
                self.assertRaises(
                    ValueError,
                    poi.set_altitude,
                    altitude=alt
                )

    def test_set_altitude_mode(self):
        poi = Poi()
        for mode in self.alt_mode_tests_valid + self.alt_mode_tests_invalid:
            poi = Poi()
            try:
                AltitudeMode(mode)
                poi.set_altitude_mode(
                    altitude_mode=mode
                )
                self.assertEqual(AltitudeMode(mode), poi.altitude.mode)
            except ValueError:
                self.assertRaises(
                    ValueError,
                    poi.set_altitude_mode,
                    altitude_mode=mode
                )
