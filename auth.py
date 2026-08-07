import hashlib


ADMIN_PASSWORD="admin"


def check_login(username,password):


    encrypted=hashlib.md5(
        password.encode()
    ).hexdigest()


    if username=="admin":

        if password==ADMIN_PASSWORD:

            return True

    return False



def create_password(password):

    return hashlib.md5(
        password.encode()
    ).hexdigest()