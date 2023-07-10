#!/usr/bin/env python3

import rospy
from genpy import Message
from std_msgs.msg import String

class SubscriberBase(rospy.Subscriber):
    def __init__(self, name: str, node: str, data_class: Message):
        rospy.init_node(node, anonymous=True)

        super().__init__(name, data_class, self.callback)

    def callback(self):
        ''' Overload callback for unique return '''
        rospy.loginfo("Hello world")    

