from random import sample, choice
from string import ascii_letters


def random_email():
    email = ''
    for _ in range(7):
        letter = sample(choice(ascii_letters), 1)[0]
        email += letter

    email += '@gmail.com'
    return email


def random_string_specific_length(length):
    return ''.join(choice(ascii_letters) for i in range(length))
