import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters and join them to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
print("Welcome to the Password Generator!")

# Prompt the user for the desired password length
while True:
    try:
        length = int(input("Enter the desired length of your password: "))
        if length < 4:
            print("Password length should be at least 4 characters for security reasons. Please try again.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Generate the password
password = generate_password(length)

# Display the generated password
print(f"Your generated password is: {password}")
