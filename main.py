from user import User
from functions.create_password import create_password
from functions.sign_in import sign_in
from functions.sign_up import sign_up
from functions.update_passwords import update_passwords
from functions.get_passwords import get_passwords
from functions import supabase_config

supabase_config.create_supabase_client()

def promptAuth():
    print('Welcome to Password Manager: ')
    
    while True:
        print('1. sign in')
        print('2. sign up')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                valid, phoneNumber, name, email = sign_in()
                if valid:
                    user = User(name, email, phoneNumber)
                    return user
            case '2':
                valid, email, phoneNumber, name = sign_up()
                if valid:
                    user = User(name, email, phoneNumber)
                    return user
            case _:
                print('Invalid choice')
                continue

def promptAuthenticated(user):
    print('Welcome to Password Manager: ' + user.name)
    while True:
        print('1. create password')
        print('2. access passwords')
        print('3. update passwords')
        print('4. sign out')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                create_password(user.email)
            case '2':
                get_passwords(user)
            case '3':
                update_passwords(user)
            case '4':
                user.logout()
                break
            case _:
                print('Invalid choice')
                continue
                
            
user = promptAuth()
promptAuthenticated(user)

# Last todo 
# 1. Add a function to delete a password
# 2. Account Help(recover password through sms)
