#!/usr/bin/env python3

import rospy
import math

from include.Subscriber import SubscriberBase
from ros_practice.msg import Random

class RandomSubscriber(SubscriberBase):
    def __init__(self, data_class: Random, name: str, node: str):
        super().__init__(name, node, data_class)

    def callback(self, data: Random):
        if data.activity == "active":
            rospy.loginfo(msg = f"{math.log10(data.random_value)}")

if __name__ == "__main__":
    subscriber = RandomSubscriber(
        data_class = Random,
        name = "random",
        node = "sub_node"
    )

    rospy.spin()
