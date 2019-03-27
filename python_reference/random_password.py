import random

def random_password():
    a = ""

    for i in range(30):
        a += chr(random.randint(32,126))

    return a


word = random_password()
print(word)
