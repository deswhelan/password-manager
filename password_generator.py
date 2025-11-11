import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(entry_password):
    letter_count = random.randint(8, 10)
    symbol_count = random.randint(2, 4)
    number_count = random.randint(2, 4)

    char_list = ([random.choice(LETTERS) for _ in range(letter_count)]
                 + [random.choice(SYMBOLS) for _ in range(symbol_count)]
                 + [random.choice(NUMBERS) for _ in range(number_count)])

    random.shuffle(char_list)

    password = ""
    for char in char_list:
      password += char

    entry_password.delete(0, "end")
    entry_password.insert(0, password)