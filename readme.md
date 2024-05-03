# User Management Module

This user management module allows for basic CRUD (Create, Read, Update, Delete) operations on user accounts within the system. It has been developed using django for the backend and html/css for the frontend.

## Features

1. Create User
   - Functionality to create a new user with necessary input fields including gender, full name, email address, mobile number, address, username, and password.
   - Proper validation of user inputs to ensure data integrity.
   - User records are stored in the database.

2. Read User
   - Retrieve and display all created user details.

3. Update User
   - Allow users to update their respective details information except email and username.
   - Implement appropriate validation for updating user data.

4. Delete User
   - Implement the ability to delete user accounts from the system.


## Technologies Used

- Backend:  Django/Python
- Frontend: HTML/CSS

## Setup Instructions

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# For Windows:
.\env\Scripts\activate
# For macOS/Linux:
source env/bin/activate

# Install Django
pip install django

# Install requirements
pip install -r requirements.txt

# Migrate into the database
python manage.py makemigrations
python manage.py migrate

# Create an admin user
python manage.py createsuperuser

# Navigate to the source directory
cd src

# Run the server
python manage.py runserver