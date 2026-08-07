

def calculate_discount(price):

    discount = 0

    if price > 100:
        discount = price * 0.1

    if price > 200:
        discount = price * 0.2

    if price > 300:
        discount = price * 0.3


    return price-discount



def calculate_discount_old(price):

    discount = 0

    if price > 100:
        discount = price * 0.1

    if price > 200:
        discount = price * 0.2

    if price > 300:
        discount = price * 0.3

    return price-discount