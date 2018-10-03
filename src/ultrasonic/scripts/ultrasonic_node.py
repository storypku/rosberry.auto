#!/usr/bin/env python
# encoding: utf-8
import RPi.GPIO as gpio
import rospy
from ultrasonic.msg import Ultrasonic
from ultrasonic import UltrasonicSensor

class UltrasonicNode:
    def __init__(self, sensor, queue_size=1):
        self.sensor = sensor
        self.pub = rospy.Publisher(
            "ultrasonic", Ultrasonic, queue_size=queue_size)
        self.counter = 0

    def run(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            dist = round(self.sensor.detect_once(), 2)
            self.counter = (self.counter + 1) % 2147483647

            msg = Ultrasonic()
            msg.header.stamp = rospy.Time.now()
            msg.header.frame_id = "ultrasonic-{}".format(self.counter)
            msg.front = dist
            self.pub.publish(msg)
            rate.sleep()

if __name__ == "__main__":
    try:
        rospy.init_node("ultrasonic_node", anonymous=True)
        sensor = UltrasonicSensor(19, 26)
        node = UltrasonicNode(sensor)
        node.run()
    except rospy.ROSInterruptException:
        pass
