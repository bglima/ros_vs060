#!/usr/bin/env python
import rospy
from control_msgs.msg import FollowJointTrajectoryActionGoal
from geometry_msgs.msg import Twist
from mousepos import mousepos

# Init a new node
rospy.init_node('bruno_turtle_commander')

# Create a publisher which will send messages
pub = rospy.Publisher('/arm_controller/position_trajectory_controller/follow_joint_trajectory/goal', Twist)

# Create a message of type geometry_msgs/Twist, which has:
#
# geometry_msgs/Vector3 linear
#  float64 x
#  float64 y
#  float64 z
#geometry_msgs/Vector3 angular
#  float64 x
#  float64 y
#  float64 z
state = FollowJointTrajectoryActionGoal()

rate = rospy.Rate(5)  # Create a frequency rate for message to be published

# Main loop
while not rospy.is_shutdown():
    mouse_x, mouse_y = mouseFromCenter()
    state.angular.z, state.linear.x = normAndCenter( mouse_x, mouse_y )
    
    if abs( state.linear.x ) < maxval[0] * 0.05:
        state.linear.x = 0
    if abs( state.angular.z ) < maxval[1] * 0.05:
        state.angular.z = 0
        
    pub.publish(state)
    rate.sleep()

