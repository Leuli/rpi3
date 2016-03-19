import shutil
from copyjob import Copyjob


print("start")

#shutil.copytree("/home/pi/sd_test/1","/home/pi/sd_test/2")

print("ende")

job1 = Copyjob("/home/pi/sd_test/1","/home/pi/sd_test/2")
print(job1.start_job())