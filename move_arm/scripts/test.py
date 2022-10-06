#!/usr/bin/env python


import rospy
from move_arm import MoveArm
from text_to_speech import TextToSpeech


rospy.init_node("test_move_arm", anonymous=True)
rospy.loginfo("Testing move arm")

tts = TextToSpeech()
tts.say("Handing over the object to the nearest person")
arm = MoveArm()
arm.execute()
rospy.sleep(1.0)
tts.say("Moving arm back to home position")
arm.execute(motion_name="home_right")
rospy.sleep(1.0)

