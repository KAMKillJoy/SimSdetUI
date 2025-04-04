"""
Модуль для создания данных нового клиента с данными:
- postcode
- firstname
- secondname
"""

import random
import string

english_alphabet = list(string.ascii_lowercase)


class Client:
    def __init__(self):
        self.postcode = self.__generate_postcode()
        self.first_name = self.__generate_firstname(self.postcode)
        self.last_name = self.__generate_random_string(random.randint(1, 15))

    def __generate_postcode(self):
        return random.randint(1000000000, 9999999999)

    def __generate_firstname(self, postcode):
        postcode_str = str(postcode)
        numparts = [postcode_str[i:i + 2] for i in range(0, len(postcode_str), 2)]
        firstname = list()

        for i in numparts:
            firstname.append(english_alphabet[int(i) % 25])
        return "".join(firstname)

    def __generate_random_string(self, length):
        characters = string.ascii_letters
        random_string = ''.join(random.choices(characters, k=length))
        return random_string
