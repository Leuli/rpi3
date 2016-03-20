from time import sleep
from copyjob import Copyjob
import shutil
from dropbox_uploader import DbxUploadManager
from settings_manager import SettingsMgnr

# initialise settings object (read ini file)
settings = SettingsMgnr()

dbx = DbxUploadManager(settings)
dbx.start()

# weiter: session upload mit DbxUploadManager

# shutil.rmtree("/home/pi/sd_test/2")
# job1 = Copyjob("/home/pi/sd_test/1","/home/pi/sd_test/2")
# # job1.start()
# while job1.is_alive():
#     sleep(1)
#     print("progress:{}   running:{}".format(job1.get_progress(), job1.is_alive()))
#


# with open("/home/pi/dbx_token.txt") as f:
#     dbx_token = f.read()
#
# dbx = DbxUploadManager('')
# dbx.start()
#
# for i in range(0, 10):
#     print("test")
#     sleep(1)





