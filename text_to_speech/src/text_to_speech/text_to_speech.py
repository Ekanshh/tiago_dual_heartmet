#import ROS headers
import rospy
import actionlib

#import PAL Robotics custom headers
from pal_interaction_msgs.msg import TtsAction, TtsGoal

class TextToSpeech(object):
    
    def __init__(self):
        self.client = actionlib.SimpleActionClient('tts', TtsAction)
        rospy.loginfo("[text_to_speech][TextToSpeech] Waiting for server...")
        self.client.wait_for_server()
        rospy.loginfo("[text_to_speech][TextToSpeech] Reached server")
    
    def say(self, text):
        goal = TtsGoal()
        goal.rawtext.text = text
        goal.rawtext.lang_id = "en_GB"
        self.client.send_goal(goal)
        self.client.wait_for_result()
        res = self.client.get_result()
        if res:
            rospy.loginfo("[text_to_speech][TextToSpeech] goal success")
        else:
            rospy.logerr("[text_to_speech][TextToSpeech] goal error")
