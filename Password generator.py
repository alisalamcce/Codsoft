import random
import string

def generate_password(length):
    if length < 4:
        return "Error: Password length must be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = [random.choice(characters) for _ in range(length)]
    
    # Ensure at least one character from each set
    password[0] = random.choice(string.punctuation)
    password[1] = random.choice(string.digits)
    password[2] = random.choice(string.ascii_letters)

    # Shuffle the password
    random.shuffle(password)

    return ''.join(password)

while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Error: Enter a valid length greater than 0.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
        another = input("Do you want to generate more passwords? (yes/no): ")
        if another.lower() != 'yes':
            break
    except ValueError:
        print("Error: Please enter a valid positive integer for the password length.")
