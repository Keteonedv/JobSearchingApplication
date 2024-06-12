import csv
import os
from users import User
from profiles import JobSeekerProfile, EmployerProfile
from vacancy import Vacancy
from application import Application 

def main():
    user_manager = User()
    job_seeker_profile_manager = JobSeekerProfile()
    employer_profile_manager = EmployerProfile()

    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Log Out")
        print("4. Update Profile")
        print("5. View Profile")
        print("6. Add Vacancy")
        print("7. Update Vacancy")
        print("8. Apply to Vacancy")
        print("9. View Applications")
        print("10. View Applied Jobs")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_type = input("Are you a Job Seeker or Employer? (Enter 'job_seeker' or 'employer'): ")

                user_manager.sign_up(username, password, user_type)

                if user_type == 'job_seeker':
                    create_profile = input("Do you want to create a profile? (yes/no): ").lower()
                    if create_profile == 'yes':
                        job_type = input("Enter job type: ")
                        salary = input("Enter expected salary: ")
                        education = input("Enter education: ")
                        experience = input("Enter experience: ")
                        job_seeker_profile_manager.create_profile({
                            'username': username,
                            'job_type': job_type,
                            'salary': salary,
                            'education': education,
                            'experience': experience
                        })
                elif user_type == 'employer':
                    create_profile = input("Do you want to create a profile? (yes/no): ").lower()
                    if create_profile == 'yes':
                        company_name = input("Enter company name: ")
                        job_openings = input("Enter job openings: ")
                        location = input("Enter location: ")
                        industry = input("Enter industry: ")
                        offered_salary = input("Enter offered salary: ")
                        employer_profile_manager.create_profile({
                            'username': username,
                            'company_name': company_name,
                            'job_openings': job_openings,
                            'location': location,
                            'industry': industry,
                            'offered_salary': offered_salary
                        })
            except (KeyboardInterrupt, EOFError):
                print("\nOperation interrupted. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

        elif choice == '2':
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_type = user_manager.login(username, password)
                if user_type:
                    print(f"Logged in as {username} ({user_type})")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                user_manager.logout()
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            user_type = input("Are you a Job Seeker or Employer? (Enter 'job_seeker' or 'employer'): ")
            if user_type == 'job_seeker':
                try:
                    username = user_manager.current_user
                    profile_updates = {}
                    profile_updates['job_type'] = input("Enter new job type: ")
                    profile_updates['salary'] = input("Enter new expected salary: ")
                    profile_updates['education'] = input("Enter new education: ")
                    profile_updates['experience'] = input("Enter new experience: ")
                    job_seeker_profile_manager.update_profile(username, profile_updates)
                except Exception as e:
                    print("Error:", e)
            elif user_type == 'employer':
                try:
                    username = user_manager.current_user
                    profile_updates = {}
                    profile_updates['company_name'] = input("Enter new company name: ")
                    profile_updates['job_openings'] = input("Enter new job openings: ")
                    profile_updates['location'] = input("Enter new location: ")
                    profile_updates['industry'] = input("Enter new industry: ")
                    profile_updates['offered_salary'] = input("Enter new offered salary: ")
                    employer_profile_manager.update_profile(username, profile_updates)
                except Exception as e:
                    print("Error:", e)

        elif choice == '5':
            user_type = input("Are you a Job Seeker or Employer? (Enter 'job_seeker' or 'employer'): ")
            if user_type == 'job_seeker':
                try:
                    profile = job_seeker_profile_manager.view_profile(user_manager.current_user)
                    if profile:
                        print(profile)
                except Exception as e:
                    print("Error:", e)
            elif user_type == 'employer':
                try:
                    profile = employer_profile_manager.view_profile(user_manager.current_user)
                    if profile:
                        print(profile)
                except Exception as e:
                    print("Error:", e)


        elif choice == '6':
            try:
                username = user_manager.current_user
                if username:
                    job_title = input("Enter job title: ")
                    job_description = input("Enter job description: ")
                    location = input("Enter location: ")
                    salary = input("Enter salary: ")
                    requirements = input("Enter requirements: ")
                    employer_profile_manager.add_vacancy(username, job_title, job_description, location, salary, requirements)
                else:
                    print("Please log in first.")
            except Exception as e:
                print("Error:", e)

        elif choice == '7':
            try:
                username = user_manager.current_user
                if username:
                    job_title = input("Enter the job title of the vacancy you want to update: ")
                    vacancy_updates = {}
                    vacancy_updates['job_description'] = input("Enter new job description (leave blank to keep current): ")
                    vacancy_updates['location'] = input("Enter new location (leave blank to keep current): ")
                    vacancy_updates['salary'] = input("Enter new salary (leave blank to keep current): ")
                    vacancy_updates['requirements'] = input("Enter new requirements (leave blank to keep current): ")
                    vacancy_updates = {k: v for k, v in vacancy_updates.items() if v}
                    employer_profile_manager.update_vacancy(username, job_title, vacancy_updates)
                else:
                    print("Please log in first.")
            except Exception as e:
                print("Error:", e)


        elif choice == '8':
            try:
                username = user_manager.current_user
                if username:
                    employer_username = input("Enter the employer's username: ")
                    job_title = input("Enter the job title: ")
                    application_text = input("Enter your application text: ")
                    application_data = {
                        'job_seeker_username': username,
                        'employer_username': employer_username,
                        'job_title': job_title,
                        'application_text': application_text
                    }
                    application_manager = Application()
                    application_manager.apply_to_vacancy(application_data)
                else:
                    print("Please log in first.")
            except Exception as e:
                print("Error:", e)

        elif choice == '9':
            try:
                username = user_manager.current_user
                if username:
                    applications = employer_profile_manager.view_applications(username)
                    if applications:
                        for application in applications:
                            print(application)
                    else:
                        print("No applications found.")
                else:
                    print("Please log in first.")
            except Exception as e:
                print("Error:", e)

        elif choice == '10':
            try:
                username = user_manager.current_user
                if username:
                    applications = job_seeker_profile_manager.view_applied_jobs(username)
                    if applications:
                        for application in applications:
                            print(application)
                    else:
                        print("No applied jobs found.")
                else:
                    print("Please log in first.")
            except Exception as e:
                print("Error:", e)

        elif choice == '11':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


        if __name__ == "__main__":
            main()
