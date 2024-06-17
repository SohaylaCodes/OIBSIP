import string
import random

def generate_password(length):

    if length < 4:
        print("Password length should be at least 4")
        return None

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    random.shuffle(password)

    
    return ''.join(password)

def main():
    print("Welcome to the Password Generator")
    try:
        length = int(input("Enter the desired length for the password: "))
        
        password = generate_password(length)
        if password:
            print(f"\nGenerated password: {password}")
    except ValueError:
        print("Please enter a valid numerical value for the password length.")

if __name__ == "__main__":
    main()
