#!/usr/bin/env python3
from __future__ import print_function
import sys
import math
import numpy as np

#ROS Imports
import rospy
from sensor_msgs.msg import Image, LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

# This node is very silly, it drives just against the wall!
# But it might be useful for testing the emergency brake node...

class silly:
    def __init__(self):
        lidarscan_topic = '/scan'
        drive_topic = '/nav'
        self.last_steer = 0
        self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback)
        self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size=1)

    def lidar_callback(self, data):
        drive_msg = AckermannDriveStamped()
        drive_msg.header.stamp = rospy.Time.now()
        drive_msg.header.frame_id = "laser"
        drive_msg.drive.speed = 0.3
        drive_msg.drive.steering_angle = 0
        self.drive_pub.publish(drive_msg)

def main(args):
    rospy.init_node("silly_node", anonymous=True)
    rfgs = silly()
    rospy.sleep(0.1)
    rospy.spin()

if __name__ == '__main__':
    main(sys.argv)

