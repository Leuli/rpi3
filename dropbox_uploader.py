import sys
import threading
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


class DbxUploadManager(threading.Thread):

    def __init__(self, settings):
        threading.Thread.__init__(self)
        self.dbx = 0
        self.settings = settings

    def setup(self):
        # create dropbox object
        self.dbx = dropbox.Dropbox(self.settings.dbx_auth_token)

        # Check that the access token is valid
        try:
            self.dbx.users_get_current_account()
        except AuthError as err:
            sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    def upload(self, local_file_path, dbx_file_path):
        with open(local_file_path, 'rb') as f:
            try:
                self.dbx.files_upload(f, dbx_file_path, mode=WriteMode('overwrite'))
            except ApiError as err:
                # This checks for the specific error where a user doesn't have
                # enough Dropbox space quota to upload this file
                if (err.error.is_path() and
                        err.error.get_path().error.is_insufficient_space()):
                    sys.exit("ERROR: Cannot back up; insufficient space.")
                elif err.user_message_text:
                    print(err.user_message_text)
                    sys.exit()
                else:
                    print(err)
                    sys.exit()
        print("done uploading")

    def run(self):
        self.setup()
        self.upload("/home/pi/sd_test/1/P1180922.JPG", "/travelpi/P1180922.JPG")


# import sys
# import threading
# import dropbox
# from dropbox.files import WriteMode
# from dropbox.exceptions import ApiError, AuthError
#
#
# def setup(auth_token):
#
#     # create dropbox object
#     dbx = dropbox.Dropbox(auth_token)
#
#     # Check that the access token is valid
#     try:
#         dbx.users_get_current_account()
#     except AuthError as err:
#         sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
#
#     return dbx
#
#
# def upload(dbx, local_file_path, dbx_file_path):
#     with open(local_file_path, 'r') as f:
#         try:
#             dbx.files_upload(f, dbx_file_path, mode=WriteMode('overwrite'))
#         except ApiError as err:
#             # This checks for the specific error where a user doesn't have
#             # enough Dropbox space quota to upload this file
#             if (err.error.is_path() and
#                     err.error.get_path().error.is_insufficient_space()):
#                 sys.exit("ERROR: Cannot back up; insufficient space.")
#             elif err.user_message_text:
#                 print(err.user_message_text)
#                 sys.exit()
#             else:
#                 print(err)
#                 sys.exit()
#     print("done uploading")
