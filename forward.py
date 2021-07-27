#coding: utf8

import rospy
from clover import srv
from std_srvs.srv import Trigger
import sys 

def moveforward(n=1):

    rospy.init_node('flight')

    get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
    navigate = rospy.ServiceProxy('navigate', srv.Navigate)
    navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
    set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
    set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
    set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
    set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
    land = rospy.ServiceProxy('land', Trigger)

    # Takeoff and hover 1 m above the ground
    navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)

    # Wait for 3 seconds
    rospy.sleep(3)

    # Fly forward 1 m
    navigate(x=n, y=0, z=0, frame_id='body')

    # Wait for 3 seconds
    rospy.sleep(3)

    # Perform landing
    land()

if __name__=="__main__":
    if len(sys.argv) is 2 and sys.argv[1]<5:
        moveforward(sys.argv[1])
        print("Moving forward ",sys.argv[1]," meters")
    else:    
        moveforward()
        print("Moving forward 1 meter")