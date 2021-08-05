#coding: utf8

import rospy
from clover import srv
from std_srvs.srv import Trigger
import sys 
from geopy import distance
import math

def movepos(ini,fin):

    rospy.init_node('flight')

    get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
    navigate = rospy.ServiceProxy('navigate', srv.Navigate)
    navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
    set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
    set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
    set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
    set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
    land = rospy.ServiceProxy('land', Trigger)

    if not math.isnan(get_telemetry().lat):
        dp=(get_telemetry().lat,get_telemetry().lon)
        if int(distance.distance(dp,ini).m) <5:
            # Takeoff and hover 1 m above the ground
            navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
            print("Takeoff complete")
            # Wait for 3 seconds
            rospy.sleep(5)
            # Fly forward to A point
            navigate_global(lat=ini[0], lon=ini[1], z=0, speed=0.5, frame_id='body')
            print("Reached point A")
            # Wait for 3 seconds
            rospy.sleep(3)
            #fly to point B
            navigate_global(lat=fin[0], lon=fin[1], z=0, speed=0.5, frame_id='body')
            print("Reached point B")
            #wait
            rospy.sleep(2)
            # Perform landing
            land()
            print("land completed")
        else:
            print("Move drone closer to A point and try again!!")
    else:
        print("GPS unavailable!! Try again once GPS is available!!")

if __name__=="__main__":
    if len(sys.argv) is 5 :
        a=(float(sys.argv[1]),float(sys.argv[2]))
        b=(float(sys.argv[3]),float(sys.argv[4]))
        d=int(distance.distance(a,b).m)
        if d<10:
            print("Moving from point A to point B ")
            movepos(a,b)
        else:
            print("Distance more than 10m")
    else:    
        print("required parameters not provided")