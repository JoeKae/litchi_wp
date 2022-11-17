# litchi_wp 1.1.0

 Python package to handle litchi csv waypoints

## Examples:

### Create Waypoint in your code

```python
from litchi_wp.waypoint import Waypoint
from litchi_wp.enums import ActionType, AltitudeMode

wp = Waypoint(lat=-21.360244, lon=-64.85657, alt=100)  # minimal waypoint setup
wp.set_altitude(value=100, mode=AltitudeMode.AGL)  # set altitude above ground
wp.set_speed_ms(value=0.1)  # stop movement (0 sets cruise speed, so this is the best we can get)
wp.set_action(index=0, actiontype=ActionType.TILT_CAMERA, param=-90)  # tilt gimbal for nadir shot
wp.set_action(index=1, actiontype=ActionType.STAY_FOR, param=1000)  # wait 1 second to stabilize
wp.set_action(index=2, actiontype=ActionType.TAKE_PHOTO)  # take the photo

output = wp.get_header()  # first line for the waypoint file needs to be the header
output += wp.to_line()  # adds the waypoint to the output
print(output)  # check the result
```
```
latitude,longitude,altitude(m),heading(deg),curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,actiontype1,actionparam1,actiontype2,actionparam2,actiontype3,actionparam3,actiontype4,actionparam4,actiontype5,actionparam5,actiontype6,actionparam6,actiontype7,actionparam7,actiontype8,actionparam8,actiontype9,actionparam9,actiontype10,actionparam10,actiontype11,actionparam11,actiontype12,actionparam12,actiontype13,actionparam13,actiontype14,actionparam14,actiontype15,actionparam15,altitudemode,speed(m/s),poi_latitude,poi_longitude,poi_altitude(m),poi_altitudemode,photo_timeinterval,photo_distinterval
-21.360244,-64.85657,100,180,0,0,0,0,5,-90,0,1000,1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,1,0.1,0,0,0,0,-1.0,-1.0
```

### Create Waypoints from litchi csv file

```python
from litchi_wp.waypoint import Waypoint
filename = '/home/user/file.csv'
waypoints = Waypoint.from_file(filename)
"""
Now waypoints contains a list of all the waypoint objects created from parsing the file
"""
```

## See the docs for all the options:

- [Waypoint](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/waypoint.html)
- [Action](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/action.html)
- [Altitude](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/altitude.html)
- [Enums](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/enums.html)
- [Gimbal](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/gimbal.html)
- [Photo](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/photo.html)
- [Poi](https://htmlpreview.github.io/?https://raw.githubusercontent.com/JoeKae/litchi_wp/main/docs/litchi_wp/waypoint.html)