from users import User
from profiles import JobSeekerProfile, EmployerProfile

def main():
    user_manager = User()
    job_seeker_profile_manager = JobSeekerProfile()
    employer_profile_manager = EmployerProfile()

    while True:
        print("\n1. Sign Up")
        print("2. Log In")
        print("3. Log Out")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
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
                    employer_profile_manager.create_profile({
                        'username': username,
                        'company_name': company_name,
                        'job_openings': job_openings,
                        'location': location,
                        'industry': industry
                    })

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_type = user_manager.login(username, password)
            if user_type:
                print(f"Logged in as {username} ({user_type})")

        elif choice == '3':
            user_manager.logout()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
