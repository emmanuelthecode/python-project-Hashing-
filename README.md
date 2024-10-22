# python-project-Hashing-
This was a python project that focused on Password hashing and implemented a Graphical User Interface to hash passwords. 
Tkinter Password Validator
This Python program creates a simple Graphical User Interface (GUI) using the built-in Tkinter library to validate passwords by comparing an entered password with its hashed version. The password hashing and validation is done using the bcrypt library to ensure security.

Features
Password Hashing: User inputs are hashed using the bcrypt.hashpw() method, which includes the use of salt for added security.
Password Comparison: The program allows users to re-enter their password, and it checks if both inputs match after hashing.
Secure: Uses bcrypt’s salt mechanism to protect against rainbow table attacks.
Prerequisites
Before running the program, make sure you have the following dependencies installed:

bcrypt:

Install using pip:
bash
Copy code
pip install bcrypt
Tkinter:

Tkinter comes pre-installed with Python, but if it's missing, you can install it based on your OS:
For Ubuntu/Debian:
Copy code
sudo apt-get install python3-tk
For Windows/Mac: Tkinter should be included in your Python installation.
How It Works
The user enters a password in the first field.
The password is hashed using bcrypt, and salt is added.
The user is prompted to re-enter the password in the second field.
The program compares the re-entered password with the hashed version.
If the passwords match, the program outputs: "The passwords are the same."
If they don't match, the program outputs: "The passwords are different."


Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Run the program:

bash
Copy code
python3 password_validator.py
Enter a password in the first field, re-enter the same password in the second field, and click the Confirm button.

Code Overview
The main components of the program:

Tkinter GUI: Handles the user interface, with fields for entering and confirming the password.
bcrypt: Used for hashing the entered password and validating it with the second input.
Validation Function: The function validate_password() hashes the first password, compares it to the second password, and displays the result.
Example

Type the password in the first field.
Type the same password in the second field.
Press the Confirm button to validate the input.
