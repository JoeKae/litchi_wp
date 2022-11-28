# pylint: skip-file
from unittest import TestCase

from litchi_wp.photo import Photo


class TestPhoto(TestCase):
    time_tests_valid = [-1, 0, 10, 20.4, "4.5"]
    time_tests_invalid = ["abc"]

    distance_tests_valid = [-1, 0, 10, 20.4, "4.5"]
    distance_tests_invalid = ["abc"]

    def test_set_time_interval(self):
        for t in self.time_tests_valid + self.time_tests_invalid:
            photo = Photo()
            try:
                float(t)
                photo.set_time_interval(t)
                self.assertEqual(float(t), photo.time_interval)
                self.assertEqual(float(0), photo.distance_interval)
            except ValueError:
                self.assertRaises(ValueError, photo.set_time_interval, interval=t)

    def test_set_distance_interval(self):
        for d in self.distance_tests_valid + self.distance_tests_invalid:
            photo = Photo()
            try:
                float(d)
                photo.set_distance_interval(d)
                self.assertEqual(float(d), photo.distance_interval)
                self.assertEqual(float(0), photo.time_interval)
            except ValueError:
                self.assertRaises(ValueError, photo.set_distance_interval, interval=d)
