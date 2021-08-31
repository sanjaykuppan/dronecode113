from flask import Flask
import flask
from flask.globals import request
import rospy
from clover import srv
from std_srvs.srv import Trigger

import mavros
from mavros import command
mavros.set_namespace()

app = Flask(__name__)

rospy.init_node('bee',anonymous=True)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
    
@app.route('/',methods=['GET','POST'])
def home():
    return "Welcome to Test flask app!!"

@app.route('/tell',methods=['GET','POST'])
def get_tel():
    print("Entering telemetry definition")
    a=get_telemetry()
    return str(a)

@app.route('/arm',methods=['GET','POST'])
def arm():
    print("Entering arm definition")
    command.arming(True)
    return "armed"


if __name__ == '__main__':
    print("starting flask app, rospy init completed")
    app.run(debug=True,host="192.168.11.1",port='5000')