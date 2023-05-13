import random
import string

def password_generator(lenght):
    all_chars = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choices(all_chars, k=lenght), all_chars.split(" "))
    print(password)

password_generator(8)

