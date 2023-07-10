#!/usr/bin/env python3

import rospy
import random

from include.Publisher import PublisherBase
from pub_sub.msg import Random

class RandomPublisher(PublisherBase):
    def __init__(self, data_class: Random, name: str, node: str, f: float, queue_size: int, **kwargs):
        super().__init__(data_class, name, node, f, queue_size, **kwargs)

    def prepare_packet(self) -> bool:
        if isinstance(self.packet, Random):
            self.packet.random_value = random.random() * 10.0
            self.packet.activity = "active" if self.packet.random_value < 5 else "inactive"

            rospy.loginfo(self.packet)

            return True

        else:
            return False

if __name__ == "__main__":
    publisher = RandomPublisher(
        data_class = Random,
        name = "random",
        node = "pub_node",
        f = 20.0,
        queue_size = 1
    )

    publisher.run()