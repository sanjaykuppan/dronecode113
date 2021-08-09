#import rospy
#from clover import srv
#from std_srvs.srv import Trigger
import sys 
from geopy import distance
import math
import json
import os.path

class flight:
    def __init__(self) :
        if os.path.isfile("coord.json"):
            file_path=os.path.abspath("")+"\\coord.json"
            file=open(file_path)
            self.data=json.load(file)
            self.a=self.data['a']
            self.b=self.data['b']
            self.c=self.data['c']
            self.d=self.data['d']
            #print(type(self.data['a']['lat']))
    
    def fly():
        
        pass


if __name__=="__main__":
    obj=flight()