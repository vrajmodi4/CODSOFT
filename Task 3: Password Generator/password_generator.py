import random
import string

print("===== STRONG PASSWORD GENERATOR =====")

length = int(input("Enter password length (minimum 4): "))

if length < 4:
    print("Password length must be at least 4.")
else:
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            string.punctuation
        )
        for _ in range(length - 4)
    )

    password_list = list(uppercase + lowercase + digit + special + remaining)
    random.shuffle(password_list)

    password = ''.join(password_list)

    print("\nGenerated Strong Password:")
    print(password)