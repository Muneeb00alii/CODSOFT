import random
import string

class PasswordGenerator:
    def __init__(self, strength, length):
        self.strength = strength
        self.length = length

    def generate_password(self):
        password = ""
        if self.strength == "weak":
            for i in range(self.length):
                password += random.choice(string.ascii_lowercase + string.digits)
        elif self.strength == "strong":
            for i in range(self.length):
                password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        return password


    def save_password(self, password):
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")

    def find_password(self, password):
        with open("passwords.txt", "r") as file:
            for line in file:
                if password in line:
                    return True
        return False


def main ():
    print("\nWelcome to Password Generator\n")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Find Password")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        strength = input("Enter the strength of the password (weak/strong): ")
        length = int(input("Enter the length of the password: "))
        password_generator = PasswordGenerator(strength, length)
        password = password_generator.generate_password()
        print("Generated Password:", password)
        password_generator.save_password(password)

    elif choice == "2":
        password = input("Enter the password to save: ")
        password_generator = PasswordGenerator("", 0)
        password_generator.save_password(password)
        print("Password saved successfully")

    elif choice == "3":
        password = input("Enter the password to find that is it used before or not: ")
        password_generator = PasswordGenerator("", 0)
        if password_generator.find_password(password):
            print("Password found")
        else:
            print("Password not found")

    elif choice == "4":
        print("Exiting...")
        exit()

    else:
        print("Invalid choice")


main()