from subprocess import call
import time
from datetime import datetime, date, time
today = datetime.today()
filename= today.strftime("%Y%m%d%H%M%S")
print filename
call(["raspivid","-t","0","-o","skycast_"+filename+".mp4"])
