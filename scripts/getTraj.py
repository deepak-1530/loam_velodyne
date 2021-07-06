# subscribe to odometry topic /integrated_to_init

import rospy
from nav_msgs.msg import Odometry
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

trajectory =  Path()
trajPub = rospy.Publisher("/slamTrajectory", Path, queue_size=1)

def odomCb(msg):
    print(msg.pose.pose.position)
    p = PoseStamped()
    trajectory.header.frame_id = msg.header.frame_id
    trajectory.header.stamp = rospy.Time.now()
    p.pose.position = msg.pose.pose.position
    p.pose.orientation = msg.pose.pose.orientation
    print(p)
    trajectory.poses.append(p)
    trajPub.publish(trajectory)
    
if __name__=="__main__":
    rospy.init_node("trajectory_node")
    print("Here")
    odomSub = rospy.Subscriber("/integrated_to_init", Odometry, odomCb)
    rospy.spin()    

