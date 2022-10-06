#!/usr/bin/env python

# ROS imports
import rospy
import actionlib
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal


class MoveArm(object):
    
    def __init__(self):
        self.client = actionlib.SimpleActionClient('/play_motion', PlayMotionAction)
        rospy.loginfo("[move_arm][MoveArm] Waiting for server...")
        self.client.wait_for_server()
        rospy.loginfo("[move_arm][MoveArm] Reached server")
    
    def execute(self, motion_name="offer_right"):
        goal = PlayMotionGoal()
        goal.motion_name = motion_name
        goal.skip_planning = False
        goal.priority = 0 
        self.client.send_goal(goal)
        self.client.wait_for_result()
        res = self.client.get_result()
        if res:
            rospy.loginfo("[move_arm][MoveArm] goal success")
        else:
            rospy.logerr("[move_arm][MoveArm] goal error")