#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
import std_msgs.msg
import actionlib_msgs.msg
from mousepos import mouseFromCenter
from control_msgs.msg import FollowJointTrajectoryActionGoal
from geometry_msgs.msg import Pose, PoseStamped, Point, Quaternion
from moveit_commander import MoveGroupCommander, conversions
from tf.transformations import quaternion_from_euler
from math import pi

# Init a new node
rospy.init_node('bruno_arm_commander')
arm = MoveGroupCommander("manipulator")

# Use rospy.Rate for frequency. Use rospy.Duration for period
rate = rospy.Rate(1)


while not rospy.is_shutdown():
    mouse_x, mouse_y = mouseFromCenter()
    
    point = Point( 0.4 + mouse_y, \
                   0.0 + mouse_x, \
                   0.4 + random.uniform(-0.05, 0.05) )
    
    orient = Quaternion(  0, 0.7071,  0.7071, 0)                   
    
    pose = PoseStamped( header = rospy.Header(stamp = rospy.Time.now(), frame_id = '/BASE'), \
                        pose = Pose(position = point, orientation = orient) \
                      )
                        
    print ' [SYS] Executing current pose: \n', pose, '\n'
    arm.set_pose_target(pose)
    arm.go(True)
    rate.sleep()    

moveit_commander.roscpp_shutdown()