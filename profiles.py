import csv
import os

class Profile:
    def __init__(self, filename='profiles.csv'):
        self.filename = filename
        self.setup()

    def setup(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'job_type', 'salary', 'education', 'experience'])

    def create_profile(self, username, job_type, salary, education, experience):
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, job_type, salary, education, experience])
        print(f"Profile for '{username}' created successfully.")

    def update_profile(self, username, profile_updates):
        profiles = {}

        # Read existing profiles into a dictionary
        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                profiles[row['username']] = {
                    'job_type': row['job_type'],
                    'salary': row['salary'],
                    'education': row['education'],
                    'experience': row['experience']
                }

        # Update the profile if the username matches
        if username in profiles:
            profiles[username].update(profile_updates)

            # Write back updated profiles
            with open(self.filename, 'w', newline='') as f:
                fieldnames = ['username', 'job_type', 'salary', 'education', 'experience']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for user, info in profiles.items():
                    writer.writerow({
                        'username': user,
                        'job_type': info['job_type'],
                        'salary': info['salary'],
                        'education': info['education'],
                        'experience': info['experience']
                    })
            print(f"Profile for '{username}' updated successfully.")
        else:
            print(f"User '{username}' not found.")

    def search_profiles(self, criteria):
        matching_profiles = []
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    profile_info = {
                        'job_type': row['job_type'],
                        'salary': row['salary'],
                        'education': row['education'],
                        'experience': row['experience']
                    }
                    if any(criteria in value for value in profile_info.values()):
                        matching_profiles.append({
                            "username": row['username'],
                            "profile_info": profile_info
                        })
        except Exception as e:
            print(f"An error occurred while searching the profiles: {e}")
        return matching_profiles

if __name__ == "__main__":
    profile_manager = Profile()

    # Creating a new profile
    profile_manager.create_profile("keti_davitadze", "Engineer", "50000", "B.Sc in Engineering", "5 years")

    # Updating the profile
    profile_manager.update_profile("Keti_davitadze", {"salary": "60000", "experience": "6 years"})

    # Searching profiles
    print(profile_manager.search_profiles("60000"))
