#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_letter = ""
total_symbol = ""
total_number = ""
for letter in range(1, nr_letters + 1):
    random_letter_index = random.randint(0, len(letters) - 1)
    letter_string = letters[random_letter_index]
    total_letter = total_letter + letter_string
for number in range(1, nr_numbers + 1):
    random_number_index = random.randint(0, len(numbers) - 1)
    number_string = numbers[random_number_index]
    total_number = total_number + number_string
for symbol in range(1, nr_symbols + 1):
    random_symbol_index = random.randint(0, len(symbols) - 1)
    symbol_string = symbols[random_symbol_index]
    total_symbol = total_symbol + symbol_string
password = total_letter + total_symbol + total_number

#Order of characters randomised:
print(''.join(random.sample(password, len(password))))
