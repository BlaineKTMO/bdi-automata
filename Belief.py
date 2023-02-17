import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan

# Can use this to have a consistent realtime beliefSet as a node
# BDI would then contact this node to refresh its BDI

odomName = "/odom"
gwptName = "/gwpt"
laneCallbackName = "/img_to_laser/LaneScan"
laneFollowCallbackName = "/lane_scan_frame"

class Belief():
    def __init__(self, beliefSet = {}):
        self.beliefSet = {
            "ready" : True,
            "goal_in_local" : False,
            "lanes" : False,
            "lidar_feed" : False,
            "camera_feed" : False,
            "gps_feed" : False,
            "is_moving" : False,
            "obstacles" : False,
            "dead_man" : False,
            "heading_gwpt" : False,
            "heading_iwpt" : False,
            "goals_complete" : False,
            "at_iwpt" : False,
            "at_gwpt" : False
        }

        self.odomSub = rospy.Subscriber(odomName, Odometry, self.odomCallback)
        self.gwptSub = rospy.Subscriber(gwptName, PoseStamped, self.gwptCallback)
        self.laneSub = rospy.Subscriber(laneCallbackName, LaserScan, self.laneCallback)
        self.laneFollowSub = rospy.Subscriber(laneFollowCallbackName, PoseStamped, self.laneFollowCallback)
        self.lidarSub = rospy.Subscriber(lidarName, PoseStamped, self. lidarCallback)
        self.gpsSub = rospy.Subscriber(gpsName, Odometry, self.gpsCallback)
        self.iwptSub = rospy.Subscriber(iwptName, PoseStamped, self.iwptCallback)

    def odomCallback(msg):
        pass

    def gwptCallback(msg):
        pass

    def laneCallback(msg):
        pass
    
    def lidarCallback(msg):
        pass

    def gpsCallback(msg):
        pass

    def isMoving(msg):
        pass

    def costmapCallback(msg):
        pass

    def iwptCallback(msg):
        pass

    def laneFollowCallback(msg):
        pass


if __name__ == '__main__':
    rospy.init_node('')
