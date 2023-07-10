#!/usr/bin/env python3

import rospy
from genpy import Message

class PublisherBase(rospy.Publisher):
    def __init__(self, data_class: Message, name: str, node: str, f: float, queue_size: int, **kwargs):
        assert f > 0.0
        self.packet = data_class()

        super().__init__(
            name = name,
            data_class = data_class,
            queue_size = queue_size,
            **kwargs
        )

        rospy.init_node(node)

        self.rate = rospy.Rate(f)
        
    def run(self):
        while not rospy.is_shutdown():
            # abstract method to prepare packet
            packet_ready = self.prepare_packet()

            if packet_ready:
                # publish packet
                self.publish(self.packet)

            # enforce publish frequency
            self.rate.sleep()

    def initialize_packet(self):
        raise NotImplementedError

    def prepare_packet(self) -> bool:
        assert isinstance(self.packet, self.data_class)