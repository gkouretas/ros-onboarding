#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('velocity_commands', Twist, queue_size=10)
    rospy.init_node('commander', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist = Twist()

        twist.linear.x = 10

        rospy.loginfo(twist)
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
