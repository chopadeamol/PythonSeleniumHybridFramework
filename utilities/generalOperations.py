import random
import string

# def random_generator():
#     random_number = random.randint(100000, 999999)
#     return random_number

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))