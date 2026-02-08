import random
import string


def generatePassword(length):
    password = ""

    if length >= 14:
        pool = string.ascii_letters + string.digits + string.punctuation
    elif length >= 9:
        pool = string.ascii_letters + string.digits
    else:
        pool = string.ascii_letters

    for i in range(length):
        password += random.choice(pool)
        
    return password

if __name__ == "__main__":
    while True: 
        print("\nLevels: 5-8=Weak | 9-13=Moderate | 14+=Strong")
        userInput = input("Enter the number of characters:")

        try:
            pick = int(userInput)

            if pick < 5:
                print("Minimum 5 characters required.")
            else:
                break
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generatePassword(pick)
    print(f"Generated password: {password}")
    with open("generated_password.txt", "w") as file:
        file.write(password)


