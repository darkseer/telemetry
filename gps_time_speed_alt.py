#!/usr/bin/python

import gps
from subprocess import call
import time
from datetime import datetime, date, time

today = datetime.today()
filename= today.strftime("%Y%m%d%H%M%S")+"_telemetry.dat"
# place at /home/pi/gps_time_speed_alt.py 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


 
while True:
    try:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
        if report['class'] == 'TPV':
            if hasattr(report, 'time') and hasattr(report, 'speed') and hasattr(report, 'alt'):
                output= str(report.time) +","+ str(report.speed * gps.MPS_TO_KPH) +","+ str(report.alt) + "\n"
                print output
                fo = open("/home/pi/"+filename, "a+")
                fo.write( output );
                fo.close

    except KeyError:
		pass
    except KeyboardInterrupt:
		quit()
    except StopIteration:
		session = None
		print "GPSD has terminated"

