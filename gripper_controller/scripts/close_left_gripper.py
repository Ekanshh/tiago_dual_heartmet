#!/usr/bin/env python

# ROS imports
import rospy
# Local imports
from gripper_controller import GripperController

rospy.init_node("close_left_gripper")

gripper_right = GripperController('left')
gripper_right.run('close')