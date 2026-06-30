# Predefined correct user ID and password for authentication
correct_user_id = "krishna"
correct_password = "u25ev054"

# Take inputs and convert to lowercase for case-insensitive verification
user_id = input("Enter user ID: ").lower()
password = input("Enter password: ").lower()

# Compare details
if user_id == correct_user_id and password == correct_password:
    print("Drone connected successfully")
else:
    print("Authentication failed. Invalid credentials.")