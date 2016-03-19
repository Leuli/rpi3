import dropbox


def tues():
    # read dbx token
    with open("/home/pi/dbx_token.txt") as f:
        dbx_token = f.read()

    dbx = dropbox.Dropbox(dbx_token)

    print(dbx.users_get_current_account())
