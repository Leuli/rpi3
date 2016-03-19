import dropbox


def tues():
    # read dbx token
    with open("/home/pi/dbx_token.txt") as f:
        dbx_token = f.read()

    # connect dropbox account
    dbx = dropbox.Dropbox(dbx_token)
    dbx.users_get_current_account()

    for entry in dbx.files_list_folder('').entries:
        print(entry.name)

def upload(localfile, backuppath):
