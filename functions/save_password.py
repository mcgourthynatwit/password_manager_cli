import uuid
from functions import supabase_config

def save_password(email, passwordName, encryptedPassword):
    supabase = supabase_config.create_supabase_client()
    
    try:
        response = supabase.table('passwords').insert({"id": str(uuid.uuid4()), "password_name": passwordName, "email": email, "encrypt_password": encryptedPassword}).execute()
        print('Password saved successfully')
    except Exception as e:
        print('Error saving password:', e)