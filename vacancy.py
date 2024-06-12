import csv
import os

class Vacancy:
    def __init__(self, filename='vacancies.csv'):
        self.filename = filename
        self.fieldnames = ['employer_username', 'job_title', 'job_description', 'location', 'salary', 'requirements']
        self.setup()

    def setup(self):
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.fieldnames)

    def add_vacancy(self, vacancy_data):
        try:
            with open(self.filename, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                writer.writerow(vacancy_data)
            print(f"Vacancy '{vacancy_data['job_title']}' added successfully.")
        except Exception as e:
            print(f"An error occurred while adding the vacancy: {e}")

    def update_vacancy(self, employer_username, job_title, vacancy_updates):
        vacancies = []
        updated = False

        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['employer_username'] == employer_username and row['job_title'] == job_title:
                        row.update(vacancy_updates)
                        updated = True
                    vacancies.append(row)

            if updated:
                with open(self.filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames)
                    writer.writeheader()
                    writer.writerows(vacancies)
                print(f"Vacancy '{job_title}' updated successfully.")
            else:
                print(f"Vacancy '{job_title}' not found for employer '{employer_username}'.")

        except Exception as e:
            print(f"An error occurred while updating the vacancy: {e}")

    def view_vacancies(self, employer_username):
        vacancies = []

        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['employer_username'] == employer_username:
                        vacancies.append(row)
        except Exception as e:
            print(f"An error occurred while viewing vacancies: {e}")

        return vacancies
