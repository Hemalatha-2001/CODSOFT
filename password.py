import random
import string

def password(character):
    value = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(value) for _ in range(character))

def Pass():
    print("Password Generator")

while True:
    try:
        length = int(input("Enter password length: "))
        if  length > 0:
            print("Generated Password:", password(length))
        else:
            print("Invalid input...Enter valid integer")
    except ValueError:
        print("Invalid input...Enter valid integer")

if __name__ == "__main__":
    Pass()
