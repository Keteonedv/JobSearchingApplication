import csv
import hashlib
import os

class User:
    def __init__(self, filename='users.csv'):
        self.filename = filename
        self.current_user = None
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self):
        if not os.path.isfile(self.filename):
            print(f"Debug: File {self.filename} does not exist. Creating file.")
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'hashed_password', 'user_type'])
        else:
            print(f"Debug: File {self.filename} already exists.")

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def sign_up(self, username, password, user_type):
        if not username or not password or not user_type:
            print("Username, password, and user type are required.")
            return

        try:
            hashed_password = self._hash_password(password)
            print(f"Debug: Writing user '{username}' to file.")
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([username, hashed_password, user_type])
            print(f"User '{username}' registered successfully.")
        except csv.Error as e:
            print(f"An error occurred while writing to the CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def login(self, username, password):
        try:
            hashed_password = self._hash_password(password)
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header
                for row in reader:
                    if len(row) != 3:
                        print(f"Debug: Malformed line: {','.join(row)}")
                        continue
                    stored_username, stored_password, stored_user_type = row
                    print(f"Debug: Checking {stored_username} == {username} and {stored_password} == {hashed_password}")
                    if stored_username == username and stored_password == hashed_password:
                        self.current_user = username
                        print("Login successful")
                        return stored_user_type
            print("Username or password incorrect")
        except Exception as e:
            print(f"An error occurred while logging in: {e}")

    def logout(self):
        if self.current_user:
            print(f"User '{self.current_user}' logged out.")
            self.current_user = None
        else:
            print("No user is logged in.")


