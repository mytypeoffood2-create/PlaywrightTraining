# Verify Registration Form Using 100 Unique Data Sets

# Task - 1  How to Automate and Validate a Registration Form Using Python, Playwright, Pytest, and Parametrized
# Testing with 100 Unique Test Data Sets, Including First Name, Last Name, Email, Gender, Password, and Confirm Password Fields?


import pytest
from playwright.sync_api import Page, expect

test_data = [
    ("Wali", "Rizvi", "wali@gmail.com", "Male", "Test@123", "Test@123"),
    ("Syed", "Ali", "syed@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ali", "Abbas", "ali@gmail.com", "Male", "Test@123", "Test@123"),
    ("Mohd", "Mehdi", "mohd@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rahil", "Naqvi", "rahil@gmail.com", "Male", "Test@123", "Test@123"),
    ("Zainul", "Raza", "gogi@gmail.com", "Male", "Test@123", "Test@123"),
    ("Aarav", "Sharma", "aarav@gmail.com", "Male", "Test@123", "Test@123"),
    ("Vivaan", "Verma", "vivaan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Aditya", "Singh", "aditya@gmail.com", "Male", "Test@123", "Test@123"),
    ("Arjun", "Patel", "arjun@gmail.com", "Male", "Test@123", "Test@123"),
    ("Kabir", "Malik", "kabir@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rehan", "Ansari", "rehan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ayaan", "Khan", "ayaan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Hamza", "Qureshi", "hamza@gmail.com", "Male", "Test@123", "Test@123"),
    ("Danish", "Shaikh", "danish@gmail.com", "Male", "Test@123", "Test@123"),
    ("Faizan", "Siddiqui", "faizan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Imran", "Mirza", "imran@gmail.com", "Male", "Test@123", "Test@123"),
    ("Farhan", "Choudhary", "farhan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Saad", "Hussain", "saad@gmail.com", "Male", "Test@123", "Test@123"),
    ("Omar", "Farooqui", "omar@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rohan", "Mehta", "rohan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Karan", "Kapoor", "karan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rahul", "Yadav", "rahul@gmail.com", "Male", "Test@123", "Test@123"),
    ("Aman", "Mishra", "aman@gmail.com", "Male", "Test@123", "Test@123"),
    ("Nikhil", "Jain", "nikhil@gmail.com", "Male", "Test@123", "Test@123"),
    ("Sahil", "Bhatia", "sahil@gmail.com", "Male", "Test@123", "Test@123"),
    ("Tariq", "Abbasi", "tariq@gmail.com", "Male", "Test@123", "Test@123"),
    ("Zeeshan", "Rana", "zeeshan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Asad", "Butt", "asad@gmail.com", "Male", "Test@123", "Test@123"),
    ("Bilal", "Akhtar", "bilal@gmail.com", "Male", "Test@123", "Test@123"),
    ("Hassan", "Nawaz", "hassan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ibrahim", "Aziz", "ibrahim@gmail.com", "Male", "Test@123", "Test@123"),
    ("Yusuf", "Baig", "yusuf@gmail.com", "Male", "Test@123", "Test@123"),
    ("Sameer", "Rathore", "sameer@gmail.com", "Male", "Test@123", "Test@123"),
    ("Pranav", "Desai", "pranav@gmail.com", "Male", "Test@123", "Test@123"),
    ("Dev", "Kulkarni", "dev@gmail.com", "Male", "Test@123", "Test@123"),
    ("Manav", "Joshi", "manav@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ishaan", "Garg", "ishaan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Samar", "Saxena", "samar@gmail.com", "Male", "Test@123", "Test@123"),
    ("Varun", "Reddy", "varun@gmail.com", "Male", "Test@123", "Test@123"),
    ("Akash", "Nair", "akash@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ananya", "Sharma", "ananya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Priya", "Verma", "priya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Aisha", "Khan", "aisha@gmail.com", "Female", "Test@123", "Test@123"),
    ("Sara", "Ali", "sara@gmail.com", "Female", "Test@123", "Test@123"),
    ("Zoya", "Rizvi", "zoya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Fatima", "Abbas", "fatima@gmail.com", "Female", "Test@123", "Test@123"),
    ("Meera", "Patel", "meera@gmail.com", "Female", "Test@123", "Test@123"),
    ("Neha", "Singh", "neha@gmail.com", "Female", "Test@123", "Test@123"),
    ("Pooja", "Mehta", "pooja@gmail.com", "Female", "Test@123", "Test@123"),
    ("Sana", "Malik", "sana@gmail.com", "Female", "Test@123", "Test@123"),
    ("Ira", "Kapoor", "ira@gmail.com", "Female", "Test@123", "Test@123"),
    ("Riya", "Jain", "riya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Noor", "Ansari", "noor@gmail.com", "Female", "Test@123", "Test@123"),
    ("Hiba", "Qureshi", "hiba@gmail.com", "Female", "Test@123", "Test@123"),
    ("Mariam", "Shaikh", "mariam@gmail.com", "Female", "Test@123", "Test@123"),
    ("Ayesha", "Siddiqui", "ayesha@gmail.com", "Female", "Test@123", "Test@123"),
    ("Nida", "Mirza", "nida@gmail.com", "Female", "Test@123", "Test@123"),
    ("Saira", "Choudhary", "saira@gmail.com", "Female", "Test@123", "Test@123"),
    ("Alina", "Hussain", "alina@gmail.com", "Female", "Test@123", "Test@123"),
    ("Maya", "Farooqui", "maya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Kavya", "Mehta", "kavya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Ishita", "Kapoor", "ishita@gmail.com", "Female", "Test@123", "Test@123"),
    ("Simran", "Yadav", "simran@gmail.com", "Female", "Test@123", "Test@123"),
    ("Aditi", "Mishra", "aditi@gmail.com", "Female", "Test@123", "Test@123"),
    ("Tanvi", "Jain", "tanvi@gmail.com", "Female", "Test@123", "Test@123"),
    ("Sana", "Bhatia", "sana2@gmail.com", "Female", "Test@123", "Test@123"),
    ("Zara", "Rana", "zara@gmail.com", "Female", "Test@123", "Test@123"),
    ("Anam", "Butt", "anam@gmail.com", "Female", "Test@123", "Test@123"),
    ("Hina", "Akhtar", "hina@gmail.com", "Female", "Test@123", "Test@123"),
    ("Amina", "Nawaz", "amina@gmail.com", "Female", "Test@123", "Test@123"),
    ("Noora", "Aziz", "noora@gmail.com", "Female", "Test@123", "Test@123"),
    ("Saba", "Baig", "saba@gmail.com", "Female", "Test@123", "Test@123"),
    ("Diya", "Rathore", "diya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Roshni", "Desai", "roshni@gmail.com", "Female", "Test@123", "Test@123"),
    ("Kriti", "Kulkarni", "kriti@gmail.com", "Female", "Test@123", "Test@123"),
    ("Mahi", "Joshi", "mahi@gmail.com", "Female", "Test@123", "Test@123"),
    ("Tanya", "Garg", "tanya@gmail.com", "Female", "Test@123", "Test@123"),
    ("Iram", "Saxena", "iram@gmail.com", "Female", "Test@123", "Test@123"),
    ("Naina", "Reddy", "naina@gmail.com", "Female", "Test@123", "Test@123"),
    ("Avni", "Nair", "avni@gmail.com", "Female", "Test@123", "Test@123"),
    ("Krish", "Sharma", "krish@gmail.com", "Male", "Test@123", "Test@123"),
    ("Yash", "Verma", "yash@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rizwan", "Khan", "rizwan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Arif", "Ali", "arif@gmail.com", "Male", "Test@123", "Test@123"),
    ("Sufiyan", "Rizvi", "sufiyan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Murtaza", "Abbas", "murtaza@gmail.com", "Male", "Test@123", "Test@123"),
    ("Dhruv", "Patel", "dhruv@gmail.com", "Male", "Test@123", "Test@123"),
    ("Laksh", "Singh", "laksh@gmail.com", "Male", "Test@123", "Test@123"),
    ("Ritesh", "Mehta", "ritesh@gmail.com", "Male", "Test@123", "Test@123"),
    ("Shahid", "Malik", "shahid@gmail.com", "Male", "Test@123", "Test@123"),
    ("Aqib", "Ansari", "aqib@gmail.com", "Male", "Test@123", "Test@123"),
    ("Adeel", "Qureshi", "adeel@gmail.com", "Male", "Test@123", "Test@123"),
    ("Muneeb", "Shaikh", "muneeb@gmail.com", "Male", "Test@123", "Test@123"),
    ("Arbaz", "Siddiqui", "arbaz@gmail.com", "Male", "Test@123", "Test@123"),
    ("Shayan", "Mirza", "shayan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Rayyan", "Choudhary", "rayyan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Azlan", "Hussain", "azlan@gmail.com", "Male", "Test@123", "Test@123"),
    ("Fahad", "Farooqui", "fahad@gmail.com", "Male", "Test@123", "Test@123"),
    ("Kunal", "Mehta", "kunal@gmail.com", "Male", "Test@123", "Test@123"),
    ("Siddharth", "Kapoor", "siddharth@gmail.com", "Male", "Test@123", "Test@123"),
    ("Harsh", "Yadav", "harsh@gmail.com", "Male", "Test@123", "Test@123"),
    ("Mayank", "Mishra", "mayank@gmail.com", "Male", "Test@123", "Test@123"),
    ("Raghav", "Jain", "raghav@gmail.com", "Male", "Test@123", "Test@123"),
    ("Aariz", "Bhatia", "aariz@gmail.com", "Male", "Test@123", "Test@123"),
    ("Danish", "Rana", "danish2@gmail.com", "Male", "Test@123", "Test@123"),
    ("Zubair", "Butt", "zubair@gmail.com", "Male", "Test@123", "Test@123"),
    ("Shahzaib", "Akhtar", "shahzaib@gmail.com", "Male", "Test@123", "Test@123"),
]


@pytest.mark.parametrize(
    "first_name, last_name, email, gender, password, confirm_password",
    test_data
)
def test_verify_label2(page: Page, first_name, last_name, email, gender, password, confirm_password):

    page.goto("https://demowebshop.tricentis.com/register")

    gender_field = page.get_by_label(gender, exact=True)
    gender_field.check()

    name = page.get_by_label("First name:")
    name.fill(first_name)

    lastname = page.get_by_label("Last name:")
    lastname.fill(last_name)

    Email = page.get_by_label("Email:")
    Email.fill(email)

    Password = page.get_by_label("Password:", exact=True)
    Password.fill(password)

    ConfirmPassword = page.get_by_label("Confirm password:", exact=True)
    ConfirmPassword.fill(confirm_password)

    expect(gender_field).to_be_checked()
    expect(name).to_have_value(first_name)
    expect(lastname).to_have_value(last_name)
    expect(Email).to_have_value(email)
    expect(Password).to_have_value(password)
    expect(ConfirmPassword).to_have_value(confirm_password)


# pytest -v -s test_locators_practice.py --headed