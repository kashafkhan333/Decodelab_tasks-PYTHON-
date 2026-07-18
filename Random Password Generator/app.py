import random
import string

def generate_password(length):
    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))

            if length < 4:
                print("Password length must be at least 4.\n")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (yes/no): ").lower()

            if again != "yes":
                print("\nThank you for using the Password Generator!")
                break

        except ValueError:
            print("Please enter a valid number.\n")


if __name__ == "__main__":
    main()
