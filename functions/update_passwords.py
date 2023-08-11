from functions import supabase_config
from functions.get_passwords import get_passwords
# this function is broken if password doesnt exist, should display users passwords when they prompt, should use twilio as well.
supabase = supabase_config.create_supabase_client()

table = supabase.table('passwords')

def delete(user):
    passwordName = input('What is the name of the password you want to delete?')
    response = table.select('password_name').eq('password_name', passwordName).eq('email',user.email).execute()
    if len(response) > 0:
        table.delete().eq('password_name', passwordName).execute()
        print('Password deleted')
    else:
        print('Password not found')

def update(user):
    get_passwords(user)

    passwordName = input('What is the name of the password you want to change?')
    response = table.select('password_name').eq('password_name', passwordName).eq('email',user.email).execute()
    if len(response.data) > 0:
        print('What would you like to change ?')
        
        while True:
            print('1. Password name')
            print('2. Password')
            userInput = input()
            match userInput:
                case '1':
                    newPasswordName = input('What would you like the new name to be?')
                    table.update({'password_name': newPasswordName}).eq('password_name', passwordName).eq('email',user.email).execute()
                    print('Password name updated')
                    break
                case '2':
                    newPassword = input('What would you like the new password to be?')
                    confirm = input('confirm password')
                    if newPassword == confirm:
                        table.update({'password': newPassword}).eq('password_name', passwordName).eq('email', user.email).execute()
                        print('Password updated') 
                        break
                    else:
                        print('Passwords do not match')
                        continue
                case _:
                    print('Invalid choice')
                    continue
    else:
        print('Password not found')


def update_passwords(user):
    while True:
        print('1. Update password')
        print('2. Delete password')
        print('3. Go back')
        userInput = input('Enter your choice: ')
        match userInput:
            case '1':
                update(user)
                break
            case '2':
                delete(user)
                break
            case _:
                print('Invalid choice')
                continue


