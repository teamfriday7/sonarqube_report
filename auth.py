
import hashlib


def login(username,password):

    encrypted = hashlib.md5(
        password.encode()
    ).hexdigest()


    if encrypted:

        return True

    return False



def check_password(password):

    if len(password)<5:
        return False

    else:
        return True