#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from mousepos import mousepos

# Init a new node
rospy.init_node('bruno_turtle_commander')

# Create a publisher which will send messages
pub = rospy.Publisher('turtle1/cmd_vel', Twist)

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
state = Twist()

dim = [2560.0, 1080.0] # Display dimensions X and Y
half = [ x * 0.5 for x in dim ] # Half of display dimensions
maxval = [15.0, 10.0] # Max value for linear and angular velocity 

rate = rospy.Rate(5)  # Create a frequency rate for message to be published

# Functions that transforms mouse coordinates from display to centered maxval space
def normAndCenter( pos_x, pos_y ):
    pos = [pos_x, pos_y]    
    tf = [ -maxval[i] * (pos[i] - half[i]) / half[i] for i in range(2) ]
    return tf[0], tf[1]

# Main loop
while not rospy.is_shutdown():
    mouse_x, mouse_y = mousepos()
    state.angular.z, state.linear.x = normAndCenter( mouse_x, mouse_y )
    
    if abs( state.linear.x ) < maxval[0] * 0.05:
        state.linear.x = 0
    if abs( state.angular.z ) < maxval[1] * 0.05:
        state.angular.z = 0
        
    pub.publish(state)
    rate.sleep()

