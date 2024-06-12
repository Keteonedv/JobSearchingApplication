import csv
import os

class Profile:
    def __init__(self, filename, fieldnames):
        self.filename = filename
        self.fieldnames = fieldnames
        self.setup()

    def setup(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.fieldnames)

    def create_profile(self, profile_data):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fieldnames)
            writer.writerow(profile_data)
        print(f"Profile for '{profile_data['username']}' created successfully.")

    def update_profile(self, username, profile_updates):
        profiles = {}
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                profiles[row['username']] = row
        if username in profiles:
            profiles[username].update(profile_updates)
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for profile in profiles.values():
                    writer.writerow(profile)
            print(f"Profile for '{username}' updated successfully.")
        else:
            print(f"User '{username}' not found.")

    def search_profiles(self, criteria):
        matching_profiles = []
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if any(criteria in value for value in row.values()):
                        matching_profiles.append(row)
        except Exception as e:
            print(f"An error occurred while searching the profiles: {e}")
        return matching_profiles

    # def view_profile(self, username):
    #     try:
    #         with open(self.filename, 'r') as f:
    #             reader = csv.DictReader(f)
    #             for row in reader:
    #                 if row['username'] == username:
    #                     return row
    #         print(f"Profile for '{username}' not found.")
    #     except Exception as e:
    #         print(f"An error occurred while viewing the profile: {e}")
    #     return None

class JobSeekerProfile(Profile):
    def __init__(self, filename='job_seekers_profiles.csv'):
        fieldnames = ['username', 'job_type', 'salary', 'education', 'experience']
        super().__init__(filename, fieldnames)

    def view_profile(self, username):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username:
                        return row
            print(f"Profile for '{username}' not found.")
        except Exception as e:
            print(f"An error occurred while viewing the profile: {e}")
        return None

class EmployerProfile(Profile):
    def __init__(self, filename='employers_profiles.csv'):
        fieldnames = ['username', 'company_name', 'job_openings', 'location', 'industry', 'offered_salary']
        super().__init__(filename, fieldnames)

    def view_profile(self, username):
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username:
                        return row
            print(f"Profile for '{username}' not found.")
        except Exception as e:
            print(f"An error occurred while viewing the profile: {e}")
        return None

