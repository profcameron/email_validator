try:
    import email_validator as ev  # Attempt to import the email_validator library for validating email addresses
except ImportError:
    print("Error: The email_validator library is not installed. Please install it to use this program.")
    exit(1)  # Exit the program with an error status

# Initialize a variable to track the validity of the email address
valid = False

# Loop until a valid email address is entered
while valid == False:
    try:
        # Prompt the user to enter their email address
        address = input("Enter your email: ")

        # Validate the entered email address
        emailinfo = ev.validate_email(address)

        valid = True  # If validation is successful, set valid to True
        email = emailinfo.normalized  # Normalize the email address (e.g., convert to lowercase)

    except ev.EmailNotValidError as e:  # Handle the case where the email is not valid
        print(str(e))  # Print the error message from the exception
        print(address + " is not valid. Please re-enter.")  # Prompt the user to re-enter a valid email

# After exiting the loop, print the validated email address
print(email + " is a valid email.")
