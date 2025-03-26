import random
import string

english_alphabet = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
)

def generate_postcode():
    return random.randint(1000000000, 9999999999)

def generate_firstname(postcode):
    postcode_str = str(postcode)
    numparts = [postcode_str[i:i+2] for i in range(0, len(postcode_str), 2)]
    firstname = list()

    for i in numparts:
        firstname.append(english_alphabet[int(i)%25])
    return "".join(firstname)

def generate_random_string(length):
    characters = string.ascii_letters
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


class Client:
    def __init__(self):
        self.postcode = generate_postcode()
        self.first_name = generate_firstname(self.postcode)
        self.second_name = generate_random_string(random.randint(1,15))
