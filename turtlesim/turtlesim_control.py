# turtlesim_control.py

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    """
    Controls the movement of the turtlesim node.
    """
    rospy.init_node('turtle_controller', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    vel_msg = Twist()
    vel_msg.linear.x = 2.0  # Move forward
    vel_msg.angular.z = 1.0  # Rotate

    while not rospy.is_shutdown():
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
