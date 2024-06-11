import csv
import os

class User:
    def __init__(self, filename='users.csv'):
        self.filename = filename
        self.current_user = None
        self.setup()

    def setup(self):
        try:
            if not os.path.isfile(self.filename):
                with open(self.filename, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['username', 'hashed_password', 'user_type'])
        except Exception as e:
            print(f"An error occurred while setting up the file: {e}")

    def hash_password(self, password):
        return str(hash(password))

    def sign_up(self, username, password, user_type):
        self.setup()
        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                hashed_password = self.hash_password(password)
                writer.writerow([username, hashed_password, user_type])
            print(f"User '{username}' registered successfully.")
        except Exception as e:
            print(f"An error occurred while signing up: {e}") 

    def login(self, username, password):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    stored_username = row['username']
                    stored_password = row['hashed_password']
                    stored_user_type = row['user_type']
                    if stored_username == username and self.hash_password(password) == stored_password:
                        self.current_user = username
                        print("Login successful")
                        return stored_user_type
                print("Username or password incorrect")
        except Exception as e:
            print(f"An error occurred while logging in: {e}")

    def logout(self):
        if self.current_user is not None:
            print(f"User '{self.current_user}' logged out.")
            self.current_user = None
        else:
            print("No user is logged in.")
