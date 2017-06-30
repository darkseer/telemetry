#!/usr/bin/python

from subprocess import call
import time
from datetime import datetime, date, time
today = datetime.today()
filename= today.strftime("%Y%m%d%H%M%S")
print filename
call(["raspivid","-t","0","-o","/home/pi/"+filename+"_skycast.mp4"])
