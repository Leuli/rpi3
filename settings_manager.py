import configparser
import os.path

class SettingsMgnr:

    def __init__(self):
        self.dbx_auth_token = ""
        self.dbx_local_path = ""
        self.dbx_remote_path = ""


        if os.path.isfile("/home/pi/travelpi_cfg.ini"):
            #config = configparser.ConfigParser()
            pass
        else:
            self.new_settings()


    def new_settings(self):

        # read settings from cli
        self.dbx_auth_token = input("Enter dropbox auth token:")
        self.dbx_local_path = input("Enter your local TravelPi backup path:")
        self.dbx_remote_path = input("Enter your TravelPi backup folder in your Dropbox:")

        # write ini file
        cfgparser = configparser.ConfigParser()
        cfgfile = open("/home/pi/travelpi_cfg.ini", 'w')         # todo: what happens if file already exists? E.g. new settings
        cfgparser.add_section('DropboxSettings')
        cfgparser.set('DropboxSettings', 'dbx_auth_token', self.dbx_auth_token)
        cfgparser.set('DropboxSettings', 'dbx_local_path', self.dbx_local_path)
        cfgparser.set('DropboxSettings', 'dbx_remote_path', self.dbx_remote_path)
        cfgparser.write(cfgfile)
        cfgfile.close()
