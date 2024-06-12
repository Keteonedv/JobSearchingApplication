import csv
import os
class Application:
    def __init__(self, filename='applications.csv'):
        self.filename = filename
        self.fieldnames = ['job_seeker_username', 'employer_username', 'job_title', 'application_text']
        self.setup()

    def setup(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.fieldnames)

    def apply_to_vacancy(self, application_data):
        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writerow(application_data)
            print(f"Application to '{application_data['job_title']}' sent successfully.")
        except Exception as e:
            print(f"An error occurred while applying to the vacancy: {e}")

    def view_applications(self, employer_username):
        applications = []

        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['employer_username'] == employer_username:
                        applications.append(row)
        except Exception as e:
            print(f"An error occurred while viewing applications: {e}")

        return applications
