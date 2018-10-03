# rosberry.auto

A self-driving car powered both by Raspberry PI and ros.

## Build
```
cd rosberry.auto
catkin_make 
```

## Run
```
source devel/setup.bash
rosrun ultrasonic ultrasonic_node.py
```

## Hardware

- Raspberry PI (2B/3B/3B+)
- HC-04/US-015 Ultrasonic sensor (Trig->GPIO19, Echo->GPIO26)
- L298N Dual H-Bridge Motor Driver
- 4-wheeled robot chassis

