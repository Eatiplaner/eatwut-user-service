import random


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
           "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]


def random_email():
    email = ''
    for _ in range(7):
        letter = random.sample(letters, 1)[0]
        email += letter

    email += '@gmail.com'
    return email
