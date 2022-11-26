## [2.1.0] - 2022-11-26
 
### Migration
#### 2.0.0 -> 2.1.0
- No changes needed.
 
### Added
- typing stubs


## [2.0.0] - 2022-11-20
 
### Migration
#### 1.x.x -> 2.0.0
- waypoint.set_action changed
  - old: waypoint.set_action(index=x, actiontype=y, param=z)
  - new: waypoint.set_action(action_type=y, param=z)
- to set specific action index use
  - waypoint.replace_action(index=x, action_type=y, param=z)
 
### Added

#### Waypoint

- internal action index handling
  - waypoint.set_action returns False if all action slots are full
 
### Changed
 
#### Waypoint

- waypoint.set_action parameter actiontype changed to action_type
  - old: waypoint.set_action(index=x, actiontype=y, param=z)
  - new: waypoint.set_action(action_type=y, param=z)


## [1.1.1] - 2022-11-20
 
### Migration
#### 1.1.0 -> 1.1.1
- No changes needed.
 
### Fixed

- Regex filter errors
  - did not allow negative latitude
  - did not allow some photo interval values
 
 
## [1.1.0] - 2022-11-17
 
### Migration
#### 1.0.x -> 1.1.0
- No changes needed.
 
### Added
#### Waypoint

- Method from_line to parse a line from a litchi csv file.
- Method from_file to parse a litchi csv file.

 
### Changed
 
- Switched docstrings to Google style.

### Fixed

- Typos in the documentation.
 