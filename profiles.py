import csv
import os

from application import Application
from vacancy import Vacancy

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


class JobSeekerProfile(Profile):
    def __init__(self, filename='job_seekers_profiles.csv'):
        fieldnames = ['username', 'job_type', 'salary', 'education', 'experience']
        super().__init__(filename, fieldnames)
        self.application_manager = Application()

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

    def view_applied_jobs(self, job_seeker_username):
        applications = []
        try:
            with open(self.application_manager.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['job_seeker_username'] == job_seeker_username:
                        applications.append(row)
        except Exception as e:
            print(f"An error occurred while viewing applications: {e}")
        return applications

    
class EmployerProfile(Profile):
    def __init__(self, filename='employers_profiles.csv'):
        fieldnames = ['username', 'company_name', 'job_openings', 'location', 'industry', 'offered_salary']
        super().__init__(filename, fieldnames)
        self.vacancy_manager = Vacancy()
        self.application_manager = Application()

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
    
    def add_vacancy(self, employer_username, job_title, job_description, location, salary, requirements):
        vacancy_data = {
            'employer_username': employer_username,
            'job_title': job_title,
            'job_description': job_description,
            'location': location,
            'salary': salary,
            'requirements': requirements
        }
        self.vacancy_manager.add_vacancy(vacancy_data)

    def update_vacancy(self, employer_username, job_title, vacancy_updates):
        self.vacancy_manager.update_vacancy(employer_username, job_title, vacancy_updates)

    def view_vacancies(self, employer_username):
        return self.vacancy_manager.view_vacancies(employer_username)

    def view_applications(self, employer_username):
        return self.application_manager.view_applications(employer_username)
    


