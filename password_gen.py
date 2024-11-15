import random

password_length = int(input("Enter your desired password length: "))

character = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(_)+=-*/"

password = []

for i in range(password_length):
    random_character = random.choice(character)
    password.append(random_character)
print("The random password is " + "".join(password))