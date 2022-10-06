#!/usr/bin/env python
import rospy
import time

# For gripper control
from gripper_controller import GripperController
from text_to_speech import TextToSpeech

test_gripper_with_speech = True
test_gripper_only = False

rospy.init_node("testing_gripper")

if test_gripper_only:
    rospy.loginfo('[test_gripper] Testing gripper')
    gripper_right = GripperController('right')
    gripper_right.run('open')
    rospy.sleep(1.0)
    gripper_left = GripperController('left')
    gripper_left.run('open')
    rospy.sleep(1.0)
    gripper_right = GripperController('right')
    gripper_right.run('close')
    rospy.sleep(1.0)
    gripper_left = GripperController('left')
    gripper_left.run('close')

if test_gripper_with_speech:
    tts = TextToSpeech()
    rospy.loginfo('[test_gripper] Testing gripper')
    tts.say('Testing gripper')
    rospy.sleep(0.5)
    tts.say('Opening gripper right')
    gripper_right = GripperController('right')
    gripper_right.run('open')
    rospy.sleep(0.5)
    tts.say('Opening gripper left')
    gripper_left = GripperController('left')
    gripper_left.run('open')
    rospy.sleep(0.5)
    tts.say('Closing gripper right')
    gripper_right = GripperController('right')
    gripper_right.run('close')
    rospy.sleep(0.5)
    tts.say('Closing gripper left')
    gripper_left = GripperController('left')
    gripper_left.run('close')
    