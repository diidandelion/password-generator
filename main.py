import random
letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
           'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
           'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
           's', 'S', 't', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
           'X', 'y', 'Y', 'z', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to Password Generator!\n")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
password = ""
password_list = []

for i in range(0, num_letters):
    password_list.append(random.choice(letters))

for i in range(0, num_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, num_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
for char in password_list:
    password += char

print(f"Your password is: {password}")
