# Your original code:
import random

def generate_password() -> None:
    print("\n=== PASSWORD GENERATOR ===")
    
    #length validation
    while True:
        try:
            length = int(input("How many characters? (8-20): "))
            if 8 <= length <= 20:
                break
            print("Please enter between 8 and 20!")
        except ValueError:
            print("Invalid input! Please type a number not letters.")
        
    chars = "abcdefghijklmnopqrstuvwxyz"
    if  input("Include uppercase? (y/n): ").lower() in ['y', 'yes']:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if input("Include numbers? (y/n): ").lower() in ['y', 'yes']:
        chars += "0123456789"
    if input("Include special characters? (y/n): ").lower() in ['y', 'yes']:
        chars += "!@#$%^&*()"
    
    password = ""
    for i in range(length):
        password += random.choice(chars)
    
    print(f"\nYour password: {password}")
if __name__ == "__main__":
    generate_password()