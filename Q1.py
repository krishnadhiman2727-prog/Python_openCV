# This is for a particular drone configuration
# Showing the available options to the user
print("Drone Movement Options:")
print("1. Roll")
print("2. Pitch")
print("3. Yaw")

# Take the option number as input from the user
option = int(input("Enter option number: "))

# Use conditional statements to determine which movement to perform
if option == 1:
    # Option 1 corresponds to Roll movement
    print("Slow down left motors for left roll or right motors for right roll")
elif option == 2:
    # Option 2 corresponds to Pitch movement
    print("Slow down front motors for forward pitch or rear motors for backward pitch")
elif option == 3:
    # Option 3 corresponds to Yaw movement
    print("Slow down clockwise motors for yaw left or counter clockwise for yaw right")
else:
    # Handle invalid input that is not 1, 2, or 3
    print("Invalid option selected")