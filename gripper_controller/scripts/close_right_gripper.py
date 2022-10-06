#!/usr/bin/env python

# ROS imports
import rospy
# Local imports
from gripper_controller import GripperController

rospy.init_node("close_right_gripper")

gripper_right = GripperController('right')
gripper_right.run('close')