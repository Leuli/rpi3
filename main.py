from time import sleep
from copyjob import Copyjob
import shutil

shutil.rmtree("/home/pi/sd_test/2")
job1 = Copyjob("/home/pi/sd_test/1","/home/pi/sd_test/2")
job1.start()
while job1.is_alive():
    sleep(1)
    print("progress:{}   running:{}".format(job1.get_progress(), job1.is_alive()))

