import configparser
import os.path

class SettingsMgnr:

    def __init__(self):
        self.dbx_auth_token = ""
        self.dbx_local_path = ""
        self.dbx_remote_path = ""
        self.cfgparser = configparser.ConfigParser()

        if os.path.isfile("/home/pi/travelpi_cfg.ini"):
            #config = configparser.ConfigParser()
        else:



    def new_settings(self):

        # read settings from cli
        self.dbx_auth_token = input("Enter dropbox auth token:")
        self.dbx_local_path = input("Enter your local TravelPi backup path:")
        self.dbx_remote_path = input("Enter your TravelPi backup folder in your Dropbox:")

        # create ini file
        cfgfile = open("/home/pi/travelpi_cfg.ini")         # todo: what happens if file already exists? E.g. new settings
