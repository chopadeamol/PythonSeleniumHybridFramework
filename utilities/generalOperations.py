import random
import string
import datetime

# def random_generator():
#     random_number = random.randint(100000, 999999)
#     return random_number

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def currentTimestamp():
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return current_time