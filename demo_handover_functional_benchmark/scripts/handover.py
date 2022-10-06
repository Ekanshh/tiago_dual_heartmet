#!/usr/bin/env python

# ROS imports
import rospy
from geometry_msgs.msg import WrenchStamped
# Local imports
from move_arm import MoveArm
from gripper_controller import GripperController
from text_to_speech import TextToSpeech
import numpy as np
import argparse

class HandOver(object):
    
    def __init__(self, gripper_side="right"):
        rospy.init_node("hand_over", anonymous=True)
        self.tts = TextToSpeech()
        self.arm = MoveArm()
        self.gripper = GripperController(gripper_side)
        self.wrench = None
        self.initial_wrench = None
        self.is_grasped = False
        self.wrist_ft_sub = rospy.Subscriber("/wrist_right_ft", WrenchStamped, self.get_wrench_data)
        parser = argparse.ArgumentParser()
        parser.add_argument('--name', required=True)
        parser.add_argument('--object', required=True)
        self.args = parser.parse_args()
        rospy.sleep(1.0)
    
    def run(self):    
        time_start = rospy.Time.now()
        self.initial_wrench = self.record_initial_wrench()
        self.tts.say("Hello {args.name}! I will handover the {args.object} to you".format(args=self.args))
        self.arm.execute()
        rospy.sleep(1.0)
        self.tts.say("Please take it.")
        while not self.is_grasped:
            self.is_grasped = self.check_grasp()
            time_current=rospy.Time.now()
            if self.is_grasped and (time_current-time_start).to_sec() < 20:
                # self.tts.say("Thank you for grasping the object")
                rospy.sleep(0.5)
                # self.tts.say("I will release the object now")
                self.gripper.run("open")
                rospy.sleep(1.0)
                # self.tts.say("I will move my arm back now")
                self.arm.execute(motion_name="home_right")
            elif (time_current-time_start).to_sec() > 20:
                self.tts.say("Looks like you don't want the {args.object}".format(args=self.args))
                rospy.sleep(1.0)
                self.arm.execute(motion_name="home_right")
                break
            else:
                continue
                    
    def check_grasp(self):
        wrench = rospy.wait_for_message('/wrist_right_ft', WrenchStamped, timeout=5)
        rospy.loginfo("Wrench Corrected: %s", wrench.wrench.force.z)
        if (abs(wrench.wrench.force.z - self.initial_wrench)) > 10.0:
                return True
    
    def record_initial_wrench(self):
        wrenches = []
        for i in range(20):
            wrenches.append(self.wrench.wrench.force.z)
            rospy.loginfo("Recording initial wrench: %s", self.wrench.wrench.force.z)
        initial_wrench = np.mean(wrenches)
        rospy.loginfo("Initial wrench: %s", initial_wrench)
        return initial_wrench
            
    def get_wrench_data(self, msg):
        self.wrench = msg

if __name__ == '__main__':
    hand_over = HandOver()
    hand_over.run()
    rospy.spin()