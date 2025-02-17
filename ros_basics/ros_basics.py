# ros_basics.py

import rospy
from std_msgs.msg import String

def talker():
    """
    Basic ROS publisher node.
    """
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        message = "Hello ROS!"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
