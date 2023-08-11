# Password Manager CLI

## Overview

`passwordManagerCLI` is a command-line password manager that allows users to create, store, and retrieve passwords securely. It also offers the ability to generate strong random passwords for the user.

## Features

1. **User Authentication**: Users can sign up and sign in to access their passwords.
2. **Password Generation**: Users can choose to generate a strong random password.
3. **Password Storage**: Passwords are encrypted and stored securely.
4. **Password Retrieval**: Users can retrieve their stored passwords after verifying their identity through an OTP sent via SMS.
5. **Password Update**: Users can update or delete their stored passwords.

## How to Use

1. Run the `main.py` script.
2. You will be prompted to either sign in or sign up.
3. Once authenticated, you can choose to create a new password, access stored passwords, update passwords, or sign out.

## Modules and Functions

- **User Authentication**:
  - `signIn()`: Sign in using email and password.
  - `createCredentials()`: Sign up by providing name, email, phone number, and password.
- **Password Management**:
  - `createPassword()`: Create a new password entry.
  - `getPasswords()`: Retrieve all stored passwords for the authenticated user.
  - `updatePassword()`: Update or delete a stored password.
  - `randomizePassword.generate_password()`: Generate a strong random password.
- **Utilities**:
  - `supabaseConfig.create_supabase_client()`: Create a Supabase client for database operations.
  - `twilioSend.sendMessage()`: Send an OTP via SMS for verification.

## Dependencies

- `supabase`: For database operations.
- `twilio`: For sending OTPs via SMS.
- `bcrypt`: For password hashing.
- `cryptography`: For password encryption.

## Future Improvements

- Add a function to delete a password.
- Account Help (recover password through SMS).
