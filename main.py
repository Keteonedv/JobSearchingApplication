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
        print("4. Update Profile")
        print("5. View Profile")
        print("6. Exit")
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
                    offered_salary = input("Enter offered salary: ")
                    employer_profile_manager.create_profile({
                        'username': username,
                        'company_name': company_name,
                        'job_openings': job_openings,
                        'location': location,
                        'industry': industry,
                        'offered_salary': offered_salary
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
            user_type = input("Are you a Job Seeker or Employer? (Enter 'job_seeker' or 'employer'): ")
            if user_type == 'job_seeker':
                updates = {}
                job_type = input("Enter new job type (leave blank to keep current): ")
                if job_type:
                    updates['job_type'] = job_type
                salary = input("Enter new expected salary (leave blank to keep current): ")
                if salary:
                    updates['salary'] = salary
                education = input("Enter new education (leave blank to keep current): ")
                if education:
                    updates['education'] = education
                experience = input("Enter new experience (leave blank to keep current): ")
                if experience:
                    updates['experience'] = experience
                job_seeker_profile_manager.update_profile(user_manager.current_user, updates)
            elif user_type == 'employer':
                updates = {}
                company_name = input("Enter new company name (leave blank to keep current): ")
                if company_name:
                    updates['company_name'] = company_name
                job_openings = input("Enter new job openings (leave blank to keep current): ")
                if job_openings:
                    updates['job_openings'] = job_openings
                location = input("Enter new location (leave blank to keep current): ")
                if location:
                    updates['location'] = location
                industry = input("Enter new industry (leave blank to keep current): ")
                if industry:
                    updates['industry'] = industry
                offered_salary = input("Enter new offered salary (leave blank to keep current): ")
                if offered_salary:
                    updates['offered_salary'] = offered_salary
                employer_profile_manager.update_profile(user_manager.current_user, updates)

        elif choice == '5':
            user_type = input("Are you a Job Seeker or Employer? (Enter 'job_seeker' or 'employer'): ")
            if user_type == 'job_seeker':
                profile = job_seeker_profile_manager.view_profile(user_manager.current_user)
            elif user_type == 'employer':
                profile = employer_profile_manager.view_profile(user_manager.current_user)
            
            if profile:
                print("Profile information:")
                for key, value in profile.items():
                    print(f"{key}: {value}")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
