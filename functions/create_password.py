from functions.save_password import save_password
from functions.generate_password import generate_password
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

CONFIRM_PASSWORD_NAME = 'y'
RENAME_PASSWORD = 'n'

# encrypt password
def encrypt_password(password):
    load_dotenv()
    key = os.getenv('ENCRYPTION_KEY')
    cipher = Fernet(key.encode('utf-8'))
    encrypted_password = cipher.encrypt(password.encode('utf-8'))

    del password
    return encrypted_password

def create_password(email):
    while True:
        password_name = input('What is the name of the password?')
        user_input = input('confirm password name: ' + password_name + ' (y/n)')
        user_input = user_input.lower()
    
        if user_input == CONFIRM_PASSWORD_NAME:
            break

        elif user_input == RENAME_PASSWORD:
            continue
        else:
            print('Invalid input. Please enter y or n.')
            continue

    print('Password:')
    while True:
        print('1. Generate strong password')
        print('2. Enter your own password')
        user_input = input('Enter your choice: ')
        match user_input:
            case '1':
                password = generate_password()
                print('Your strong password is: ' + password)
                break
            case '2':
                password = input('Enter your password: ')
                break
            case _:
                print('Invalid choice')
                continue

    encrypted_password = encrypt_password(password)
    save_password(email, password_name, encrypted_password.decode('utf-8'))

    del password_name
    del password
