# user.py

import csv
import os

class User:
    def __init__(self, filename='users.csv'):
        self.filename = filename
        self.current_user=None
        self.setup()

    def setup(self):
        try:
            if not os.path.isfile(self.filename):
                with open(self.filename, 'w') as f:
                    f.write('username,hashed_password\n')
        except Exception as e:
            print(f"An error ocurred while setting up the file: {e}")

    def hash_password(self, password):
        return str(hash(password))

    def sign_up(self, username, password):
        self.setup()
        try:
            with open(self.filename, 'a') as f:
                hashed_password = self.hash_password(password)
                f.write(f"{username},{hashed_password}\n")
            print(f"User '{username}' registered successfully.")
        except Exception as e:
            print(f"An error ocurred while signing up: {e}") 
        

    def login(self, username, password):
        try:
            with open(self.filename, 'r') as f:
                f.readline()  # Skip the header
                for line in f:
                    stored_username, stored_password = line.strip().split(',')
                    if stored_username == username and self.hash_password(password) == stored_password:
                        print("Login successful")
                        self.current_user=username
                        return
                print("Username or password incorrect")
        except Exception as e:
            print(f"An error occurred while logging in: {e}")

    def logout(self):
        if self.current_user is not None:
            print("User logged out.")
            self.current_usert=None
        else:
            print("No user is logged in.")

    
