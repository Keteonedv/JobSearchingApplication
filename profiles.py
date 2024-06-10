import csv
import os

class Profile:
    def __init__(self, filename='profiles.csv'):
        self.filename = filename
        self.setup()

    def setup(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                f.write('username,profile_info\n')
                print("File created")
                
    def create_profile(self, username, profile_info):
    profile_info_str_list = []  # Initialize an empty list to hold key:value strings

    for key, value in profile_info.items():  # Iterate through each key-value pair in the dictionary
        pair_str = f"{key}:{value}"  # Create a string in the format "key:value"
        profile_info_str_list.append(pair_str)  # Add the string to the list

    profile_info_str = ';'.join(profile_info_str_list)  # Join the list into a single string, separated by semicolons

    with open(self.filename, 'a') as f:
        f.write(f"{username},{profile_info_str}\n")
    print(f"Profile for '{username}' created successfully.")
