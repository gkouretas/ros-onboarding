#!/usr/bin/env python3

import rospy

from include.Subscriber import SubscriberBase
from pub_sub.msg import Random

class RandomSubscriber(SubscriberBase):
    def __init__(self, data_class: Random, name: str, node: str):
        super().__init__(name, node, data_class)

    def callback(self, data: Random):
        msg = f'''
        ID: {rospy.get_caller_id()}
        Activity: {data.activity}
        Value: {data.random_value}
        '''
        rospy.loginfo(msg)

if __name__ == "__main__":
    subscriber = RandomSubscriber(
        data_class = Random,
        name = "random",
        node = "sub_node"
    )

    rospy.spin()
