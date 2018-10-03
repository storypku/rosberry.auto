#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as gpio
import rospy

from ultrasonic import PassFilter
# TRIG_PORT=19
# ECHO_PORT=26

class UltrasonicSensor:
    def __init__(self, trig_port, echo_port, threshold=200.0, alpha=1.0):
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(trig_port, gpio.OUT)
        gpio.setup(echo_port, gpio.IN)

        self.trig_port = trig_port
        self.echo_port = echo_port
        self.keeper = PassFilter(threshold, alpha)

        gpio.output(trig_port, gpio.LOW)
        rospy.sleep(0.1)

    
    def detect_once(self):
        gpio.output(self.trig_port, gpio.HIGH)
        rospy.sleep(0.000010) # 10ms
        gpio.output(self.trig_port, gpio.LOW)

        pulse_start = 0
        pulse_stop = 0

        while gpio.input(self.echo_port) == 0:
            pulse_start = rospy.Time.now()

        while gpio.input(self.echo_port) == 1:
            pulse_stop = rospy.Time.now()

        duration = pulse_stop - pulse_start

        distance = duration.to_sec() * 17150 # 343.0 m/s
        distance = self.keeper.filter(distance)
        return distance

    def __del__(self):
        gpio.cleanup()

