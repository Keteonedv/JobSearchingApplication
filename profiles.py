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

        # Read existing profiles into a dictionary
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                profiles[row['username']] = row

        # Update the profile if the username matches
        if username in profiles:
            profiles[username].update(profile_updates)

            # Write back updated profiles
            with open(self.filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writeheader()
                for user, info in profiles.items():
                    writer.writerow(info)
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


class JobSeekerProfile(Profile):
    def __init__(self, filename='job_seekers.csv'):
        fieldnames = ['username', 'job_type', 'salary', 'education', 'experience']
        super().__init__(filename, fieldnames)


class EmployerProfile(Profile):
    def __init__(self, filename='employers.csv'):
        fieldnames = ['username', 'company_name', 'industry', 'location', 'job_openings']
        super().__init__(filename, fieldnames)