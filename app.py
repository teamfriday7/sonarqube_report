from database import get_user
from auth import login
from utils import calculate_discount


PASSWORD = "Admin@123"


def process_user(username, password):

    user = get_user(username)

    if user:
        result = login(username, password)

        if result == True:
            print("Login successful")

            discount = calculate_discount(100)

            print("Discount:", discount)

        else:
            print("Login failed")

    else:
        print("User not found")


def very_complex_function(a,b,c,d,e,f):

    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            return "Everything true"
                        else:
                            return "F false"
                    else:
                        return "E false"
                else:
                    return "D false"
            else:
                return "C false"
        else:
            return "B false"
    else:
        return "A false"


process_user("admin","password")