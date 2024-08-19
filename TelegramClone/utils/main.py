import random


def send_code():
    code = str(random.randrange(100_000 , 1_000_000))
    with open('/home/dilshod/PycharmProjects/TelegramClone/phone_number.txt' , 'w') as f:
        f.write(code)

    return code


