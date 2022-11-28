# pylint: skip-file
import os
from unittest import TestCase

from litchi_wp.enums import AltitudeMode, GimbalMode, RotationDirection, ActionType
from litchi_wp.waypoint import Waypoint


class TestWaypoint(TestCase):
    lat_tests_valid = [0, 50.188110, -16.972741, "50.118110"]
    lat_tests_invalid = ["abc"]

    lon_tests_valid = [0, 8.042336, -96.328125, "8.042336"]
    lon_tests_invalid = ["abc"]

    alt_tests_valid = [0, 0.8, 50.53, 100, -5, -5.4, "10"]
    alt_tests_invalid = ["abc"]

    alt_mode_tests_valid = [AltitudeMode.MSL, AltitudeMode.AGL]
    alt_mode_tests_invalid = [0, "123"]

    head_test_valid = [0, 180, 300.35, "300"]
    head_test_invalid = [-180, "abc"]

    curve_test_valid = [0, 3, 5.5, "5.5"]
    curve_test_invalid = [-3, "abc"]

    rot_dir_tests_valid = [RotationDirection.CW, RotationDirection.CCW]
    rot_dir_tests_invalid = [-1, "1", "abc"]

    speed_tests_valid = [-10, -1, 0, 10, 12.35, "5.5"]
    speed_tests_invalid = ["abc"]

    action_type_tests_valid = [
        ActionType.NO_ACTION,
        ActionType.TAKE_PHOTO,
        ActionType.STAY_FOR,
        ActionType.ROTATE_AIRCRAFT,
        ActionType.TILT_CAMERA,
        ActionType.START_RECORDING,
        ActionType.STOP_RECORDING
    ]
    action_type_tests_invalid = ["abc", -1]

    photo_dist_tests_valid = [0, 10.15, "15.4"]
    photo_dist_tests_invalid = ["abc"]

    photo_time_tests_valid = [0, 10.15, "15.4"]
    photo_time_tests_invalid = ["abc"]

    gimbal_mode_tests_valid = [GimbalMode.DISABLED, GimbalMode.FOCUS_POI, GimbalMode.INTERPOLATE]
    gimbal_mode_tests_invalid = [-1, "abc"]

    def assertCoordinate(self, lat_ref, lat_test, lon_ref, lon_test):
        self.assertTrue(self.isNumber(lat_test))
        self.assertTrue(self.isNumber(lon_test))
        self.assertEqual(float(lat_ref), float(lat_test))
        self.assertEqual(float(lon_ref), float(lon_test))

    def isNumber(self, x):
        if isinstance(x, int):
            return True
        if isinstance(x, float):
            return True
        return False

    def test_set_coordinates(self):
        def set_coord():
            try:
                float(lat)
                float(lon)
                waypoint.set_coordinates(lat=lat, lon=lon)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_coordinates, lat=lat, lon=lon)
                return False

        for lat in self.lat_tests_valid + self.lat_tests_invalid:
            for lon in self.lon_tests_valid + self.lon_tests_invalid:
                waypoint = Waypoint(0, 0, 0)
                if set_coord():
                    self.assertCoordinate(
                        lat_ref=lat,
                        lat_test=waypoint.lat,
                        lon_ref=lon,
                        lon_test=waypoint.lon
                    )

    def test_set_altitude(self):
        def set_alt():
            try:
                float(alt)
                AltitudeMode(alt_mode)
                waypoint.set_altitude(alt, alt_mode)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_altitude, value=alt, mode=alt_mode)
                return False

        for alt_mode in self.alt_mode_tests_valid + self.alt_mode_tests_invalid:
            for alt in self.alt_tests_valid + self.alt_tests_invalid:
                waypoint = Waypoint(0, 0, 0)
                if set_alt():
                    self.assertEqual(float(alt), waypoint.altitude.value)
                    self.assertEqual(AltitudeMode(alt_mode), waypoint.altitude.mode)

    def test_set_heading(self):
        def set_head():
            try:
                float(head)
                waypoint.set_heading(head)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_heading, value=head)
                return False

        for head in self.head_test_valid + self.head_test_invalid:
            waypoint = Waypoint(0, 0, 0)
            if set_head():
                self.assertEqual(float(head), waypoint.heading)

    def test_set_curvesize(self):
        def set_curve():
            try:
                float(curve)
                waypoint.set_curvesize(curve)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_curvesize, value=curve)
                return False

        for curve in self.curve_test_valid + self.curve_test_invalid:
            waypoint = Waypoint(0, 0, 0)
            if set_curve():
                self.assertEqual(abs(float(curve)), waypoint.curvesize)
                self.assertGreaterEqual(waypoint.curvesize, 0)

    def test_set_rotation_direction(self):
        def set_head():
            try:
                RotationDirection(rot_dir)
                waypoint.set_rotation_direction(rot_dir)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_rotation_direction, value=rot_dir)
                return False

        for rot_dir in self.rot_dir_tests_valid + self.rot_dir_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            if set_head():
                self.assertEqual(RotationDirection(rot_dir), waypoint.rotationdir)

    def test_set_gimbal(self):
        for gimbal_mode in self.gimbal_mode_tests_valid + self.gimbal_mode_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            for pitch_angle in range(-90, 20):
                try:
                    GimbalMode(gimbal_mode)
                    waypoint.set_gimbal(gimbal_mode, pitch_angle)
                except ValueError:
                    self.assertRaises(
                        ValueError,
                        waypoint.set_gimbal,
                        mode=gimbal_mode,
                        pitchangle=pitch_angle
                    )

    def test_set_speed_ms(self):
        def set_speed():
            try:
                waypoint.set_speed_ms(speed)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_speed_ms, value=speed)
                return False

        for speed in self.speed_tests_valid + self.speed_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            if set_speed():
                self.assertEqual(float(speed), waypoint.speed)

    def test_set_speed_kmh(self):
        def set_speed():
            try:
                waypoint.set_speed_kmh(speed)
                return True
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_speed_kmh, value=speed)
                return False

        for speed in self.speed_tests_valid + self.speed_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            if set_speed():
                self.assertEqual(float(speed) / 3.6, waypoint.speed)

    def test_set_poi(self):
        for lat in self.lat_tests_valid + self.lat_tests_invalid:
            for lon in self.lon_tests_valid + self.lon_tests_invalid:
                for alt in self.alt_tests_valid + self.alt_tests_invalid:
                    for alt_mode in self.alt_mode_tests_valid + self.alt_mode_tests_invalid:
                        waypoint = Waypoint(0, 0, 0)
                        try:
                            float(lat)
                            float(lon)
                            float(alt)
                            AltitudeMode(alt_mode)
                            waypoint.set_poi(
                                lat=lat,
                                lon=lon,
                                alt=alt,
                                alt_mode=alt_mode
                            )
                            self.assertEqual(float(lat), waypoint.poi.lat)
                            self.assertEqual(float(lon), waypoint.poi.lon)
                            self.assertEqual(float(alt), waypoint.poi.altitude.value)
                            self.assertEqual(AltitudeMode(alt_mode), waypoint.poi.altitude.mode)
                        except ValueError:
                            self.assertRaises(
                                ValueError,
                                waypoint.set_poi,
                                lat=lat,
                                lon=lon,
                                alt=alt,
                                alt_mode=alt_mode
                            )


    def test_set_photo_interval_time(self):
        for time in self.photo_time_tests_valid + self.photo_time_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            try:
                float(time)
                waypoint.set_photo_interval_time(time)
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_photo_interval_time, seconds=time)

    def test_set_photo_interval_distance(self):
        for dist in self.photo_dist_tests_valid + self.photo_dist_tests_invalid:
            waypoint = Waypoint(0, 0, 0)
            try:
                float(dist)
                waypoint.set_photo_interval_distance(dist)
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_photo_interval_distance, meters=dist)

    def test_replace_action(self):
        waypoint = Waypoint(0, 0, 0)
        for i in range(15):
            waypoint.replace_action(i, ActionType.NO_ACTION, 0)
        self.assertRaises(IndexError, waypoint.replace_action, -1, ActionType.NO_ACTION, 0)
        self.assertRaises(IndexError, waypoint.replace_action, 15, ActionType.NO_ACTION, 0)

    def test_set_action(self):
        waypoint = Waypoint(0, 0, 0)
        for a_type in self.action_type_tests_valid + self.action_type_tests_invalid:
            try:
                ActionType(a_type)
                waypoint.set_action(a_type, 0)
            except ValueError:
                self.assertRaises(ValueError, waypoint.set_action, a_type, 0)
        waypoint = Waypoint(0, 0, 0)
        for i in range(15):
            self.assertEqual(i, waypoint.set_action(ActionType.NO_ACTION, 0))
        self.assertEqual(-1, waypoint.set_action(ActionType.NO_ACTION, 0))


    def test_get_header(self):
        self.assertEqual(
            'latitude,longitude,altitude(m),heading(deg),curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,actiontype1,actionparam1,actiontype2,actionparam2,actiontype3,actionparam3,actiontype4,actionparam4,actiontype5,actionparam5,actiontype6,actionparam6,actiontype7,actionparam7,actiontype8,actionparam8,actiontype9,actionparam9,actiontype10,actionparam10,actiontype11,actionparam11,actiontype12,actionparam12,actiontype13,actionparam13,actiontype14,actionparam14,actiontype15,actionparam15,altitudemode,speed(m/s),poi_latitude,poi_longitude,poi_altitude(m),poi_altitudemode,photo_timeinterval,photo_distinterval\n',
            Waypoint.get_header()
        )

    def test_to_line(self):
        line = '21.2568609,-157.8071047,100.0,180.0,0.0,0,0,0.0,0,1500,1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,1,15.0,0.0,0.0,0.0,0,-1.0,-1.0\n'
        waypoint = Waypoint.from_line(line)
        line_split = line.split(',')
        line2_split = waypoint.to_line().split(',')
        self.assertEqual(line_split, line2_split)

    def test_from_line(self):
        self.test_to_line()

    def test_from_file(self):
        filename = os.path.join(os.path.dirname(__file__), 'waypoints.csv')
        waypoints = Waypoint.from_file(filename)
        content_waypoints = Waypoint.get_header()
        for waypoint in waypoints:
            content_waypoints += waypoint.to_line()
        with open(filename, mode='r', encoding='utf-8') as file:
            content_file = file.read()
            self.assertEqual(content_file, content_waypoints)
